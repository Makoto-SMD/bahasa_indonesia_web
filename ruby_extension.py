"""
Ruby text (furigana) Markdown extension for Python-Markdown and Zensical.

Supported Syntaxes:
1. remark-ruby syntax (Primary):
   - {漢字|かんじ}
   - {日本|にほん}
2. Bracket syntax:
   - [漢字]{かんじ}
3. Aozora Bunko syntax:
   - ｜漢字《かんじ》 or |漢字《かんじ》
   - 漢字《かんじ》 (kanji characters followed by 《reading》)
4. Popup tooltip (Abbr) syntax:
   - [単語]?(説明)
"""

from __future__ import annotations

import re
from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor


class RubyPostprocessor(Postprocessor):
    """Postprocessor that replaces simplified ruby notation with HTML <ruby> tags.

    Runs after raw HTML blocks are resolved, ensuring ruby syntax inside custom
    HTML components (e.g. <div class="ja-sentence">...</div>) works seamlessly.
    Code blocks (<pre>, <code>) and script/style tags are safely preserved.
    """

    def __init__(self, md=None, use_rp: bool = False, enable_aozora: bool = True, enable_brackets: bool = True):
        super().__init__(md)
        self.use_rp = use_rp
        self.enable_aozora = enable_aozora
        self.enable_brackets = enable_brackets

    def _make_ruby(self, base: str, ruby: str) -> str:
        base = base.strip()
        ruby = ruby.strip()
        if not base or not ruby:
            return ""
        if self.use_rp:
            return f"<ruby>{base}<rp>(</rp><rt>{ruby}</rt><rp>)</rp></ruby>"
        return f"<ruby>{base}<rt>{ruby}</rt></ruby>"

    def _make_abbr(self, text: str, title: str) -> str:
        text = text.strip()
        title = title.strip().replace('"', '&quot;')
        if not text or not title:
            return text
        return f'<abbr title="{title}">{text}</abbr>'

    def run(self, html: str) -> str:
        # 1. Stash code blocks and special tags so their contents are never transformed
        blocks: list[str] = []

        def stash(m: re.Match[str]) -> str:
            blocks.append(m.group(0))
            return f"__RUBY_STASH_{len(blocks)-1}__"

        stash_pattern = re.compile(
            r"<(pre|code|script|style)\b[^>]*>[\s\S]*?</\1>", re.IGNORECASE
        )
        html_stashed = stash_pattern.sub(stash, html)

        # 2. Abbreviation / Popup hint syntax: [text]?(tooltip)
        def repl_abbr(m: re.Match[str]) -> str:
            return self._make_abbr(m.group(1), m.group(2))

        html_stashed = re.sub(
            r"\[([^\]\r\n]+)\]\?\(([^)\r\n]+)\)",
            repl_abbr,
            html_stashed,
        )

        # 3. remark-ruby syntax: {base|ruby} or {base\|ruby}
        def repl_remark(m: re.Match[str]) -> str:
            return self._make_ruby(m.group(1), m.group(2))

        html_stashed = re.sub(
            r"\{([^{|<>]+?)(?:\\\||\|)([^}<>]+?)\}", repl_remark, html_stashed
        )

        # 4. Bracket syntax: [base]{ruby}
        if self.enable_brackets:
            def repl_bracket(m: re.Match[str]) -> str:
                return self._make_ruby(m.group(1), m.group(2))

            html_stashed = re.sub(
                r"\[([^\]<>]+)\]\{([^}<>]+)\}", repl_bracket, html_stashed
            )

        # 5. Aozora Bunko explicit syntax: ｜base《ruby》 or |base《ruby》
        def repl_aozora_explicit(m: re.Match[str]) -> str:
            return self._make_ruby(m.group(1), m.group(2))

        html_stashed = re.sub(
            r"[｜\|]([^《\s<>]+)《([^》<>]+)》", repl_aozora_explicit, html_stashed
        )

        # 6. Aozora Bunko implicit kanji syntax: 漢字《ruby》
        if self.enable_aozora:
            def repl_aozora_kanji(m: re.Match[str]) -> str:
                return self._make_ruby(m.group(1), m.group(2))

            html_stashed = re.sub(
                r"([\u4e00-\u9fff\u3005\u30f6\u30ee]+)《([^》<>]+)》",
                repl_aozora_kanji,
                html_stashed,
            )

        # 7. Restore preserved code and special tags
        for i, block in enumerate(blocks):
            html_stashed = html_stashed.replace(f"__RUBY_STASH_{i}__", block)

        return html_stashed


class RubyExtension(Extension):
    """Markdown extension to support Ruby (furigana) annotations."""

    def __init__(self, **kwargs):
        self.config = {
            "use_rp": [False, "Wrap ruby text with <rp>(</rp> and <rp>)</rp> tags"],
            "enable_aozora": [True, "Enable Aozora Bunko style: 漢字《かんじ》"],
            "enable_brackets": [True, "Enable bracket style: [漢字]{かんじ}"],
        }
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        # Priority 10 ensures this runs after raw_html (30) is expanded,
        # allowing ruby syntax inside custom HTML blocks (e.g. div.ja-sentence)
        processor = RubyPostprocessor(
            md=md,
            use_rp=self.getConfig("use_rp"),
            enable_aozora=self.getConfig("enable_aozora"),
            enable_brackets=self.getConfig("enable_brackets"),
        )
        md.postprocessors.register(processor, "ruby-postprocessor", 10)


def makeExtension(**kwargs):
    return RubyExtension(**kwargs)

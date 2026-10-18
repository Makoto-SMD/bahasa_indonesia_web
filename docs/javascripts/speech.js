/**
 * インドネシア語学習ナレッジベース - インタラクティブ音声再生 & コピー機能
 * Web Speech API (speechSynthesis id-ID) & Clipboard API
 */

(() => {
  const initInteractiveCards = () => {
    // 例文カード (.id-example) に対する処理
    const sentences = document.querySelectorAll(".id-sentence:not([data-interactive-initialized])");

    sentences.forEach((sentenceEl) => {
      sentenceEl.setAttribute("data-interactive-initialized", "true");

      const rawText = sentenceEl.textContent.trim();
      if (!rawText) return;

      // ボタンコンテナ
      const actionGroup = document.createElement("span");
      actionGroup.className = "id-action-group";

      // 1. 音声再生ボタン (Web Speech API)
      if ("speechSynthesis" in window) {
        const playBtn = document.createElement("button");
        playBtn.type = "button";
        playBtn.className = "id-btn id-btn--speech";
        playBtn.setAttribute("aria-label", "インドネシア語の音声を再生");
        playBtn.setAttribute("title", "発音を聞く (Web Speech API)");
        playBtn.innerHTML = `
          <svg class="id-btn__icon id-btn__icon--idle" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
            <path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>
          </svg>
          <svg class="id-btn__icon id-btn__icon--active" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
            <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path>
          </svg>
        `;

        playBtn.addEventListener("click", (e) => {
          e.stopPropagation();
          window.speechSynthesis.cancel();

          const utterance = new SpeechSynthesisUtterance(rawText);
          utterance.lang = "id-ID";
          utterance.rate = 0.92; // 学習者向けに自然かつ聞き取りやすい速度

          playBtn.classList.add("is-playing");

          utterance.onend = () => {
            playBtn.classList.remove("is-playing");
          };

          utterance.onerror = () => {
            playBtn.classList.remove("is-playing");
          };

          window.speechSynthesis.speak(utterance);
        });

        actionGroup.appendChild(playBtn);
      }

      // 2. コピーボタン (Clipboard API)
      if (navigator.clipboard) {
        const copyBtn = document.createElement("button");
        copyBtn.type = "button";
        copyBtn.className = "id-btn id-btn--copy";
        copyBtn.setAttribute("aria-label", "例文をクリップボードにコピー");
        copyBtn.setAttribute("title", "テキストをコピー");
        copyBtn.innerHTML = `
          <svg class="id-btn__icon id-btn__icon--copy" xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
          </svg>
          <svg class="id-btn__icon id-btn__icon--check" xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="20 6 9 17 4 12"></polyline>
          </svg>
        `;

        copyBtn.addEventListener("click", async (e) => {
          e.stopPropagation();
          try {
            await navigator.clipboard.writeText(rawText);
            copyBtn.classList.add("is-copied");
            setTimeout(() => {
              copyBtn.classList.remove("is-copied");
            }, 1800);
          } catch (err) {
            console.warn("Clipboard write failed:", err);
          }
        });

        actionGroup.appendChild(copyBtn);
      }

      sentenceEl.appendChild(actionGroup);
    });
  };

  // 初回実行
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initInteractiveCards);
  } else {
    initInteractiveCards();
  }

  // Material for MkDocs Instant Navigation (SPA遷移) 購読対応
  if (typeof document$ !== "undefined") {
    document$.subscribe(initInteractiveCards);
  }
})();

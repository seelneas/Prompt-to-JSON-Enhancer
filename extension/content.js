chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg === "GET_SELECTION") {
    const sel = window.getSelection().toString().trim();
    if (sel) return sendResponse({ text: sel });
    const el = document.activeElement;
    if (el && (el.tagName === "TEXTAREA" || (el.tagName === "INPUT" && el.type === "text"))) {
      return sendResponse({ text: el.value || "" });
    }
    return sendResponse({ text: "" });
  }
});

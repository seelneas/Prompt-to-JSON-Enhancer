const grabBtn = document.getElementById("grab-btn");
const enhanceBtn = document.getElementById("enhance-btn");
const copyBtn = document.getElementById("copy-btn");
const promptInput = document.getElementById("prompt-input");
const resultEl = document.getElementById("result");
const statusEl = document.getElementById("status");

grabBtn.addEventListener("click", async () => {
  statusEl.textContent = "Grabbing selection from active tab...";
  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const response = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: () => {
        const sel = window.getSelection().toString().trim();
        if (sel) return sel;
        const el = document.activeElement;
        if (el && (el.tagName === "TEXTAREA" || (el.tagName === "INPUT" && el.type === "text"))) {
          return el.value || "";
        }
        const areas = document.querySelectorAll('textarea, input[type="text"], [role="textbox"]');
        for (const a of areas) {
          if (a && a.value && a.value.trim().length > 0) return a.value.trim();
        }
        return "";
      }
    });
    const grabbed = response?.[0]?.result || "";
    if (!grabbed) {
      statusEl.textContent = "No selection or input value found on page.";
      return;
    }
    promptInput.value = grabbed;
    statusEl.textContent = "Copied prompt into the editor.";
  } catch (err) {
    console.error(err);
    statusEl.textContent = "Error grabbing selection: " + err.message;
  }
});

enhanceBtn.addEventListener("click", async () => {
  const prompt = promptInput.value.trim();
  if (!prompt) {
    statusEl.textContent = "Please paste or grab a prompt first.";
    return;
  }
  statusEl.textContent = "Sending to backend for enhancement...";
  resultEl.textContent = "";
  try {
    const resp = await fetch("http://localhost:8000/enhance", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt })
    });
    if (!resp.ok) {
      const t = await resp.text();
      statusEl.textContent = "Backend error: " + resp.status + " - " + t;
      return;
    }
    const data = await resp.json();
    const pretty = JSON.stringify(data, null, 2);
    resultEl.textContent = pretty;
    statusEl.textContent = "Success — JSON ready.";
  } catch (err) {
    console.error(err);
    statusEl.textContent = "Network error: " + err.message;
  }
});

copyBtn.addEventListener("click", async () => {
  const text = resultEl.textContent;
  if (!text) {
    statusEl.textContent = "Nothing to copy.";
    return;
  }
  try {
    await navigator.clipboard.writeText(text);
    statusEl.textContent = "JSON copied to clipboard.";
  } catch (err) {
    statusEl.textContent = "Failed to copy: " + err.message;
  }
});

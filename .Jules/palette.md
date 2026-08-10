## 2026-08-10 - Telegram Custom Keyboard Layouts
**Learning:** Telegram custom keyboards (`ReplyKeyboardMarkup`) default to a large size and single-row layouts can become cramped and difficult to tap on mobile devices.
**Action:** Always set `resize_keyboard=True` and organize long lists of buttons into logical multi-row grids (e.g., 2x2 instead of 1x4) to optimize mobile UX and prevent keyboards from obscuring chat history.

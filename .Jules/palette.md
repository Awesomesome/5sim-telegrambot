## 2026-08-08 - Telegram Custom Keyboard Optimization for Mobile UX
**Learning:** Mobile Telegram users experience excessive scrolling and awkwardly large buttons when custom keyboards (`ReplyKeyboardMarkup`) default to single-column layouts and lack the `resize_keyboard=True` parameter.
**Action:** Always set `resize_keyboard=True` to adjust button height for mobile screens, and format lists into logical grids (e.g., 2-column arrays like `[items[i:i+2] for i in range(0, len(items), 2)]`) to fit more choices in less screen space.

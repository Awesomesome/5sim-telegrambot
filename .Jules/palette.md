## 2024-05-18 - Telegram Keyboard Optimization for Mobile
**Learning:** Telegram custom keyboards can take up excessive screen space on mobile devices and long single-column lists require excessive scrolling, degrading the user experience.
**Action:** Always use `resize_keyboard=True` when instantiating `ReplyKeyboardMarkup` to optimize vertical space on mobile, and chunk long lists into multi-column logical grids (e.g., 3 columns) to reduce scrolling.

## 2024-05-18 - Telegram Keyboard Optimization
**Learning:** Telegram custom keyboards (`ReplyKeyboardMarkup`) display as excessively tall, single-column lists on mobile by default, causing unnecessary scrolling and poor UX.
**Action:** When creating custom keyboards in Telegram bots, use `resize_keyboard=True` to adapt button sizes to mobile screens, and organize long lists of options (like countries or products) into multi-column grids (e.g., 2 columns) to minimize scrolling.

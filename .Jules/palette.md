## 2024-03-21 - Telegram Custom Keyboard Layouts for Mobile
**Learning:** Default Telegram custom keyboards (`ReplyKeyboardMarkup`) take up too much vertical screen space on mobile devices and single rows of many buttons are hard to tap.
**Action:** Always set `resize_keyboard=True` to shrink the keyboard to fit the buttons, and organize main menu options into grids (e.g., 2x2) rather than single, long rows.

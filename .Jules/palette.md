## 2023-10-27 - Telegram Custom Keyboard Optimization
**Learning:** Custom Telegram keyboards (`ReplyKeyboardMarkup`) display as large, single-column lists by default, which can overwhelm the mobile UI and cause a poor experience. Emojis and accidental trailing spaces also frequently break strict string equality checks.
**Action:** Always set `resize_keyboard=True` to scale down buttons on mobile. Arrange static menu options into logical 2x2 grids rather than a single list. Use the `in` operator (e.g. `if 'keyword' in user_input:`) to parse input gracefully so emojis and spaces are ignored.

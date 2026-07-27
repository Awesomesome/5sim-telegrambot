
## 2024-05-24 - Improve Telegram Keyboard UX
**Learning:** Default Telegram custom keyboards (`ReplyKeyboardMarkup`) can be overwhelmingly large on mobile devices if `resize_keyboard=True` is not explicitly set, negatively impacting UX. Additionally, a long list of main menu options in a single row is hard to read.
**Action:** Always set `resize_keyboard=True` when instantiating `ReplyKeyboardMarkup` to ensure mobile-friendly sizes, and format main menu buttons in logical grids (e.g., 2x2) rather than single rows for better readability.

## 2024-05-24 - Telegram Custom Keyboard Optimization
**Learning:** Default Telegram custom keyboards stretch vertically to fill device width, leading to excessive scrolling when displaying long lists of options (like countries, products, operators).
**Action:** Always set `resize_keyboard=True` in `ReplyKeyboardMarkup` for mobile optimization, and chunk long single-column option lists into multi-column grids (e.g., rows of 3) using a helper function.

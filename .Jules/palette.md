## 2024-05-18 - Telegram Keyboard Optimization
**Learning:** Long single-column lists in Telegram custom keyboards (`ReplyKeyboardMarkup`) cause excessive scrolling and a poor user experience on mobile devices. Additionally, failing to set `resize_keyboard=True` makes the keyboard take up too much vertical space.
**Action:** Use a utility function like `chunk_list` to organize long lists of options (like countries or products) into multi-column grids (e.g., 3 columns). Always set `resize_keyboard=True` on `ReplyKeyboardMarkup` instances to optimize the layout for mobile.

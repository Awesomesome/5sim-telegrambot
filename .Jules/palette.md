## 2026-10-24 - Mobile Optimization for Telegram Keyboards
**Learning:** Long single-column `ReplyKeyboardMarkup` lists cause excessive scrolling and poor scannability on mobile devices. Native Telegram keyboards do not auto-resize by default, hiding messages.
**Action:** Always set `resize_keyboard=True` and chunk long option lists (like countries, products, operators) into multi-column grids (e.g., using `chunk_list`). Ensure options are sorted alphabetically for findability.

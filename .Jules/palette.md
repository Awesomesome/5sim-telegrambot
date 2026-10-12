## 2023-10-12 - Telegram Keyboard Mobile Optimization
**Learning:** Long single-column lists in Telegram custom keyboards cause excessive scrolling on mobile and hinder scannability. Missing `resize_keyboard=True` makes keyboards take up too much vertical screen space.
**Action:** Sort and chunk list arrays into multi-column grids (e.g., using `chunk_list`) and always set `resize_keyboard=True` when instantiating `ReplyKeyboardMarkup` to improve mobile UX.

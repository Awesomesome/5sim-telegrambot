## 2026-10-25 - Telegram Keyboard Mobile Optimization
**Learning:** Long single-column lists in Telegram custom keyboards create excessive scrolling on mobile devices, reducing scannability and findability of options.
**Action:** Always sort options alphabetically and chunk them into multi-column grids (e.g., using `chunk_list`), and ensure `resize_keyboard=True` is set on all `ReplyKeyboardMarkup` instances.

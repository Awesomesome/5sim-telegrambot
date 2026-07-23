## 2024-05-24 - Mobile-Optimized Telegram Keyboards
**Learning:** Telegram custom keyboards (`ReplyKeyboardMarkup`) without `resize_keyboard=True` take up too much vertical space on mobile devices, leading to a poor user experience. Also, single wide rows are hard to read and tap, and strict string matching breaks when emojis are added to buttons.
**Action:** Always set `resize_keyboard=True`, organize buttons into logical grids, and check inputs using the `in` operator (e.g., `'yes' in text.lower()`) to gracefully handle emojis.

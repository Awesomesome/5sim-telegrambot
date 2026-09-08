## 2024-05-24 - Telegram Keyboard Mobile Optimization
**Learning:** Telegram custom keyboards can become unusable on mobile devices when long, single-column lists are presented or when buttons take up too much vertical space, requiring excessive scrolling.
**Action:** When designing Telegram bots with `ReplyKeyboardMarkup`, always use `resize_keyboard=True` to adjust button height for mobile. Furthermore, use `chunk_list` to break long 1D option lists into multi-column 2D grids (e.g., 3 columns) to improve scannability and reduce scrolling fatigue.

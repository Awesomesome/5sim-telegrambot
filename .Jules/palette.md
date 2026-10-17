## 2024-03-24 - Mobile-Optimized Telegram Keyboards
**Learning:** Telegram custom keyboards become inaccessible on mobile when presented as long single-column lists (requiring excessive scrolling) or when `resize_keyboard=True` is omitted (occupying too much vertical space). Furthermore, unordered lists increase cognitive load during scanning.
**Action:** Always set `resize_keyboard=True` on `ReplyKeyboardMarkup`, sort user-facing options alphabetically for findability, and use a utility function to chunk long lists into multi-column grids.

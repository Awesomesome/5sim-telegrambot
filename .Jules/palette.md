## 2024-05-19 - Mobile-Optimized Telegram Keyboards
**Learning:** Telegram custom keyboards (`ReplyKeyboardMarkup`) can be difficult to use on mobile devices if they have too many items in a single column, requiring excessive scrolling. Additionally, omitting `resize_keyboard=True` causes keyboards to occupy too much vertical screen space.
**Action:** When designing or updating Telegram keyboards, always use `resize_keyboard=True`. For lists with many items, organize the buttons into multi-column grids (e.g., chunking into 3 items per row) to ensure a compact, user-friendly mobile experience.

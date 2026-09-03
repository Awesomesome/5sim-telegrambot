## 2024-06-25 - Custom Keyboard Sizing on Telegram
**Learning:** Custom keyboards on Telegram take up half the user's screen by default which can be overwhelming and bad UX. Large lists displayed in single columns require extensive scrolling.
**Action:** Always set `resize_keyboard=True` when creating `ReplyKeyboardMarkup` elements so they dynamically resize based on their contents. Use grouping logic like a `chunk_list` function to arrange long arrays (like countries or operators) into multi-column grids.

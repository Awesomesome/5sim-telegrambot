## 2024-05-18 - [Keyboard Mobile Optimization]
**Learning:** Long single-column lists in Telegram custom keyboards cause excessive scrolling on mobile.
**Action:** Use chunk_list helper to group options into grids and always set resize_keyboard=True for ReplyKeyboardMarkup.

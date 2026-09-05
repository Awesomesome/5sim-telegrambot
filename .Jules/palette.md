## 2024-09-05 - Mobile Optimization for Telegram Custom Keyboards
**Learning:** Telegram custom keyboards (`ReplyKeyboardMarkup`) without `resize_keyboard=True` render at maximum height on mobile, obstructing the chat view. Long, single-column lists force users to scroll excessively, degrading the UX significantly.
**Action:** Always set `resize_keyboard=True` for Telegram custom keyboards to allow them to adapt to the mobile screen size. Utilize multi-column grids (chunking lists) for large sets of options to minimize scrolling and create a more intuitive, compact layout.

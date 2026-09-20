## 2026-09-20 - Mobile-Optimized Telegram Keyboards
**Learning:** In Telegram bots, default custom keyboards take up massive screen real estate and render as single-column vertical lists by default, which creates poor UX for selecting from large sets of options (like countries or operators).
**Action:** Always enable `resize_keyboard=True` in `ReplyKeyboardMarkup` to scale the UI properly on mobile devices, and pre-process flat lists into multi-column nested arrays (e.g., using a chunking utility) to group options into intuitive grids that reduce scrolling.

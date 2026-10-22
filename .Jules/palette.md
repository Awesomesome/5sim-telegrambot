## 2026-10-22 - Mobile-Optimized Telegram Keyboards
**Learning:** Long single-column custom keyboards without resizing consume excessive screen space on mobile, causing scroll fatigue and poor scannability.
**Action:** Always apply `resize_keyboard=True` to `ReplyKeyboardMarkup` and chunk long lists into multi-column grids (e.g., 2 columns) with alphabetically sorted options to improve layout and findability.

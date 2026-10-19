## 2024-10-24 - Mobile Optimized Custom Keyboards
**Learning:** Telegram custom keyboards can occupy too much vertical screen space on mobile devices and single-column lists require excessive scrolling.
**Action:** Always set `resize_keyboard=True` on `ReplyKeyboardMarkup`, and sort/chunk long lists into multi-column grids for better scannability and findability.
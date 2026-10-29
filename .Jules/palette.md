## 2026-10-29 - Mobile-Optimized Telegram Keyboards
**Learning:** Single-column lists and unresized keyboards create excessive scrolling and take up too much vertical screen space on mobile Telegram clients, reducing scannability and findability.
**Action:** Always set `resize_keyboard=True` and chunk long alphabetical lists into multi-column grids (e.g., 2 or 3 columns) using a helper function to improve mobile UX.

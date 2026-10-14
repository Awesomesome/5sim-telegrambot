## 2026-10-14 - Optimize Telegram Keyboards
**Learning:** Telegram custom keyboards (`ReplyKeyboardMarkup`) without `resize_keyboard=True` take up too much vertical space on mobile devices. Long, single-column lists are difficult to scan and require excessive scrolling.
**Action:** Always set `resize_keyboard=True` for mobile optimization. Organize buttons into logical grids, specifically sorting/alphabetizing and chunking long lists into multi-column grids (e.g., 3 columns) to prevent excessive scrolling and aid scannability.

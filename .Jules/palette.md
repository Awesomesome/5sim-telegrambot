## 2024-05-24 - Telegram Custom Keyboard Layouts
**Learning:** Long single-column lists in Telegram custom keyboards cause excessive scrolling and poor scannability on mobile devices.
**Action:** Always set `resize_keyboard=True` for mobile optimization. Organize buttons into logical grids, specifically sorting/alphabetizing and chunking long lists into multi-column grids (using tools like `chunk_list`) to prevent excessive scrolling and aid scannability.

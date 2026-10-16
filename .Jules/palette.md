## 2026-10-16 - Optimize Telegram Custom Keyboards for Scannability
**Learning:** Telegram custom keyboards without `resize_keyboard=True` or chunking result in poor mobile scannability and excessive scrolling for long single-column lists (like countries or operators).
**Action:** Always organize buttons into logical grids by sorting/alphabetizing and chunking long lists into multi-column grids (using `utils.chunk_list`), and ensure `resize_keyboard=True` is set for optimal mobile UX.

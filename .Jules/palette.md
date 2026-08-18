## 2024-05-23 - Telegram Custom Keyboard Optimization
**Learning:** Telegram custom keyboards can quickly overwhelm mobile screens if lists are long. Additionally, default sizing looks large and unnatural.
**Action:** Always set `resize_keyboard=True` to allow Telegram to optimize key size. Chunk long lists (like countries or products) into multi-column grids (e.g., 3 items per row) to prevent excessive scrolling and improve navigation efficiency.

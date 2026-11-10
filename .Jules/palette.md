## 2024-05-24 - Mobile Keyboard Scannability
**Learning:** Telegram custom keyboards default to full width, causing long single-column lists to create excessive vertical scrolling and poor scannability on mobile devices.
**Action:** Always set `resize_keyboard=True` and utilize a helper like `chunk_list()` to format long selections (e.g., countries, products) into alphabetical, multi-column grids for findability and reduced scroll fatigue. Additionally, utilize defensive ordering `['No', 'Yes']` for consequential actions.

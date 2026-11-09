## 2024-11-09 - Mobile Keyboards & Defensive UX
**Learning:** Scrolling through long single-column lists (like countries) is tedious, and destructive actions need deliberate friction.
**Action:** Chunk long arrays into multi-column grids using resize_keyboard=True and sort options alphabetically. Apply defensive ordering (e.g. ['No', 'Yes']) for destructive confirmations.

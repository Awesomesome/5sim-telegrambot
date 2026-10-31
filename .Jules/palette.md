## 2024-05-24 - Mobile Keyboard Layout Optimization
**Learning:** Long single-column custom keyboards cause excessive scrolling on mobile and hide choices.
**Action:** Refactored keyboards to use resize_keyboard=True and implemented chunk_list to format alphabetical options into multi-column grids for better scannability.

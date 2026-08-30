## 2024-05-18 - Optimize Telegram custom keyboards for mobile UI
**Learning:** Telegram custom keyboards can take up excessive screen space on mobile devices and single-column lists require extensive scrolling, severely degrading the UX.
**Action:** When creating `ReplyKeyboardMarkup` objects, always set `resize_keyboard=True` to scale down the keyboard natively. For long lists of options (like countries or products), chunk the single list into multi-column grids (arrays of arrays) to condense the layout and reduce scrolling.

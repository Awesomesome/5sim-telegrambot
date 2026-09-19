## 2024-05-16 - Telegram Custom Keyboard Optimization
**Learning:** Single-column lists of choices in Telegram custom keyboards cause excessive scrolling on mobile devices, leading to poor usability. Furthermore, neglecting to set `resize_keyboard=True` forces keyboards to take up full vertical space, hindering the view of chat history.
**Action:** When implementing Telegram custom keyboards (`ReplyKeyboardMarkup`), organize lists of items into multi-column grids (chunking by 3 or similar) and explicitly set `resize_keyboard=True` to adapt to mobile screens efficiently.

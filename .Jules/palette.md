## 2024-05-24 - Mobile Keyboard Optimization
**Learning:** Telegram custom keyboards can easily overwhelm the mobile viewport if not properly configured. Long single-column lists force excessive scrolling, and omitting `resize_keyboard=True` causes keyboards to occupy far too much vertical space by default.
**Action:** When building `ReplyKeyboardMarkup`, always pass `resize_keyboard=True` (as the first kwarg after the layout array). Organize long lists (like countries, products, operators) into multi-column grid lists using a chunking utility.

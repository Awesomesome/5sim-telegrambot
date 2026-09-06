## 2024-09-06 - Telegram Keyboard UX and Accessibility
**Learning:** Telegram's custom keyboards (`ReplyKeyboardMarkup`) can be overwhelmingly large on mobile screens if not resized. Furthermore, long single-column lists force users into excessive scrolling, harming accessibility and ease-of-use.
**Action:** Always set `resize_keyboard=True` when instantiating custom keyboards to optimize for mobile screens. Utilize a multi-column grid by chunking list items using the `chunk_list` utility function to condense choices and prevent excessive scrolling.

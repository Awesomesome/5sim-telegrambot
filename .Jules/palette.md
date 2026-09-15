## 2026-09-15 - Telegram Keyboard UX and Input Handling
**Learning:** Single-column Telegram keyboards create excessive scrolling on mobile. Strict string equivalence and regex matching break when users input text alongside emojis or use partial matches.
**Action:** Use `resize_keyboard=True` and chunk lists into multi-column grids (e.g., using `chunk_list` helper). Prefer `Filters.text & ~Filters.command` in `ConversationHandler` and partial matching like `.startswith()` for resilient user input parsing.

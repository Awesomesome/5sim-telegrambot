## 2024-05-15 - Improve Telegram Keyboard UX and Interaction

**Learning:** When adding emojis to Telegram reply keyboards to improve visual appeal, strict string matching (`==`) or exact regex (`^$`) on the backend fails, breaking conversation flows.

**Action:** Organize main keyboards into a 2x2 grid with `resize_keyboard=True` for better mobile usability. Use `.startswith()` (or similar partial matching) for button text handlers and `Filters.text & ~Filters.command` instead of strict regex in `ConversationHandler` states to gracefully handle text paired with emojis.

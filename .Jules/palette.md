## 2024-07-26 - Flexible Input Handling for Telegram Keyboards
**Learning:** Telegram users often input text alongside emojis when using custom keyboards, which causes rigid input validations (like `==` or strict regex matching) to fail.
**Action:** When handling Telegram bot custom keyboard responses, always use `resize_keyboard=True` for mobile optimization and use the `in` operator (or flexible text filters) instead of strict equality to gracefully accommodate responses mixed with emojis.

## 2024-08-03 - Mobile-Optimized Telegram Keyboards
 **Learning:** Telegram custom keyboards default to the size of the standard keyboard, which takes up too much screen space and squishes buttons if not organized in a grid. Also, users frequently add emojis or tap quickly, so strict regex or equality matching on text input often fails gracefully.
 **Action:** Always set `resize_keyboard=True` and organize buttons into logical grids for better mobile UX. Use partial matching (e.g., `.startswith()`) and `Filters.text & ~Filters.command` for boolean/text choices instead of strict regex.

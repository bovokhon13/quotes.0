translations = {
    "en": {
        "welcome": "Welcome to the Quote Bot! Use /quote to get a random literary quote.",
        "help": "Available commands:\n/quote - Get a random quote\n/favorites - View saved quotes\n/delete_quote - Delete a quote\n/language - Change language",
        "choose_language": "Choose a language:",
        "quote": "Quote: {quote}",
        "quote_saved": "Quote saved!",
        "no_favorites": "You have no favorite quotes.",
        "favorites": "Your favorite quotes:\n{quotes}",
        "enter_quote_index": "Enter the number of the quote to delete:",
        "quote_deleted": "Quote deleted!",
        "invalid_index": "Invalid quote number.",
        "invalid_input": "Please enter a valid number.",
        "stats": "Stats: {users} users, {quotes} quotes saved."
    },
    "ru": {
        "welcome": "Добро пожаловать в бот с цитатами! Используйте /quote, чтобы получить случайную цитату.",
        "help": "Доступные команды:\n/quote - Получить случайную цитату\n/favorites - Просмотреть сохраненные цитаты\n/delete_quote - Удалить цитату\n/language - Сменить язык",
        "choose_language": "Выберите язык:",
        "quote": "Цитата: {quote}",
        "quote_saved": "Цитата сохранена!",
        "no_favorites": "У вас нет сохраненных цитат.",
        "favorites": "Ваши избранные цитаты:\n{quotes}",
        "enter_quote_index": "Введите номер цитаты для удаления:",
        "quote_deleted": "Цитата удалена!",
        "invalid_index": "Неверный номер цитаты.",
        "invalid_input": "Пожалуйста, введите корректное число.",
        "stats": "Статистика: {users} пользователей, {quotes} сохраненных цитат."
    }
}

def get_translation(lang_code: str, key: str) -> str:
    return translations.get(lang_code, translations["en"]).get(key, key)

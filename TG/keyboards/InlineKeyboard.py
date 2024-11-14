from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_habit_choice_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="➕ Добавить полезную привычку",
                              callback_data="useful")],
        [InlineKeyboardButton(text="❌ Отказаться от вредной привычки",
                              callback_data="harmful")],
        [InlineKeyboardButton(text="🔍 Отслеживание привычек",
                              callback_data="track")],
        [InlineKeyboardButton(text="⚙️ Редактировать привычки",
                              callback_data="update_habits")],
        [InlineKeyboardButton(text="❌ Отмена", callback_data="cancel")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def completion_marks_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="✅ Я выполнил!",
                              callback_data="completed")],
        [InlineKeyboardButton(text="❌ Я не выполнил!",
                              callback_data="not_fulfill")],
        [InlineKeyboardButton(text="❌ Отмена", callback_data="cancel")]

    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def track_habit_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="➕ Начать отслеживать привычку",
                              callback_data="begin")],
        [InlineKeyboardButton(text="❌ Прекратить отслеживать привычку",
                              callback_data="cease")],
        [InlineKeyboardButton(text="🔄  Назад", callback_data="back")]

    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def create_track_habits_inline_keyboard(habits: dict, is_tracked: bool) -> InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру с привычками, отсортированными по флагу отслеживания.

    :param habits: Список привычек в формате словарей.
    :param is_tracked: Флаг отслеживания привычек. True для отслеживаемых привычек, False для неотслеживаемых.
    :return: Инлайн-клавиатура.
    """
    if not habits:
        habits = []
    # Фильтруем привычки по флагу отслеживания
    filtered_habits = [habit for habit in habits if habit.get("is_tracked") == is_tracked]

    # Создаем список для кнопок
    buttons = []

    if filtered_habits:
        # Для каждой отфильтрованной привычки создаем кнопку
        for habit in filtered_habits:
            habit_name = habit["name"]
            habit_id = habit["id"]
            # Создаем кнопку с названием привычки и её идентификатором как callback_data
            button = InlineKeyboardButton(text=habit_name, callback_data=f"habit_{habit_id}")
            # Добавляем кнопку в список кнопок
            buttons.append([button])  # добавляем кнопку в отдельный список, чтобы создать новый ряд
    else:
        # Если нет привычек с нужным флагом, добавляем сообщение
        no_habits_button = InlineKeyboardButton(
            text="Нет привычек с этим статусом",
            callback_data="no_habits"
        )
        buttons.append([no_habits_button])

    # Добавляем кнопку "🔄 Назад" в отдельный ряд
    back_button = InlineKeyboardButton(text="🔄 Назад", callback_data="back")
    buttons.append([back_button])

    # Создаем инлайн-клавиатуру, передавая список списков кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


def update_habits_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="✏️  Изменить привычку", callback_data="change")],
        [InlineKeyboardButton(text="❌  Удалить привычку", callback_data="delete")],
        [InlineKeyboardButton(text="🔄  Назад", callback_data="back")]

    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def create_change_fields_keyboard(habit_id: int) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="Изменить название", callback_data=f"change_name_{habit_id}")],
        [InlineKeyboardButton(text="Изменить описание", callback_data=f"change_description_{habit_id}")],
        [InlineKeyboardButton(text="Изменить целевые дни", callback_data=f"change_target_days_{habit_id}")],
        [InlineKeyboardButton(text="Изменить дату начала", callback_data=f"change_start_date_{habit_id}")],
        [InlineKeyboardButton(text="🔄 Назад", callback_data="back")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def useful_habit_choice_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="💪 Здоровье", callback_data="health")],
        [InlineKeyboardButton(text="🏃 Спорт", callback_data="sport")],
        [InlineKeyboardButton(text="🍏 Питание", callback_data="nutrition")],
        [InlineKeyboardButton(text="✍️ Свой вариант", callback_data="option")],
        [InlineKeyboardButton(text="🔄 Назад", callback_data="back")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def health_habit_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="😴 Сон", callback_data="sleep")],
        [InlineKeyboardButton(text="💧 Гидратация", callback_data="hydration")],
        [InlineKeyboardButton(text="🧘‍♀️ Медитация", callback_data="meditation")],
        [InlineKeyboardButton(text="✍️ Свой вариант", callback_data="option")],
        [InlineKeyboardButton(text="🔄 Назад", callback_data="back")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard


def sport_habit_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="🏋️‍♂️ Силовые тренировки", callback_data="strength_training")],
        [InlineKeyboardButton(text="🏃 Бег", callback_data="running")],
        [InlineKeyboardButton(text="🏊 Плавание", callback_data="swimming")],
        [InlineKeyboardButton(text="✍️ Свой вариант", callback_data="option")],
        [InlineKeyboardButton(text="🔄 Назад", callback_data="back")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard


def nutrition_habit_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="🥗 Овощи и фрукты", callback_data="fruits_veggies")],
        [InlineKeyboardButton(text="🍳 Завтрак", callback_data="breakfast")],
        [InlineKeyboardButton(text="🥤 Снижение сахара", callback_data="less_sugar")],
        [InlineKeyboardButton(text="✍️ Свой вариант", callback_data="option")],
        [InlineKeyboardButton(text="🔄 Назад", callback_data="back")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard


def harmful_habit_choice_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="🚬 Курение", callback_data="smoking")],
        [InlineKeyboardButton(text="🍺 Алкоголь", callback_data="alcohol")],
        [InlineKeyboardButton(text="✍️ Свой вариант", callback_data="option")],
        [InlineKeyboardButton(text="🔄 Назад", callback_data="back")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


# Функция для создания инлайн-клавиатуры на основе списка привычек
def create_habits_inline_keyboard(habits: dict) -> InlineKeyboardMarkup:
    # Создаем список для кнопок
    buttons = []

    if habits:
        # Для каждой привычки создаем кнопку
        for habit in habits:
            habit_name = habit["name"]
            habit_id = habit["id"]
            # Создаем кнопку с названием привычки и её идентификатором как callback_data
            button = InlineKeyboardButton(text=habit_name, callback_data=f"habit_{habit_id}")
            # Добавляем кнопку в список кнопок
            buttons.append([button])  # добавляем кнопку в отдельный список, чтобы создать новый ряд

        # Добавляем кнопку "🔄 Назад"
        back_button = InlineKeyboardButton(text="🔄 Назад", callback_data="back")
        buttons.append([back_button])  # добавляем кнопку "Назад" в отдельный ряд

    else:
        # Если привычек нет, добавляем сообщение, что привычек пока нет
        no_habits_button = InlineKeyboardButton(text="Привычек пока нет", callback_data="no_habits")
        buttons.append([no_habits_button])
        # Также добавляем кнопку "🔄 Назад" в случае отсутствия привычек
        back_button = InlineKeyboardButton(text="🔄 Назад", callback_data="back")
        buttons.append([back_button])  # добавляем кнопку "Назад" в отдельный ряд

    # Создаем инлайн-клавиатуру, передавая список списков кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


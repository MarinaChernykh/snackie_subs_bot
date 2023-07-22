"""
Texts for bot answers
"""

BOT_COMMANDS_INFO = (
    ("start",
     "Начало работы с ботом",
     "При отправке этой команды происходит начало взаимодействие с ботом"
     ),
    ("help",
     "Помощь и справка",
     "При отправке этой команды бот покажет, какие команды доступны для взаимодействия с ним",
     ),
)
# MAIN
TEXT_HELP = "Помощь и справка о боте\n\n" \
            "Для того, чтобы отписаться, отправь сообщение 'Отписаться' в чат\n\n" \
            "Доступные команды:\n" \
            "- /start\n" \
            "- /help\n"

TEXT_GREETING = "Привет! Рада видеть тебя в числе интересующихся проектом Антидиетический фитнес клуб ❤ \n\n" \
                "<b><i>Что ждет тебя внутри клуба:</i></b>\n" \
                "- 3 программы тренировок для разного уровня подготовки - для дома и зала\n" \
                "- Комьюнити атлеток, поддерживающих и вдохновляющих друг друга\n\n " \
                "<b><i>Бонусы этого месяца</i></b>  🎁\n" \
                "- 8 дополнительных домашних тренировок в формате “повторяй за мной”\n" \
                "- Лекция “Особенности летнего питания” от нутрициолога "

TEXT_MAIN_FOR_IS_ACTIVE_USER = "В клубе с {first_sub_date}\n" \
                               "Тип подписки: {sub_humanize_name}\n" \
                               "Дата окончания: {unsub_date}\n" \
                               "{sub_date_text}"

TEXT_SPAM_MESSAGE = "Не надо так часто писать, подожди 3 секунды, пожалуйста 🌸"

TEXT_UNKNOWN_MESSAGE = "Я не знаю такой команды 🌼"

# SUBSCRIPTION
TEXT_TARIFFS = "Клуб работает по подписке.\nТы можешь оплатить участие сразу " \
               "на несколько месяцев, или начать с одного.\n" \
               "Подписка продлится автоматически.\n\n" \
               "<b>Тарифы:</b>\n"

TEXT_TARIFFS_DETAIL = "{humanize_name} - {payment_period_name}, <s>{crossed_out_price}</s> {payment_amount} " \
                      "{payment_currency}\n"

TEXT_INVOICE = "Ссылка будет активна в течение часа. Если не успеешь оплатить " \
               "- запроси ее заново, нажав кнопку выбранного тарифа."

TEXT_NOTIFICATION_ONE_DAY_AFTER_UNSUCCESSFUL_PAYMENT = "Привет!\nАнтидиетический фитнес клуб - это не" \
                                                       " только тренировки, " \
                                                       "но и крутое комьюнити девушек. " \
                                                       "Вместе с нами ты полюбишь свое тело, " \
                                                       "станешь увереннее в себе и влюбишься в движение. " \
                                                       "\nГотова присоединиться к самому поддерживающему чату " \
                                                       "в твоей жизни? ♥ "

TEXT_NOTIFICATION_FIVE_DAYS_AFTER_UNSUCCESSFUL_PAYMENT = "Привет! \nКлуб уже вовсю работает! Каждый месяц " \
                                                         "тебя будут ждать новые классные обновления: от марафона " \
                                                         "зарядок до лекций антидиетических экспертов.\n" \
                                                         "Мне хочется создать безопасное фитнес пространство, " \
                                                         "в котором каждая девушка будет чувствовать себя уверенно.\n" \
                                                         "Присоединяйся к тем, кто уже отказался " \
                                                         "от диет и ограничений 💫"

# UNSUBSCRIPTION
TEXT_UNSUBSCRIPTION_START = "Ты уверена, что хочешь отписаться? \n" \
                            "Текущая подписка действует до {unsub_date}.\n" \
                            "{sub_date_text}"

# PAYMENT
TEXT_PAYMENT_INFO = "Оплата на сумму {value} " \
                    "{currency} прошла успешно.\n" \
                    "Оформлена подписка на {sub_period_text}"

TEXT_SUCCESSFUL_PAYMENT = "Спасибо за доверие ❤\nВыбери, с чего хочешь начать!"

TEXT_OUT_OF_TIME_FOR_PAYMENT = "К сожалению, время на оплату вышло. " \
                               "Нажми на выбранный тариф, чтобы запросить ссылку заново 👆"

TEXT_PAYMENT_ERROR = "Упс, что-то пошло не так!\nНе получилось создать твою подписку в клуб." \
                     "Попробуй оплатить через 5-10 минут.\nЕсли все еще не получится - пиши мне в личку @snackiebird1"

TEXT_SUCCESSFUL_AUTO_PAYMENT = "Подписка на {payment_name} фитнеса успешно продлена\n"

TEXT_UNSUCCESSFUL_AUTO_PAYMENT = "Упс, что-то пошло не так!\nМы не смогли продлить твою подписку в клубе. " \
                                 "Возможно, на карте не хватает средств.\nПопробуй продлить подписку самостоятельно 👇"

# Errors
TEXT_UNSUB_ERROR_ADMIN = "Произошла ошибка во время отмены подписки у пользователя: {user_id}"

TEXT_UNSUB_ERROR_USER = "Произошла ошибка во время отменены подписки.\n" \
                        "Пожалуйста, напиши @snackiebird1, я обязательно все исправлю!\n" \
                        "Твой ID: {user_id}"

TEXT_UNBAN_ERROR_ADMIN = "Возникла проблема с выдачей доступа в {bot_name} у пользователя {user_id} "

TEXT_UNBAN_ERROR_USER = "Возникла проблема с доступами к ботам. Пожалуйста, напиши " \
                        "@snackiebird1 для решения вопроса." \
                        "Твой ID: {user_id}"

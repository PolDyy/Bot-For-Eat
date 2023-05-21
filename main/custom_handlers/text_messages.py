from aiogram.types import Message


def get_start_message(message: Message):

    first_name = message.from_user.first_name
    message = f"Привет, {first_name}\nЕсли ты ищешь где вкусно покушать, то ты по адресу!"

    return message


def get_answer_for_text(message: Message):
    if message.text.strip().lower() == 'помощь':
        answer = "У нас есть такой вот функционал...."
    elif message.text.strip().lower() == "оформить заказ":
        answer = "Для оформления заказа нужно нажать соответствующую кнопку"
    else:
        answer = "К сожалению я вас не понял.\n Нажмите на одну из возможных кнопок "
    return answer

from aiogram import types
from aiogram.types.web_app_info import WebAppInfo


class CustomMarkups:

    bt_order = types.KeyboardButton("Оформить заказ", web_app=WebAppInfo(url="https://eshaurma.github.io/app_order/"))
    bt_help = types.KeyboardButton("Помощь")

    @classmethod
    def get_start_markup(cls):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        markup.add(cls.bt_order, cls.bt_help)
        return markup


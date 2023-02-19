from aiogram import types
from aiogram.types import InlineKeyboardMarkup

import google_sheet
from google_sheet import *


# button start(column category)

def get_start():
    categories_ = categories[1:]
    button_set = set(types.InlineKeyboardButton(i, callback_data=f'category{i}') for i in categories_)
    inline_kb1 = InlineKeyboardMarkup(row_width=1)
    inline_kb1.add(*button_set)
    return inline_kb1


new = dict_


def get_button(new):
    button_set = set(types.InlineKeyboardButton(i, callback_data=f'trademark{i}') for i in new.values)
    inline_kb1 = InlineKeyboardMarkup(row_width=1)
    inline_kb1.add(*button_set)
    inline_kb1.add(types.InlineKeyboardButton('Вернуться в главное меню', callback_data='get_start'))
    return inline_kb1

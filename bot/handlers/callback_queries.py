from aiogram import F, types
from ..callback_datas import MainMenuCallback
from aiogram.handlers.callback_query import CallbackQuery
from ..keyboards import inline_keyboards


@router.message(F.text == 'q')
async def main_menu(message: types.Message):
    await message.answer('Hello')


@router.callback_query(MainMenuCallback.filter(F.action == 'ad_placements'))
async def main_menu(query: CallbackQuery, callback_data: MainMenuCallback):
    await query.message.edit_text('''Ваш баланс на текущий момент ниже минимальной суммы для выплаты (1 000 RUB)

В данный момент Вы находитесь в разделе рекламных площадок.

Баланс: 0 RUB''', reply_markup=inline_keyboards.adplacement_kb())

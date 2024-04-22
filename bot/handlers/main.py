from aiogram import Router, F, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from ..callback_datas import MainMenuCallback
from ..keyboards import inline_keyboards
from ..keyboards.inline_keyboards import theme_of_adv
from ..states import Advertisment
from db import advertismentservice as adv_data
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

router = Router()
user_new_adv = {}

'''Callback queries handlers'''


@router.callback_query(MainMenuCallback.filter())
async def main_menu(query: CallbackQuery, callback_data: MainMenuCallback, state: FSMContext):
    user_id = query.from_user.id
    data = await adv_data.get_advertisements_by_user_id(user_id)
    if callback_data.action == 'ad_placements':
        await query.message.edit_text('''Ваш баланс на текущий момент ниже минимальной суммы для выплаты (1 000 RUB)
    
В данный момент Вы находитесь в разделе рекламных площадок.
    
Баланс: 0 RUB''', reply_markup=inline_keyboards.adplacement_kb())
    elif callback_data.action == 'advertisements':
        await query.message.edit_text('''Вы в разделе рекламных объявлений. Здесь можно приобрести показы Ваших объявлений в каналах, подключенных к боту в качестве рекламных площадок.

Ваш баланс: 0 RUB''', reply_markup=inline_keyboards.advirtisement_kb())
    elif callback_data.action == 'new_advertisement':
        await query.message.answer('''Пришлите публичный username Вашего канала в формате @username или t.me/username

Если хотите продвигать бота, пришлите его username''')
        await state.set_state(Advertisment.add_new_advetisment)
    elif callback_data.action == 'my_advertisement':
        if not data:
            await query.message.answer('У вас нет рекламных объявлений')
        else:
            kb = InlineKeyboardBuilder()
            for i in data:
                kb.button(text=f"{i['ad_id']}'", callback_data=f'myadv_{i['ad_id']}')
            kb.button(text='Назад', callback_data='back_to_adv_menu')
            await query.message.edit_text('Ваши рекламные обьявления', reply_markup=kb.as_markup())
    elif callback_data.action == 'do_payment':
        pass
    elif callback_data.action == 'pay_history':
        pass
    elif callback_data.action == 'main_menu':
        await menu(query)
    elif callback_data.action == 'new_placement':
        pass
    elif callback_data.action == 'my_placement':
        pass
    elif callback_data.action == 'deliver_pay':
        pass


@router.callback_query(F.data.startswith('myadv_'))
async def my_adv(query: CallbackQuery):
    adv_id = int(query.data.split('_')[1])
    adv_info = await adv_data.get_advertisement_by_ad_id(adv_id)
    adv_name = adv_info['ad_name']
    adv_text = adv_info['ad_text']
    status = adv_info['status']
    ad_chanel_id = adv_info['ad_chanel_id']
    theme = adv_info['theme']
    shows = adv_info['shows']
    await query.message.edit_text(f'''Вот как выглядит ваша рекламное обьявление
    
{adv_name}
    ''')


@router.callback_query(F.data.in_(theme_of_adv))
async def theme_of_adv(query: CallbackQuery):
    print(query.data)
    user_id = query.from_user.id
    user_new_adv[user_id].append(query.data)
    await query.message.edit_text('Выберите регион', reply_markup=inline_keyboards.region_adv_kb())


@router.callback_query(F.data.in_(['back_to_theme', 'russia']))
async def back_to_theme(query: CallbackQuery):
    if query.data == 'back_to_theme':
        await query.message.edit_text('Выберите тематику', reply_markup=inline_keyboards.theme_of_adv_kb())
    elif query.data == 'russia':
        await query.message.edit_text('''Пришлите цену за 1000 показов (CPM) в валюте RUB

Рекомендуемая цена в Вашей тематике и гео: 103.57 RUB

Если укажете слишком маленькую ставку, то Ваше объявление будет показано с меньшим приоритетом после более дорогих. Не рекомендуем так делать.''',
                                      reply_markup=inline_keyboards.region_adv_kb())


'''State handlers'''


@router.message(Advertisment.add_new_advetisment)
async def add_new_adv(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if message.text.startswith('@') or message.text.startswith('t.me/') or message.text.startswith('https://t.me/'):
        user_new_adv[user_id] = [message.text]
        await message.answer('''
Пришлите видимый текст рекламируемой ссылки (не более 20 символов).

С его помощью можно замаскировать стандартный идентификатор канала в начале объявления. Например “@сhannelName123 - ...” заменить на “Улётные приколы - ...”

Чтобы пропустить этот шаг, пришлите “-”
        ''')
        await state.set_state(Advertisment.add_new_adv_name)
    else:
        await message.answer(
            'Пожалуйста, пришлите публичный username Вашего канала в формате @username или t.me/username')


@router.message(Advertisment.add_new_adv_name)
async def ad_name(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_new_adv[user_id].append(message.text)
    await state.set_state(Advertisment.add_new_adv_text)
    await message.answer('''Пришлите описание Вашего канала в одну строку (без добавления username, только текст).

Максимум 120 символов. Ссылки и эмоджи запрещены. Соблюдайте пунктуацию и орфографию.

Придумайте такое описание, которое заставит людей открыть Ваш канал и подписаться на него.''')


@router.message(Advertisment.add_new_adv_text)
async def adv_text(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_new_adv[user_id].append(message.text)
    await message.answer('Теперь укажите тематику Вашего объявления (можно выбрать только одну)',
                         reply_markup=inline_keyboards.theme_of_adv_kb())


'''Message handlers'''


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await menu(message)


'''Some Func'''


async def menu(message=None, query=None):
    if message:
        await message.answer('''adsmanager_bot предоставляет уникальную возможность для монетизации телеграм каналов за счет размещения автоматических рекламных объявлений под вашими постами.
Доходность от 0.5$ за 1 000 показов. Подайте заявку на вступление в программу и узнайте подробности с помощью кнопки “Рекламные площадки”.

Для размещения рекламного объявления используйте кнопку “Рекламные объявления”. CPM от 0.8$''',
                             reply_markup=inline_keyboards.main_menu_kb())
    else:
        await query.message.edit_text('''adsmanager_bot предоставляет уникальную возможность для монетизации телеграм каналов за счет размещения автоматических рекламных объявлений под вашими постами.
Доходность от 0.5$ за 1 000 показов. Подайте заявку на вступление в программу и узнайте подробности с помощью кнопки “Рекламные площадки”.

Для размещения рекламного объявления используйте кнопку “Рекламные объявления”. CPM от 0.8$''',
                                      reply_markup=inline_keyboards.main_menu_kb())

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from ..callback_datas import MainMenuCallback

theme_of_adv = ['авто и мото', 'авторские блоги', 'бизнес и стартапы',
                'в мире животных', 'видеоигры', 'дети и родители',
                'другое', 'еда и кулинария', 'здоровье и медицина',
                'знаменитости и образ жизни', 'инвестиции', 'иностранные языки',
                'интернет технологии', 'искусство и дизайн', 'история', 'психология и отношения',
                'путешествия и туризм', 'работа и вакансии', 'региональные', 'религия и духовность', 'скидки и акции',
                'спорт',
                'строительство и ремонт',
                'трейдинг', 'фитнес', 'хобби и развлечения', 'экономика и финансы', 'юмор и мемы',
                'кино', 'книги''красота и уход''криптовалюты', 'культура и события', 'любопытные факты',
                'маркетинг и пиар', 'мода и стиль', 'мотивация и саморазвитие',
                'музыка', 'наука и технологии', 'недвижимость', 'новости и сми', 'образование', 'отдых и развлечения']


def theme_of_adv_kb():
    kb = InlineKeyboardBuilder()
    for theme in theme_of_adv:
        kb.add(InlineKeyboardButton(text=theme, callback_data=theme))
    kb.adjust(1)
    return kb.as_markup()


def region_adv_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text='Russia', callback_data='russia')
    kb.button(text='Назад', callback_data='back_to_theme')
    return kb.as_markup()


def main_menu_kb():
    kb = InlineKeyboardBuilder()
    kb.button(
        text='Рекламные площадки', callback_data=MainMenuCallback(action='ad_placements').pack())
    kb.button(text='Рекламные объявления',
              callback_data=MainMenuCallback(action='advertisements').pack(),

              )
    kb.button(
        text='Условия Пользования', url='https://google.com'
    )
    kb.adjust(1)
    return kb.as_markup()


def adplacement_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text='Мои площадки', callback_data=MainMenuCallback(action='my_placement').pack())
    kb.button(text='Новая площадка', callback_data=MainMenuCallback(action='new_placement').pack())
    kb.button(text="Заказать выплату", callback_data=MainMenuCallback(action='deliver_pay').pack())
    kb.button(text='История выплат', callback_data=MainMenuCallback(action='pay_history').pack())
    kb.adjust(4)
    kb.button(text='Узнать подробнее о рекламе', url='https://google.com')
    kb.adjust(1)
    kb.button(text='Назад', callback_data=MainMenuCallback(action='main_menu').pack())
    kb.button(text='Поддержка', url='https://google.com')
    kb.adjust(2)

    return kb.as_markup()


def advirtisement_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text='Рекламное объявления',
              callback_data=MainMenuCallback(action='my_advertisement').pack())
    kb.button(text='Новое объявление', callback_data=MainMenuCallback(action='new_advertisement').pack())
    kb.button(text="Назад", callback_data=MainMenuCallback(action='main_menu').pack())
    kb.button(text='Поддержка', url='https://google.com')
    kb.button(text='Пополнить баланс', callback_data=MainMenuCallback(action='do_payment').pack())
    kb.button(text='Узнать подробнее о рекламе', url='https://google.com')

    # Второй ряд кнопок
    kb.adjust(2)

    return kb.as_markup()


def change_adv_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text='Изменить текст рекламируемой ссылки', callback_data='change_ad_name')
    kb.button(text='Изменить описание', callback_data='change_ad_text')
    kb.button(text='Изменить кол-во показов', callback_data='change_ad_shows')
    kb.button(text='Отключить рекламу', callback_data='off_adv')
    kb.button(text='Удалить рекламу', callback_data='del_adv')
    kb.button(text='Назад', callback_data='back_to_adv')
    kb.adjust(2)
    return kb.as_markup()

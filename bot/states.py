from aiogram.fsm.state import StatesGroup, State


class Advertisment(StatesGroup):
    add_new_advetisment = State()
    add_new_adv_name = State()
    add_new_adv_text = State()
    add_new_adv_cost = State()
    add_new_adv_budjet = State()

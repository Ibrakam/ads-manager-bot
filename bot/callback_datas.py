from aiogram.filters.callback_data import CallbackData


class MainMenuCallback(CallbackData, prefix="main_menu"):
    action: str

class AdPlacementCallback(CallbackData, prefix="ad_placement"):
    ad_id: int
    channel_id: int
    action: str

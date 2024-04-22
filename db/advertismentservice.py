from models import Advirtisment
from db import get_db
from datetime import datetime
import logging
from typing import List, Optional, Dict

from sqlalchemy.exc import SQLAlchemyError


async def add_advertisement(ad_text: str, cost: int, chanel_id: int,
                            advertiser_user_id: int, status: bool, ad_name: Optional[str] = None) -> bool:
    try:
        async with next(get_db()) as session:
            advertisement = Advirtisment(ad_text=ad_text, cost_for_1000=cost, ad_name=ad_name, chanel_id=chanel_id,
                                         advertiser_user_id=advertiser_user_id,
                                         creation_date=datetime.now(), status=status)
            session.add(advertisement)
            session.commit()
            return True
    except SQLAlchemyError as e:

        return False


async def get_advertisement_by_ad_id(ad_id: int) -> Dict | bool:
    try:
        async with next(get_db()) as session:
            advertisement = await session.query(Advirtisment).filter(Advirtisment.ad_id == ad_id).fisrt()
            return advertisement if advertisement else False
    except SQLAlchemyError as e:
        raise e


async def get_advertisements_by_user_id(user_id: int) -> List[Advirtisment] | bool:
    try:
        async with next(get_db()) as session:
            advertisements = await session.query(Advirtisment).filter(
                Advirtisment.advertiser_user_id == user_id
            ).all()
            return advertisements if advertisements else False
    except SQLAlchemyError as e:
        raise e


async def change_advertisment(ad_id, change_info, new_data):
    with next(get_db()) as session:
        advertisement = session.query(Advirtisment).filter(Advirtisment.ad_id == ad_id).first()
        if advertisement:
            if change_info == 'status':
                advertisement.status = new_data
                session.commit()
                return 'Advertisement status changed'
            elif change_info == 'shows':
                advertisement.shows = new_data
                session.commit()
                return 'Advertisement  changed'
            elif change_info == 'cost':
                advertisement.cost_for_1000 = new_data
                session.commit()
                return 'Advertisement  changed'
            elif change_info == 'theme':
                advertisement.theme = new_data
                session.commin()
                return 'Advertisement changed'
            elif change_info == 'ad_name':
                advertisement.ad_name = new_data
                session.commit()
                return 'Advertisement changed'
            elif change_info == 'ad_text':
                advertisement.ad_text = new_data
                session.commit()
                return 'Advertisement text changed'


async def delete_advertisement(ad_id):
    with next(get_db()) as session:
        advertisement = session.query(Advirtisment).filter(Advirtisment.ad_id == ad_id).first()
        if advertisement:
            session.delete(advertisement)
            session.commit()

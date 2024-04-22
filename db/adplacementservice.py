from models import AdPlacements
from db import get_db
from datetime import datetime


async def add_ad_placement(placement_date, ad_id, channel_id):
    with next(get_db()) as session:
        placement = AdPlacements(placement_date=placement_date, ad_id=ad_id, channel_id=channel_id)
        session.add(placement)
        session.commit()


async def delete_ad_placement(placement_id):
    with next(get_db()) as session:
        placement = session.query(AdPlacements).filter(AdPlacements.placement_id == placement_id).first()
        if placement:
            session.delete(placement)
            session.commit()

from models import Channels
from db import get_db
from datetime import datetime


async def add_chanel(admin_id, channel_name, channel_tg_id):
    with next(get_db()) as session:
        channel = Channels(admin_id=admin_id, channel_name=channel_name, channel_tg_id=channel_tg_id,
                           created_at=datetime.now())
        session.add(channel)
        session.commit()


async def get_channel(channel_tg_id, admin_id):
    with next(get_db()) as session:
        channel = session.query(Channels).filter(Channels.channel_tg_id == channel_tg_id and Channels.admin_id == admin_id).first()
        if channel:
            return channel
        return 'Channel not found'



from models import Users
from datetime import datetime
from db import get_db


async def register_user(user_name, first_name, last_name, user_tg_id):
    with next(get_db()) as session:
        user = Users(user_name=user_name, first_name=first_name, last_name=last_name, user_tg_id=user_tg_id,
                     created_at=datetime.now())
        session.add(user)
        session.commit()


async def check_user(user_tg_id):
    with next(get_db()) as session:
        user = session.query(Users).filter(Users.user_tg_id == user_tg_id).first()
        if user:
            return True
        else:
            return False


async def profile_info(user_tg_id):
    with next(get_db()) as session:
        user = session.query(Users).filter(Users.user_tg_id == user_tg_id).first()
        if user:
            return user
        return 'User not found'








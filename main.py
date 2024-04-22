import logging
from bot.handlers.main import router
from fastapi import FastAPI
import uvicorn
from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
import asyncio
from api.api import router as api_router

config_token = dotenv_values(".env")
bot_token = config_token['BOT_TOKEN']

app = FastAPI()
app.include_router(api_router)


async def main():
    bot = Bot(token=bot_token)
    dp = Dispatcher()
    await bot.delete_webhook()

    dp.include_router(router)
    await dp.start_polling(bot)
    await asyncio.Future()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)

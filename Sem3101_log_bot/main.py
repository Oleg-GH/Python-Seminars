# python3 -m venv venv        для Windows     python -m venv venv 
# source venv/bin/activate    для Windows    .\venv\Scripts\activate.bat        
# если PowerShell, то set-executionpolicy RemoteSigned

# t.me/

from aiogram import Bot, Dispatcher, executor, types
from handlers import dp

#total = 150

async def on_start(_):
    print('Bot started')


executor.start_polling(dp, skip_updates=True, on_startup=on_start)

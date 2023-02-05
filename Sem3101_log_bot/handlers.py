from aiogram import types
from create import dp
from aiogram.dispatcher.filters import Text
from random import randint
from keyboards import kb_main_menu
from datetime import datetime
import sweets

game_mode = False   # игра не запущена. Иначе - запущена

@dp.message_handler(commands=['start', 'Start', 'старт', 'Старт' 'go'])
async def mes_start(message: types.Message):
    sweets.total = 150
    sweets.step = 1
    user = message.from_user.full_name
    await message.answer(f'Привет, { user }! Давай сыграем в конфетки!  '
                         'Правила в /rules. Посмотреть список всех команд - ' 
                         'жми /help. Играть - /game. ', reply_markup=kb_main_menu)
    user_log = []
    user_log.append(str(datetime.now())[:-7])       # убрал миллисекунды
    user_log.append(user)
    user_log.append(message.from_user.id)
    user_log.append(message.from_user.username)
    user_log = list(map(str, user_log))
    with open('log.txt', 'a', encoding='UTF-8') as file:
        file.write(' || '.join(user_log) + '\n')


@dp.message_handler(commands=['help', 'Help', 'хелп'])
async def mes_help(message: types.Message):
    await message.answer(f'Список команд:\n/start\n/help\n/rules\n/total\n/set\n/game\n/stop', 
                         reply_markup=kb_main_menu)


@dp.message_handler(commands=['rules', 'Rules', 'правила', 'начать'])
async def mes_rules(message: types.Message):
    await message.answer('По умолчанию на столе есть 150 конфет. (проверить - введи /total). '
                         'Хочешь изменить - введи /set и количество через пробел (н-р, "/set 90"). '
                         'Первый ход определяется случайным образом. '
                         'Ходящий берёт от 1 до 28 шт. за один ход. ' 
                         'Сделавший последний ход выигрывает (забирает все конфеты). ' 
                         'Посмотреть список доступных команд - введи /help, начать игру - /game, '
                         'закончить игру - /stop. ', reply_markup=kb_main_menu)    


@dp.message_handler(commands=['total', 'Total', 'всего'])
async def mes_total(message: types.Message):
    await message.answer(f'По умолчанию на столе в начале игры {sweets.total} конфет. Хочешь '
                         'изменить? Набери /set и количество через пробел (н-р, "/set 90"). '
                         'Начать игру - /game. Список команд - /help. ')


@dp.message_handler(commands=['set', 'Set', 'сет'])
async def mes_settings(message: types.Message):
    global game_mode
    user = message.from_user.full_name
    if game_mode:
        await message.answer(f'{ user }, сначала выйди из игры - введи /stop. ')
    else:
        count = int(message.text.split()[1])
        sweets.total = count
        await message.answer(f'Первоначальное количество конфет установлено - {sweets.total} штук. ')
            

@dp.message_handler(commands=['candies', 'sweets', 'конфеты', 'game', 'Game', 'игра', 'играть'])
async def candies_game( message: types.Message ):
    global game_mode
    if not game_mode:
        game_mode = True 
        await sweets.new_game( message )
    else:
        if not await sweets.player( message ):
            game_mode = False


@dp.message_handler(commands=['stop', 'Stop', 'стоп'] )
async def stop_game( message: types.Message ):
    global game_mode
    user = message.from_user.full_name
    if game_mode:
        game_mode = False
        sweets.total = 150
        sweets.step = 1
        await message.answer( f'{user}, уже уходишь? 😢... Мы всегда тебя ждем. '
                             'Просто введи /start ...😃', reply_markup=kb_main_menu)
        # await mes_start( message )
    else:
        sweets.total = 150
        sweets.step = 1
        await message.answer('Игра окончена. Для новой игры нажми /game, ' 
                             'для всего остального - /start. ', reply_markup=kb_main_menu)    


@dp.message_handler(text=['да пошел ты', 'Да пошел ты', 'тьфу', 'так нечестно', 'лажа', 'сволочь'])
async def mes_curce(message: types.Message):
    await message.answer('Сам такой! Просто играть не умеешь! 😃 ', reply_markup=kb_main_menu)

@dp.message_handler(content_types='location')
async def mes_loc(message: types.Message):
    user_log = []
    user_log.append(str(datetime.now())[:-7])               # убрал миллисекунды
    user_log.append(str(message.from_user.full_name))
    user_log.append('is in point')
    user_log.append(str(message["location"])[1:-1])         # убрал фигурные скобки
    with open('log.txt', 'a', encoding='UTF-8') as file:
        file.write(' || '.join(user_log) + '\n')

@dp.message_handler(content_types='contact')
async def mes_loc(message: types.Message):
    #print(message)
    user_log = []
    user_log.append(str(datetime.now())[:-7])               # убрал миллисекунды
    user_log.append(str(message.from_user.full_name))
    user_log.append('has contact')
    user_log.append(str(message["contact"]["phone_number"]))
    with open('log.txt', 'a', encoding='UTF-8') as file:
        file.write(' || '.join(user_log) + '\n')

@dp.message_handler()
async def mes_rest(message: types.Message):  
    global game_mode
    if game_mode and message.text.isdigit():
        await candies_game(message)
    else:
        await message.answer(f'Не понял твоего {message.text}... '
                             'Попробуй снова или жми /stop и /start! ', reply_markup=kb_main_menu)
      
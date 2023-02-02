from aiogram import types
from create import dp
from aiogram.dispatcher.filters import Text
from random import randint
import sweets


game_mode = False   # игра не запущена. Иначе - запущена

@dp.message_handler(commands=['start', 'старт', 'go'])
async def mes_start(message: types.Message):
    sweets.total = 150
    sweets.step = 1
    user = message.from_user.full_name
    await message.answer(f'Привет, { user }! Давай сыграем в конфетки!  '
                         'Правила в /rules. Посмотреть список всех команд - ' 
                         'набери /help. Играть - /game. ')


@dp.message_handler(commands=['help', 'хелп'])
async def mes_help(message: types.Message):
    await message.answer(f'Список команд:\n/start\n/help\n/rules\n/total\n/set\n/game\n/stop')


@dp.message_handler(commands=['rules', 'правила', 'начать'])
async def mes_rules(message: types.Message):
    await message.answer('По умолчанию на столе есть 150 конфет. (проверить - введи /total). '
                         'Хочешь изменить - введи /set и количество через пробел (н-р, "/set 90"). '
                         'Первый ход определяется случайным образом. '
                         'Ходящий берёт от 1 до 28 шт. за один ход. ' 
                         'Сделавший последний ход выигрывает (забирает все конфеты). ' 
                         'Посмотреть список доступных команд - введи /help, начать игру - /game, '
                         'закончить игру - /stop. ')    


@dp.message_handler(commands=['total', 'всего'])
async def mes_total(message: types.Message):
    await message.answer(f'По умолчанию на столе в начале игры {sweets.total} конфет. Хочешь '
                         'изменить? Набери /set и количество через пробел (н-р, "/set 90"). '
                         'Начать игру - /game. Список команд - /help. ')


@dp.message_handler(commands=['set', 'сет'])
async def mes_settings(message: types.Message):
    global game_mode
    user = message.from_user.full_name
    if game_mode:
        await message.answer(f'{ user }, сначала выйди из игры - введи /stop. ')
    else:
        count = int(message.text.split()[1])
        sweets.total = count
        await message.answer(f'Первоначальное количество конфет установлено - {sweets.total} штук. ')
            

@dp.message_handler(commands=['candies', 'sweets', 'конфеты', 'game', 'игра', 'играть'])
async def candies_game( message: types.Message ):
    global game_mode
    if not game_mode:
        game_mode = True 
        await sweets.new_game( message )
    else:
        if not await sweets.player( message ):
            game_mode = False


@dp.message_handler(commands=['stop', 'стоп'] )
async def stop_game( message: types.Message ):
    global game_mode
    user = message.from_user.full_name
    if game_mode:
        game_mode = False
        sweets.total = 150
        sweets.step = 1
        await message.answer( f'{user}, уже уходишь? 😢... '
                             'Мы всегда тебя ждем. Просто введи /start ...😃')
        # await mes_start( message )
    else:
        sweets.total = 150
        sweets.step = 1
        await message.answer('Игра окончена. Для новой игры нажми /game, ' 
                             'для всего остального - /start. ')    


@dp.message_handler(text=['да пошел ты', 'Да пошел ты', 'тьфу', 'так нечестно', 'лажа', 'сволочь'])
async def mes_curce(message: types.Message):
    await message.answer('Сам такой! Просто играть не умеешь! 😃 ')


@dp.message_handler()
async def mes_rest(message: types.Message):  
    global game_mode
    if game_mode and message.text.isdigit():
        await candies_game(message)
    else:
        await message.answer(f'Не понял твоего {message.text}... '
                             'Попробуй снова или жми /start! ')
      
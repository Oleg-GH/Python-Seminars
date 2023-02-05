from random import choice, randint
from aiogram import types
from asyncio import sleep
from datetime import datetime
from keyboards import kb_main_menu


total = 150         # первоначальное количество конфет по умолчанию
step = 1            # номер хода
taken = ''          # взятое количество конфет в текущем ходе



async def new_game( message: types.Message ) -> int:
    global total, turn, step
    user = message.from_user.full_name
    turn = randint(0, 2)           # очередность. 1 - user, 0 - Бот
    step = 1

    await message.answer( f'{ user }, игра началась...' \
                          f'Для выхода введите  /stop' )
    await message.answer('Определение очередности...')
    await sleep(2)

    if turn == 1:
        await message.answer( f'{ user }, ваш ход. '
                              f'На столе лежит { total } конфет\n' \
                              'Cколько ты возьмешь? ' )
    else:
        await bot( message )


async def player( message: types.Message ):
    global taken, total
    user = message.from_user.full_name
    while True:
        taken = message.text
        if taken.isdigit():
            taken = int( taken )
            if taken > total:
                await message.answer( f'Ты хочешь взять { taken } конфет, '
                                      f'но на столе всего { total } конфет.\n '
                                      f'Возьми не больше {total} конфет, не жадничай 😃' )
                return True
            elif taken < 1 or taken > 28:
                if total > 28: 
                    await message.answer( 'Ты должен взять не менее 1 и не более 28 конфет...' )
                else:
                    await message.answer( 'Надо бы ввести число от 1 до 28. ' )
                return True    
            else:
                break

    if await check_win(message, "player", taken):
        return False

    await message.answer( f'Вы берете { taken } 🍬.\n ' \
                          f'На столе осталось { total } конфет.' )

    if not await bot( message ):
        return False
    return True


async def bot( message: types.Message ):
    global taken, step, total
    user = message.from_user.full_name   
    bot_took = 0
    if step == 1:
        if total > 29:
            if  total - total//29 * 29 == 0:
                bot_took = total - total//29 * 29 + 1
                taken = bot_took
                step += 1
            else:                
                bot_took = total - total//29 * 29
                taken = bot_took
                step += 1
        else:
            bot_took = 29 - taken
            taken = bot_took
            step += 1
    else:
        bot_took = 29 - taken
        taken = bot_took
        step += 1
    if await check_win( message, "Бот", taken ):
        return False
    await message.answer('Ход Бота... Я должен подумать... 🤔')
    await sleep(1)
    await message.answer('Думаю...')
    await sleep(1)
    await message.answer( f'Я забираю { bot_took } 🍬.\n' \
                        f'На столе осталось { total } конфет')
    await message.answer( f'{ user }, сколько конфет возьмешь ты?' )
    return True


async def check_win( message: types.Message, player: str, taken: int ) -> bool:
    global total
    user = message.from_user.full_name
    total -= taken

    if total < 1: 
        if player == "player":
            await message.answer( f'Ты берёшь оставшиеся { taken } конфет.\n' 
                                  f'\nКонфет больше нет! '
                                  f'\n{ user }, поздравляю, ты победил...🤓\n '
                                  f'\nЕще разок? Введи /stop, потом /game. ', 
                                    reply_markup=kb_main_menu)
            total = 150
            step = 1
            user_win = []
            user_win.append(str(datetime.now())[:-7])       # убрал миллисекунды
            user_win.append(user)
            user_win = list(map(str, user_win))
            with open('log.txt', 'a', encoding='UTF-8') as file:
                file.write('  '.join(user_win)+' has won'+'\n')
        else:
            await message.answer( f'Бот забрал последние оставшиеся кофеты. '
                                  f'А значит и твои тоже! Выиграл бот! 😎\n '
                                  f'Как насчет реванша? 🤠 Введи /stop, потом /game. ', 
                                    reply_markup=kb_main_menu)
            total = 150
            step = 1
            user_down = []
            user_down.append(str(datetime.now())[:-7])      # убрал миллисекунды
            user_down.append(message.from_user.full_name)
            user_down = list(map(str, user_down))
            with open('log.txt', 'a', encoding='UTF-8') as file:
                file.write('  '.join(user_down)+' has gone down'+'\n')
        return True
    else:
        return False



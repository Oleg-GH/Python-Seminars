from random import choice, randint
from aiogram import types


total = 150         # первоначальное количество конфет по умолчанию
step = 1            # номер хода
taken = ''          # взятое количество конфет в текущем ходе


async def new_game( message: types.Message ) -> int:
    global total, turn, step
    user = message.from_user.full_name
    turn = randint(0, 2)           # очередность. 1 - user, 0 - Бот

    await message.answer( f'{ user }, игра началась...' \
                          f'Для выхода введите  /stop' )
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
                await message.answer( f'Вы хотите взять { taken } конфет, '
                                      f'но на столе всего { total } конфет.\n '
                                      f'Возьми не больше 28 конфет, не жадничай 😃' )
                return True
            elif taken < 1 or taken > 28:
                if total > 28: 
                    await message.answer( 'Вы должны взять не менее 1 и не более 28 конфет...' )
                else:
                    await message.answer( 'Надо бы ввести число от 1 до 28. ' )
                return True    
            else:
                break

    if await check_win(message, "player", taken):
        return False

    await message.answer( f'Вы берете { taken } конфет.\n ' \
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

    await message.answer( f'Ход Бота. Он забирает { bot_took } 🍬.\n' \
                        f'На столе осталось { total } конфет')
    await message.answer( f'{ user }, сколько конфет возьмете вы?' )
    return True


async def check_win( message: types.Message, player: str, taken: int ) -> bool:
    global total
    user = message.from_user.full_name
    total -= taken

    if total == 0: 
        if player == "player":
            await message.answer( f"Вы берете { taken } конфет\n" 
                                  f"\nКонфет больше нет! "
                                  f"\n{ user }, поздравляю, вы победили...🤓 "
                                  f"\n\nЕще разок? Введи /stop, потом /game")
        else:
            await message.answer( f'Бот забрал последние оставшиеся кофеты. '
                                  f'А значит и ваши тоже! Выиграл бот! 😎\n '
                                  f'Как насчет реванша?:) Введи /stop, потом /game. ')

        return True
    else:
        return False



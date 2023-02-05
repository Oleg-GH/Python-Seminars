from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True)

btn_start = KeyboardButton('/Start')
btn_game = KeyboardButton('/Game')
btn_stop = KeyboardButton('/Stop')
btn_rules = KeyboardButton('/Rules')
btn_help = KeyboardButton('/Help')
btn_location = KeyboardButton('/location', request_location=True)
btn_contact = KeyboardButton('/contact', request_contact=True)


kb_main_menu.add(btn_start, btn_game, btn_stop)
kb_main_menu.add(btn_rules, btn_help)
kb_main_menu.add(btn_location, btn_contact)


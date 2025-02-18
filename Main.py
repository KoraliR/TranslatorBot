import telebot, os
from For_db import add_user, add_counter_repeat
EXE_PATH = os.getcwd()
def start_bot():
	TOKEN_BOT_NAME = "Bot_token.txt"
	bot_token_path = os.path.join(EXE_PATH, TOKEN_BOT_NAME)
	with open(bot_token_path) as f:
		TOKEN = f.read().strip()
	return TOKEN
TOKEN = start_bot()
bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Я бот, который поможет тебе пополнять словарный запас!")
	bot.send_message(message.from_user.id, "Отправь мне незнакомое слово на английском, и я помогу его запомнить!")
	bot.send_message(message.from_user.id, "Но в начале - настройка")
	bot.send_message(message.from_user.id, "Сколько слов в день будем повторять? Отправь число. Рекомендую указывать 20")
	bot.register_next_step_handler(message, set_word_counter)
def set_word_counter(msg):
	if msg.text.strip().isnumeric():
		num = int(msg.text.strip())
		if 1 <= num <= 50:
			ID_usr = add_user(msg.from_user.id, msg.from_user.username, EXE_PATH)
			if ID_usr.split()[0] == "OK" or ID_usr.split()[0] == "ALR":
				add_counter_repeat(int(ID_usr.split()[-1]), num, EXE_PATH, ID_usr.split()[0])

		else:
			bot.reply_to(msg, "Ну столько выучить нельзя!")
			bot.send_message(msg.from_user.id, "Сколько слов в день будем повторять? Отправь число. Рекомендую указывать 20")
			bot.register_next_step_handler(msg, set_word_counter)
	else:
		bot.reply_to(msg, "Введите корректное число цифрами от 1 до 50")
		bot.send_message(msg.from_user.id,
						 "Сколько слов в день будем повторять? Отправь число. Рекомендую указывать 20")
		bot.register_next_step_handler(msg, set_word_counter)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)



bot.infinity_polling()




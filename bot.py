token = '1751941649:AAHUCgdGjAl_SdWyHAj2zu375fmF7QU2toU'
import telebot
import time
import schedule

bot = telebot.TeleBot(token)

def send():
	f = open('result.txt', 'r')
	text = f.read()
	bot.send_message(374690609, text)


bot.polling(none_stop=True)

schedule.every(3).secondss.do(send)

while True:
	schedule.run_pending()
	time.sleep(1)
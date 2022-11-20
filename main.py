token = '1751941649:AAHUCgdGjAl_SdWyHAj2zu375fmF7QU2toU'
from playsound import playsound
import telebot
import schedule
import time
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot(token)

def parsing_l():
        f = open('result.txt','r')
        text_res = f.read()
        f.close()
        bot.send_message(374690609, text_res)
        #bot.send_message(697751699, text_res)
        print('parsed!', time.strftime("%H:%M:%S", time.gmtime()))      

def parsing_s():
        url = 'https://www.ege.spb.ru/result'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        main = soup.find('div', id='w2')
        try:
                subject = main.find_all('div', class_='exam-pub-subj')
        except AttributeError:
                bot.send_message(374690609, 'ERROR')
        condition = main.find_all('div', class_='exam-status')
        con_list = [str(i.text).split()[0] for i in condition]
        sub_list = [i.text for i in subject]
        #получаем количество результатов
        res_in_base = soup.find('div', class_ ='info-board')
        act_number = res_in_base.text.split()[6] + res_in_base.text.split()[7]
        if act_number != '130235':
                playsound('play.mp3')
                warning_n = f'НОВОЕ КОЛИЧЕСТВО РЕЗУЛЬТАТОВ - {act_number}'
                bot.send_message(374690609, warning_n)
        #for i in range(len(con_list)):
        #       print(sub_list[i], '\t', con_list[i])
        f = open('result.txt', 'w+')
        for i in range(23, len(con_list)):
                line = sub_list[i] + '\t' + con_list[i] + '\n'
                f.write(line)
        f.close()
        f = open('result.txt', 'r')
        for line in f:
                if not ('Обработка' in list(line.split())):
                        if not '(ГВЭ-1)' in list(line.split()):
                                print(line)
                                subj = line.split()[0]
                                playsound('play.mp3')
                                warning = f'ДАННЫЕ ПО {subj} ОБНОВИЛИСЬ'
                                bot.send_message(374690609, warning)
        f.close()

schedule.every(8).seconds.do(parsing_s)
schedule.every(10).minutes.do(parsing_l)

while True:
        schedule.run_pending()
        time.sleep(1)

bot.polling(none_stop=True)

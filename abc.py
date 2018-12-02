# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 08:48:00 2018

@author: Admin
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('C:/Users/Admin/du/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data = open('C:/Users/Admin/du/chatterbot-corpus-master/chatterbot_corpus/data/english/' + files, 'r').readlines()
    bot.train(data)
while True:
    message = input('You:')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print('ChatBot:', reply)
    if message.strip() == 'Bye' :
        print('ChatBot: Bye')
        break
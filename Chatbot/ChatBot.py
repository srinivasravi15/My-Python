from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('My Bot')
bot.set_trainer(ListTrainer)

#for files in os.listdir('C:/Users/Harini Ravi\Desktop\My Python\Python Data\chatterbot-corpus-master\chatterbot_corpus\data\english/'):	
#	data = open('C:/Users/Harini Ravi\Desktop\My Python\Python Data\chatterbot-corpus-master\chatterbot_corpus\data\english/'+files,'r').readlines()
#	bot.train(data)

while True:
	message = input('You:')
	if message.strip()!= 'Bye' or message.strip()!= 'bye':
		reply = bot.get_response(message)
		print('My Bot:', reply)
	if message.strip()== 'Bye' or message.strip()== 'bye':
		print('My Bot: Bye')
		break
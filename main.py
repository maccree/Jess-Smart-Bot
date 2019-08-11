#imports and sertting
import token_for_bot
import token_for_dialogflow
import json
import apiai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token=token_for_bot) # token API  Telegram
dispatcher = updater.dispatche


# comends ob
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hi')

ef textMessage(bot, update):
    request = apiai.ApiAI(token_for_dialogflow).text_request() # Dialogflow API Token
    request.lang = 'ru' # In what language will the request be sent
    request.session_id = 'BatlabAIBot' # Dialog Session ID (you need to learn the bot later)
    request.query = update.message.text # We send a request to the AI with a message from the user

    #Handlers
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)



# HAndlers on Disp
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)


updater.start_polling(clean=True)
updater.idle()

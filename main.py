#imports and sertting
import token_for_bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token=token_for_bot) # token API  Telegram
dispatcher = updater.dispatche


# comends ob
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hi')
def textMessage(bot, update):
    response = 'Ur message: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)


    #Handlers
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

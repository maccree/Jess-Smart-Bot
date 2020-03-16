#imports and sertting
import token_for_bot
import token_for_dialogflow
import json
import apiai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters



updater = Updater('<ur telegram token>', use_context= True) # token API  Telegram
dispatcher = updater.dispatche


# comends ob
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hi')

def textMessage(bot, update):

    request = apiai.ApiAI('<ur Dialogflow Token>').text_request()                      # Dialogflow API Token

    request.lang = 'ru'                                                             # In what language will the request be sent
    request.session_id = 'BatlabAIBot'                                              # Dialog Session ID (you need to learn the bot later)
    request.query = update.message.text                                             # We send a request to the "AI" with a message from the user
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']                      # Parse JSON and pull out the answer
                                                                                    # If there is an answer from the bot - send it to the user, if not - the bot did not understand it
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='I do not quite understand you!')

    #Handlers
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)



# HAndlers on Disp
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)


updater.start_polling(clean=True)
updater.idle()

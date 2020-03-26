import jess_logo

#Settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json

print(jess_logo)

updater = Updater(token='<YOUR TOKEN HERE>')      # API token to Telegram
dispatcher = updater.dispatcher

# Command processing
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello!')
def textMessage(bot, update):
    request = apiai.ApiAI('<YOUR TOKEN HERE>').text_request()
    request.lang = 'ru'                                                     # What language will the request be sent in
    request.session_id = 'BatlabAIBot'                                      # ID of the dialog Session (you need to teach the bot later)
    request.query = update.message.text                                     # Sending a request to the AI with a message from the user
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']              # Parsing the JSON and pulling out the response
# If there is a response from the bot-send it to the user, if not-the bot did not understand it
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Error')

        # Handlers
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Adding handlers to the dispatcher
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Starting the search for updates
updater.start_polling(clean=True)
updater.idle()

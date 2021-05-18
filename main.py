import constants as key
import responses as r
from telegram import *
from telegram.ext import *

bot = Bot(key.API_TOKEN)
print(bot.get_me())
print("Bot started...")

def start_command(update, context):
    update.message.reply_text("Type something random to get started!")

def help_command(update, context):
    update.message.reply_text("I can't help you, try Google.")

def command_command(update, context):
    first_chat_name = update['message']['chat']['first_name']
    update.message.reply_text(
        f"Good day, {first_chat_name}! Below is the list of commands to operate me.\n"\
        "<b>- /start\n- /help\n- /command </b>", parse_mode='HTML')

def google_command(update, context):
    text = str(update.message.text).lower()
    word = text.split()
    if len(word) < 2 or word[0] != "google":
        return False
    else: 
        def google_search():
            pass                #Work in progress...
        return google_search(word[1])
    

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = r.response(text)
    first_chat_name = update['message']['chat']['first_name']
    if response==False:
        return update.message.reply_text("Not a valid command.\nTry <b>/command</b>", parse_mode='HTML')
    elif 'Hello' in response:
        return update.message.reply_text(response + ', ' + first_chat_name + '?', reply_to_message_id=update['message']['message_id'])
    
    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error: {context.error}")

def main():
    updater = Updater(key.API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("command", command_command))
    dispatcher.add_handler(PrefixHandler('/', 'google', google_command))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    dispatcher.add_error_handler(error)

    updater.start_polling() #checking_rate
    updater.idle()

main()

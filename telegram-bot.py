import keys
import telegram
import requests
import json

bot = telegram.Bot(token=keys.tg_token)

from telegram.ext import CommandHandler , ApplicationBuilder #, Filters

updater = ApplicationBuilder().token(keys.tg_token).build() #Replace TOKEN with your token string



async def hello(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')

async def summary(update, context):
    response = requests.get('https://random.dog/woof.json')
    if(response.status_code==200): #Everything went okay, we have the data
        data = response.json()
        
        await context.bot.send_message(chat_id=update.effective_chat.id, text=data['url'])
    else: #something went wrong
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Error, something went wrong.")


hello_handler = CommandHandler('hello', hello)
updater.add_handler(hello_handler)

corona_summary_handler = CommandHandler('summary', summary)
updater.add_handler(corona_summary_handler)

updater.run_polling()



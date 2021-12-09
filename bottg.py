import requests

response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lang=uk&q=Kyiv&appid=890791bd4ab58d35f26f55f4b87b563a")
if response.status_code != 200:
    raise ConnectionError(response.status_code)
rawData = response.json()
test = f"🤓У Києві сьогодні {rawData['weather'][0]['description']}🤓\n 🌡Температура {rawData['main']['temp']} градусів по Цельсію🌡\n 🔥Гарного Вам дня!🔥"
from telegram.ext import Updater, CommandHandler
print("Бот запущен. Нажмите Ctrl+C для завершения")
def on_start(update, context):
	chat = update.effective_chat
	context.bot.send_message(chat_id=chat.id, text=test)
token = "5037909929:AAE2G1IOyxUMFcZVLxg1ojMnvUAAAA-P4O4"
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))
updater.start_polling()
updater.idle()

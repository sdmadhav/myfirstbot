from telegram.ext import Updater, CommandHandler, MessageHandler,Filters

Token="1431989781:AAGo5JKThqlQV7Lm1QJfboDB_eJdKFcMa6s"


def start(update,context):
        update.message.reply_text("Hello! Welcome to my channel.")


def help(update,context):
        update.message.reply_text("Not implemented anything yet.")



updater = Updater(Token, use_context=True)

d = updater.dispatcher

# Handlers
d.add_handler(CommandHandler("start", start))
d.add_handler(CommandHandler("help", help))

# Start the bot
updater.start_polling()

# Keep it active untile CTRL + C
updater.idle()
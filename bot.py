from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

TOKEN = os.environ.get("8294613978:AAHMD-eZgExDPB2I63wcOTbpJr5iG8xY3Dw")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Use /download to get the file")

def download(update: Update, context: CallbackContext):
    with open("example.pdf", "rb") as f:
        update.message.reply_document(
            document=f,
            filename="example.pdf"
        )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("download", download))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

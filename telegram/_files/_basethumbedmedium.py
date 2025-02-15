from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

class Photo(_BaseThumbedMedium):
    """Represents a photo file in Telegram."""

    def __init__(self, file_id, file_unique_id, file_size=None, thumbnail=None):
        super().__init__(file_id, file_unique_id, file_size, thumbnail)

def handle_photo(update: Update, context: CallbackContext):
    photo = update.message.photo[-1]  # En yüksek çözünürlüklü fotoğrafı al
    photo_obj = Photo(
        file_id=photo.file_id,
        file_unique_id=photo.file_unique_id,
        file_size=photo.file_size,
        thumbnail=photo.get_thumbnail()
    )
    update.message.reply_text(f"Fotoğraf alındı: {photo_obj}")

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Merhaba! Bir fotoğraf gönderin ve onu yöneteceğim.')

def main():
    TOKEN = "5275c451994438b1184dd395b36fc8ae61369037"
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, handle_photo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
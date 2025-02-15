from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

class Contact(TelegramObject):
    """Represents a phone contact."""
    
    def __init__(self, phone_number, first_name, last_name=None, user_id=None, vcard=None):
        super().__init__()
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard

def handle_contact(update: Update, context: CallbackContext):
    contact = update.message.contact
    contact_obj = Contact(
        phone_number=contact.phone_number,
        first_name=contact.first_name,
        last_name=contact.last_name,
        user_id=contact.user_id,
        vcard=contact.vcard
    )
    update.message.reply_text(f"Kişi alındı: {contact_obj.first_name} {contact_obj.last_name or ''}")

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Merhaba! Bir kişi gönderin ve bilgilerini alacağım.')

def main():
    # Buraya kendi token'ınızı ekleyin
    TOKEN = "7784466023:AAHV5exN22Ply1jeskJ9ffZ7b3WsHWIiCPE"
    
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.contact, handle_contact))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from typing import Optional

# _BaseMedium sınıfı tanımı
class _BaseMedium:
    """Base class for objects representing various media file types."""

    __slots__ = ("file_id", "file_unique_id", "file_size")

    def __init__(self, file_id: str, file_unique_id: str, file_size: Optional[int] = None):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.file_size: Optional[int] = file_size

    def __str__(self):
        return f"BaseMedium(file_id={self.file_id}, file_unique_id={self.file_unique_id}, file_size={self.file_size})"

# Document sınıfı tanımı
class Document(_BaseMedium):
    """This object represents a general file."""

    __slots__ = ("file_name", "mime_type", "thumbnail")

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None,
        thumbnail: Optional[object] = None,
    ):
        super().__init__(file_id, file_unique_id, file_size)
        self.file_name: Optional[str] = file_name
        self.mime_type: Optional[str] = mime_type
        self.thumbnail: Optional[object] = thumbnail

    def __str__(self):
        return (f"Document(file_id={self.file_id}, file_unique_id={self.file_unique_id}, "
                f"file_name={self.file_name}, mime_type={self.mime_type}, file_size={self.file_size})")

# Bot komutları
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Merhaba! Bir belge gönderin ve onu yöneteceğim.')

def handle_document(update: Update, context: CallbackContext):
    document = update.message.document
    doc_obj = Document(
        file_id=document.file_id,
        file_unique_id=document.file_unique_id,
        file_name=document.file_name,
        mime_type=document.mime_type,
        file_size=document.file_size
    )
    update.message.reply_text(f"Belge alındı: {doc_obj}")

def main():
    # Sağladığınız token'ı buraya ekliyorum
    TOKEN = "7784466023:AAHV5exN22Ply1jeskJ9ffZ7b3WsHWIiCPE"
    
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.document, handle_document))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
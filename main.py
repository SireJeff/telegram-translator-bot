from telegram.ext import Updater, MessageHandler, Filters
from google.cloud import translate_v2 as translate

# Replace with your Telegram Bot token
TOKEN = 'your_telegram_bot_token'

# Replace with your Google Cloud API key
translate_client = translate.Client.from_service_account_json('path_to_your_service_account_file.json')

# Function to handle incoming messages
def translate_message(update, context):
    message = update.message
    text = message.text

    # Detect the language of the message
    detection = translate_client.detect_language(text)

    # Translate to Persian if the language is English
    if detection['language'] == 'en':
        translation = translate_client.translate(text, target_language='fa')
        translated_text = translation['translatedText']
        reply_text = f"Original (English):\n{text}\n\nTranslation (Persian):\n{translated_text}"
        message.reply_text(reply_text)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Handle messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_message))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

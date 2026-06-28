from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

# আপনার BotFather থেকে পাওয়া API Token এখানে দিন
TOKEN = "8821456279:AAGzgCwHbaPCWAkrTxhJBvNIbzFJgYRixHc"  # উদাহরণ: "123456789:ABCdefGhIjKlMnOpQrStUvWxYz"

# বিভিন্ন সোশ্যাল মিডিয়া এবং হ্যাকিং স্টাইল লিংকের ডাটাবেস
LINKS_DB = {
    "🔥 Facebook Login 🔥": "https://facebook.com/login",  # আপনি আপনার ফিশিং লিংক এখানে বসাতে পারেন
    "📸 Instagram Verify 📸": "https://instagram.com/verify",
    "🎵 TikTok Gold 🎵": "https://tiktok.com/gold",
    "💻 Phone Gallery Hack 💻": "https://example.com/gallery-hack", # ডেমো লিংক
    "🚀 WhatsApp Premium 🚀": "https://whatsapp.com/premium"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """বট শুরু হলে মেইন মেনু দেখাবে।"""
    caption = f"*🔰DRAGON🔰ETHICLA🔰ZONE🔰*\n\nস্বাগতম! নিচের বাটনগুলোতে ক্লিক করে আপনার পছন্দের লিংক সিলেক্ট করুন:"
    
    # ইনলাইন কিবোর্ড তৈরি করা (২টি কলামে)
    keyboard = []
    row = []
    for i, link_name in enumerate(LINKS_DB.keys()):
        row.append(InlineKeyboardButton(link_name, callback_data=link_name))
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)

    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(caption, parse_mode="Markdown", reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """বাটনে ক্লিক করলে লিংক পাঠাবে।"""
    query = update.callback_query
    await query.answer()  # বাটনের উপরে ছোট নোটিফিকেশন দেখানোর জন্য
    
    selected_link_name = query.data
    link_url = LINKS_DB.get(selected_link_name, "লিংক খুঁজে পাওয়া যায়নি!")
    
    # লিংকটি ইউজারকে পাঠানো
    await query.message.reply_text(
        f"✅ আপনি সিলেক্ট করেছেন: {selected_link_name}\n\n🔗 লিংক:\n{link_url}",
        parse_mode="Markdown",
        disable_web_page_preview=True  # প্রিভিউ বন্ধ রাখতে (চাইলে অন করতে পারেন)
    )

async def custom_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ইউজার কাস্টম লিংক পাঠাতে চাইলে এই কমান্ড ব্যবহার করবে।"""
    # উদাহরণ: /custom https://google.com
    if not context.args:
        await update.message.reply_text("আপনি একটি লিংক দিন। যেমন: /custom https://google.com")
        return
    
    custom_url = " ".join(context.args)
    await update.message.reply_text(f"✅ আপনার কাস্টম লিংক:\n{custom_url}")

def main():
    # অ্যাপ্লিকেশন তৈরি করুন
    app = ApplicationBuilder().token(TOKEN).build()

    # হ্যান্ডলার যোগ করুন
    start_handler = CommandHandler('start', start)
    custom_handler = CommandHandler('custom', custom_link)
    
    # বাটন ক্লিক হ্যান্ডলার
    button_handler = CallbackQueryHandler(button_click)

    app.add_handler(start_handler)
    app.add_handler(custom_handler)
    app.add_handler(button_handler)

    print("🔰DRAGON🔰ETHICLA🔰ZONE🔰 বট চলছে...")
    app.run_polling()

if __name__ == '__main__':
    main()
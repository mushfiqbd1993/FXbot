import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

MAIN_BOT_TOKEN = '7942457053:AAH9AcUk5PhaD2T-cwn7mOHissr2vzWGndw'
bot = telebot.TeleBot(MAIN_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    markup = InlineKeyboardMarkup(row_width=3)
    markup.add(
        InlineKeyboardButton("🚀 Get Started", url="https://www.marketvox.com"),
        InlineKeyboardButton("🌟 Watch Videos", url="https://t.me/+OiMzr4wH6jVlMDc1"),  # Change to actual VIP group
        InlineKeyboardButton("❓ Help", url="https://t.me/fxtradifysupport_bot")
    )
    
    bot.send_message(message.chat.id,
        """📌 Welcome to FxTradify Premium Signals!

This isn’t your average signal group.
We drop real, high-converting trades — not spammy gold BS.
Truth is, a lot of “gurus” copy our trades.

📩 Message @@fxtradify_bot and press Start to begin.

💰 How It Works:
We partner with trusted brokers — they pay us, so you get everything FREE. You just need to fund your account . Withdraw at any time.

✅ Choose your funding tier — all include VIP access:

$350 – Standard start

$500 – Recommended for most

$1,000+ – Go bigger, trade smarter

🔒 The higher your deposit, the larger positions you can take while staying within proper risk management.

👉 Open your account now:
https://client.marketsvox.com/en/home

⚠️ Risk management is YOUR responsibility.
We are not liable for losses. Trade smart.

🤖 Want hands-free trading?
DM “copy trader” to activate our fully automated account run by a top trader.

Let’s run it up 📈🔥

📩 Send your screenshot here: @fxtradifysupport_bot
""", reply_markup=markup)

print("✅ Main Bot is running...")
bot.infinity_polling()

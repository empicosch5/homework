import telebot
import os
import random

# Инициализация бота с использованием его токена
bot = telebot.TeleBot("")

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['mem'])
def send_mem(message):
    if not os.path.exists('images'):
        bot.reply_to(message, "The 'images' folder does not exist.")
        return
    images = os.listdir('images')
    
    if "duck.jpg" in images and random.randint(1, 3000) == 1:
        img_name = "duck.jpg"
    else:
        
        other_images = [img for img in images if img != "duck.jpg"]
        if not other_images:
            img_name = "duck.jpg"  
        else:
            img_name = random.choice(other_images)
    with open(f'images/{img_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f)

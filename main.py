import os 
import telebot
import schedule
from time import sleep
from PIL import Image
import glob
import random
from threading import Thread

# API_KEY = os.getenv("API_KEY")
API_KEY = "5260897066:AAEbgXzHylDISIUJidFmeVBo804Gq7TaNZ8"
bot = telebot.TeleBot(API_KEY)
USER_ID = None

@bot.message_handler(commands=["help"])
def greet(message):
    bot.reply_to(message, "Hey! Added your ... to queue")

@bot.message_handler(commands=["start"])
def start(message):
    USER_ID = message.from_user.id
    bot.send_message(USER_ID, "Я буду присылать красивые букеты каждый день")
    
# @bot.message_handler(func=flower_request)
# def send_flower(message):
#     request = message.text.split()
#     bot.send_photo

@bot.message_handler(commands=['settings', 'setting', 'set', 'настройки'])
def settings(message):
    pass

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

def get_flowers(n=1):
    img_paths = "U:\Coding\Generator\content\images_out\TimeToDiscoLocally-1"
    image_list = []
    for filename in glob.glob(f"{img_paths}/*.png"):
        im = Image.open(filename)
        image_list.append(im)
    rand_images = random.choices(image_list, k=n)
    return rand_images

@bot.message_handler(commands=["flower"])
def send_flowers(message):

    for image in get_flowers():
        bot.send_photo(message.from_user.id, image)

if __name__ == "__main__":
    Thread(target=bot.infinity_polling, name='bot_infinity_polling', daemon=True).start()
    while True:
        schedule.run_pending()
        sleep(1)
    # Create the job to schedule
    # send_flowers()

    # Spin up a threa to run the schedule check so it doesn't block your bot
    # This will take the function schedule_checker which will check every second
    # to see if the scheduled hob needs to be ran

    # Thread(target=schedule_checker).start()
    # bot.polling()
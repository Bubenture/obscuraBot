import telebot
import requests
from PIL import Image
from io import BytesIO

bot = telebot.TeleBot(TOKEN)

latest_images = []

@bot.message_handler(content_types=['photo'])
def handle_message(message):
    global latest_images
    
    photo = message.photo[-1]  

    latest_images.append(bot.get_file(photo.file_id))

    if len(latest_images) == 2:
        combined_image = combine_images()

        bio = BytesIO()
        combined_image.save(bio, format='JPEG')
        bio.seek(0)
        bot.send_photo(message.chat.id, bio)

        latest_images.clear()

def combine_images():
    images = [download_image(file_info) for file_info in latest_images]

    images = [Image.open(BytesIO(image)) for image in images]

    widths, heights = zip(*(image.size for image in images))

    new_width = sum(widths)
    new_height = max(heights)

    new_image = Image.new("RGB", (new_width, new_height))

    x_offset = 0
    for image in images:
        new_image.paste(image, (x_offset, 0))
        x_offset += image.width

    return new_image

def download_image(file_info):
    url = f"https://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}"
    response = requests.get(url)
    return response.content

bot.polling()

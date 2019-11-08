import os
from PIL import Image
from dotenv import load_dotenv
from instabot import Bot
from os import listdir

DIRECTORY_WITH_IMAGES = 'images'
CROPPED_IMAGES_PREHEADER = 'cropped_'


def crop_images(directory):
    files = os.listdir(directory)
    for file in files:        
        image = Image.open("{}/{}".format(directory, file))
        if image.width > image.height:
            cropping_size = (image.width - image.height) / 2
            coordinates = (cropping_size, 0, image.height + cropping_size, image.height)
        else:
            cropping_size = (image.height - image.width) / 2
            coordinates = (0, cropping_size, image.width, image.width + cropping_size)
        cropped = image.crop(coordinates)
        cropped.save("{}/cropped_{}".format(directory, file))


def send_images_to_instagram(directory):
    bot = Bot()
    bot.login(username=os.environ['INSTAGRAM_LOGIN'], password=os.environ['INSTAGRAM_PASSWORD'])
    files = os.listdir(directory)
    only_cropped_images = filter(lambda x: x.startswith(CROPPED_IMAGES_PREHEADER), files)
    for i in only_cropped_images:
        bot.upload_photo("{}/{}".format(directory, i))
    bot.logout()


if __name__ == '__main__':
    load_dotenv()
    crop_images(DIRECTORY_WITH_IMAGES)
    send_images_to_instagram(DIRECTORY_WITH_IMAGES)

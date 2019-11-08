import requests
import os
import json
import urllib3
from PIL import Image
from dotenv import load_dotenv
from instabot import Bot
from os import listdir

DIRECTORY = 'images'
SPACEX_TEMPLATE = 'spacex'
SPACEX_URL = 'https://api.spacexdata.com/v3/launches/latest'
HUBBLE_URL = 'http://hubblesite.org/api/v3/'
HUBBLE_COLLECTION_NAME = 'wallpaper'


def get_spacex_images_urls(url):
    response = requests.request('GET', url)
    data = response.text
    dict = json.loads(data)
    links_data = dict['links']['flickr_images']
    links_list = []
    for link in links_data:
        links_list.append(link)
    return links_list


def get_hubble_image_url(url):
    response = requests.request('GET', url)
    data = response.text
    massiv = json.loads(data)
    links_data = massiv['image_files']
    links_list = []
    for link in links_data:
        link = "{}{}".format("https:", link['file_url'])
        links_list.append(link)
    return links_list[-1]


def get_hubble_images_ids(collection_name):
    url = "{}{}{}".format(HUBBLE_URL, 'images/', collection_name)
    response = requests.request('GET', url)
    data = response.text
    massiv = json.loads(data)
    ids_list = []
    for item in massiv:
        d = dict(item)
        image_id = d['id']
        ids_list.append(image_id)
    return ids_list


def get_image_type(url):
    string = url.split('.')
    return string[-1]


def download_spacex_image(image_url, image_file):
    response = requests.get(image_url)
    response.raise_for_status()
    filename = "{}/{}".format(DIRECTORY, image_file)
    if not os.path.exists(os.path.dirname(filename)):
        dir_name = os.path.dirname(filename)
        os.makedirs(dir_name)
    with open(filename, 'wb') as file:
        file.write(response.content)


def download_hubble_image(image_id):
    url = "{}{}{}".format(HUBBLE_URL, 'image/', image_id)
    response = requests.get(get_hubble_image_url(url), verify=False)
    image_url = response.url
    response.raise_for_status()
    filename = "{}/{}.{}".format(DIRECTORY, image_id, get_image_type(image_url))
    if not os.path.exists(os.path.dirname(filename)):
        dir_name = os.path.dirname(filename)
        os.makedirs(dir_name)
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(url):
    for image_number, image_url in enumerate(get_spacex_images_urls(url), start=1):
        image_file = "{}{}.jpg".format(SPACEX_TEMPLATE, image_number)
        download_spacex_image(image_url, image_file)


def fetch_hubble_collection(collection_name):
    for image_id in get_hubble_images_ids(collection_name):
        download_hubble_image(image_id)


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
    load_dotenv()
    bot = Bot()
    bot.login(username=os.environ['INSTAGRAM_LOGIN'], password=os.environ['INSTAGRAM_PASSWORD'])
    files = os.listdir(directory)
    only_cropped_images = filter(lambda x: x.startswith('cropped_'), files)
    for i in only_cropped_images:
        bot.upload_photo("{}/{}".format(directory, i))
    bot.logout()


if __name__ == '__main__':
    urllib3.disable_warnings()
    fetch_spacex_last_launch(SPACEX_URL)
    fetch_hubble_collection(HUBBLE_COLLECTION_NAME)
    crop_images(DIRECTORY)
    send_images_to_instagram(DIRECTORY)

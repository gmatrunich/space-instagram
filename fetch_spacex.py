import requests
import os
import json

DIRECTORY = 'images'
SPACEX_TEMPLATE = 'spacex'
SPACEX_URL = 'https://api.spacexdata.com/v3/launches/latest'


def get_spacex_images_urls(url):
    response = requests.request('GET', url)
    #data = response.text
    data = json.loads(response.text)
    links_data = data['links']['flickr_images']
    links_list = []
    for link in links_data:
        links_list.append(link)
    return links_list


def download_spacex_image(image_url, image_file):
    response = requests.get(image_url)
    response.raise_for_status()
    filename = "{}/{}".format(DIRECTORY, image_file)
    if not os.path.exists(os.path.dirname(filename)):
        dir_name = os.path.dirname(filename)
        os.makedirs(dir_name)
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(url):
    for image_number, image_url in enumerate(get_spacex_images_urls(url), start=1):
        image_file = "{}{}.jpg".format(SPACEX_TEMPLATE, image_number)
        download_spacex_image(image_url, image_file)


if __name__ == '__main__':
    fetch_spacex_last_launch(SPACEX_URL)

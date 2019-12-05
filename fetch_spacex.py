import requests
import os

SPACEX_URL = 'https://api.spacexdata.com/v3/launches/latest'
DIRECTORY_TO_SAVE_IMAGES = 'images'
SPACEX_FILENAME_TEMPLATE = 'spacex'


def get_spacex_images_urls(url):
    response = requests.request('GET', url)
    data = response.json()
    links_data = data['links']['flickr_images']
    links = []
    for link in links_data:
        links.append(link)
    return links


def download_spacex_image(image_url, image_file):
    response = requests.get(image_url)
    response.raise_for_status()
    filename = os.path.join(DIRECTORY_TO_SAVE_IMAGES, image_file)
    if not os.path.exists(DIRECTORY_TO_SAVE_IMAGES):
        os.makedirs(DIRECTORY_TO_SAVE_IMAGES)
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(url):
    for image_number, image_url in enumerate(get_spacex_images_urls(url), start=1):
        image_file = "{}{}.jpg".format(SPACEX_FILENAME_TEMPLATE, image_number)
        download_spacex_image(image_url, image_file)


if __name__ == '__main__':
    fetch_spacex_last_launch(SPACEX_URL)

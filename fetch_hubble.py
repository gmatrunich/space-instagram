import requests
import os
import urllib3

DIRECTORY_TO_SAVE_IMAGES = 'images'
HUBBLE_URL = 'http://hubblesite.org/api/v3/'
HUBBLE_COLLECTION_NAME = 'wallpaper'


def get_hubble_image_url(url):
    response = requests.request('GET', url)
    data = response.json()
    links_data = data['image_files']
    links = []
    for link in links_data:
        link = "{}{}".format("https:", link['file_url'])
        links.append(link)
    return links[-1]


def get_hubble_images_ids(collection_name):
    url = "{}{}{}".format(HUBBLE_URL, 'images/', collection_name)
    response = requests.request('GET', url)
    collection_info = response.json()
    ids_list = []
    for image in collection_info:
        image_info = dict(image)
        image_id = image_info['id']
        ids_list.append(image_id)
    return ids_list


def download_hubble_image(image_id):
    url = "{}{}{}".format(HUBBLE_URL, 'image/', image_id)
    response = requests.get(get_hubble_image_url(url), verify=False)
    image_url = response.url
    image_type = list(os.path.splitext(image_url))
    response.raise_for_status()
    filename = os.path.join(DIRECTORY_TO_SAVE_IMAGES, "{}{}".format(image_id, image_type[-1]))
    if not os.path.exists(DIRECTORY_TO_SAVE_IMAGES):
        os.makedirs(DIRECTORY_TO_SAVE_IMAGES)
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_hubble_collection(collection_name):
    for image_id in get_hubble_images_ids(collection_name):
        download_hubble_image(image_id)


if __name__ == '__main__':
    urllib3.disable_warnings()
    fetch_hubble_collection(HUBBLE_COLLECTION_NAME)

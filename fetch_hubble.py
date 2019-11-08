import requests
import os
import json
import urllib3

DIRECTORY = 'images'
HUBBLE_URL = 'http://hubblesite.org/api/v3/'
HUBBLE_COLLECTION_NAME = 'wallpaper'


def get_hubble_image_url(url):
    response = requests.request('GET', url)
    #data = response.text
    data = json.loads(response.text)
    links_data = data['image_files']
    links_list = []
    for link in links_data:
        link = "{}{}".format("https:", link['file_url'])
        links_list.append(link)
    return links_list[-1]


def get_hubble_images_ids(collection_name):
    url = "{}{}{}".format(HUBBLE_URL, 'images/', collection_name)
    response = requests.request('GET', url)
    #data = response.text
    data = json.loads(response.text)
    ids_list = []
    for item in data:
        d = dict(item)
        image_id = d['id']
        ids_list.append(image_id)
    return ids_list


def get_image_type(url):
    string = url.split('.')
    return string[-1]


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


def fetch_hubble_collection(collection_name):
    for image_id in get_hubble_images_ids(collection_name):
        download_hubble_image(image_id)


if __name__ == '__main__':
    urllib3.disable_warnings()
    fetch_hubble_collection(HUBBLE_COLLECTION_NAME)
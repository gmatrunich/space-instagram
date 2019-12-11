import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv


DIRECTORY_TO_SAVE_IMAGES = 'images'
NASA_APOD_URL = 'https://api.nasa.gov/planetary/apod' # Astronomy Picture of the Day
NUMBER_OF_DAYS = 7
NASA_FILENAME_TEMPLATE = 'nasa'


def get_nasa_image_url(token, entry_url, image_date):
    payload = {
                'api_key': token, 
                'date': image_date
    }
    response = requests.get(entry_url, params=payload)
    response.raise_for_status()
    image_data = response.json()
    if not image_data['media_type'] == 'video':
        return image_data['url']


def download_nasa_image(image_url, image_file):
    response = requests.get(image_url)
    response.raise_for_status()
    filename = os.path.join(DIRECTORY_TO_SAVE_IMAGES, image_file)
    if not os.path.exists(DIRECTORY_TO_SAVE_IMAGES):
        os.makedirs(DIRECTORY_TO_SAVE_IMAGES)
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_nasa_apod_images(token, entry_url, days, filename_template):
    while days >= 0:
        apod_date = datetime.today() - timedelta(days=days)
        image_date = "{}-{}-{}".format(apod_date.year, apod_date.month, apod_date.day)
        if not get_nasa_image_url(token, entry_url, image_date) == None:
            image_url = get_nasa_image_url(token, entry_url, image_date)
            image_file = "{}{}.jpg".format(filename_template, image_date)
            download_nasa_image(image_url, image_file)
        days = days - 1


if __name__ == '__main__':
    load_dotenv()
    fetch_nasa_apod_images(os.environ['NASA_API_KEY'], NASA_APOD_URL, NUMBER_OF_DAYS, NASA_FILENAME_TEMPLATE)

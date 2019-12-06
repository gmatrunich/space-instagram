import os
from dotenv import load_dotenv
from imgurpython import ImgurClient


DIRECTORY_WITH_IMAGES = 'images'
CROPPED_IMAGES_PREHEADER = 'cropped_'


def authenticate(client_id, client_secret, access_token, refresh_token):
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)
    return client


def send_images_to_imgur(client, directory):
    file_names = os.listdir(directory)
    not_cropped_images = filter(lambda x: not x.startswith(CROPPED_IMAGES_PREHEADER), file_names)
    for image in not_cropped_images:
        image = client.upload_from_path(os.path.join(directory, image), anon=False)


if __name__ == "__main__":
    load_dotenv()
    client = authenticate(os.environ['IMGUR_CLIENT_ID'], 
                          os.environ['IMGUR_CLIENT_SECRET'], 
                          os.environ['IMGUR_ACCESS_TOKEN'], 
                          os.environ['IMGUR_REFRESH_TOKEN']
			  )
    send_images_to_imgur(client, DIRECTORY_WITH_IMAGES)

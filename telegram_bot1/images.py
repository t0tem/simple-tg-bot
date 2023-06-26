import requests
import re


def get_dog_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def get_dog_image_url():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_dog_url()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    return url


def get_cat_image_url():
    contents = requests.get('http://aws.random.cat/meow?ref=apilist.fun').json()
    url = contents['file']
    return url


def get_panda_image_url():
    contents = requests.get('https://some-random-api.ml/img/panda').json()
    url = contents['link']
    return url


def get_red_panda_image_url():
    contents = requests.get('https://some-random-api.ml/img/red_panda').json()
    url = contents['link']
    return url


def get_koala_image_url():
    contents = requests.get('https://some-random-api.ml/img/koala').json()
    url = contents['link']
    return url

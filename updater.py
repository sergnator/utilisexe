import requests

import constants
from constants import VERSION, HREF, HREF_DOWNLOAD


def check_update():
    response = requests.get(HREF).json()
    current_version = response['commit']['commit']['message']
    if current_version == VERSION.split()[1]:
        return False
    return current_version


def download():
    content = requests.get(HREF_DOWNLOAD)
    with open('prgm.exe', 'wb') as f:
        f.write(content.content)
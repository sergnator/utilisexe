import sys

import requests
import os

from constants import VERSION, HREF, HREF_DOWNLOAD


def check_update():
    response = requests.get(HREF).json()
    current_version = response['commit']['commit']['message']
    if current_version == VERSION.split()[1]:
        return False
    return current_version


def download():
    os.rename('prgm.exe', 'prgm2.exe')
    content = requests.get(HREF_DOWNLOAD)
    with open('prgm.exe', 'wb') as f:
        f.write(content.content)
    os.system('prgm.exe delete --file prgm2.exe')
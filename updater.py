import requests
from constants import VERSION


def check_update():
    response = requests.get('https://api.github.com/repos/sergnator/pacmanpygame/branches/main').json()
    current_version = response['commit']['commit']['message']
    if current_version == VERSION.split()[1]:
        return False
    return True

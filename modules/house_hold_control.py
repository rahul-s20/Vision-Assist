import requests
from utils.config import ELECTRICAL_CONN


class HouseHold:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/71.1.2222.33 Safari/537.36",
            "Accept-Encoding": "*",
            "Connection": "keep-alive"
        }

    def electrical_control_func(self, segment: str, is_on: str, url: str = ELECTRICAL_CONN):
        """
        segment = 25(light) / 27(fan)
        is_on = on / off
        """
        if segment == 'light':
            segment = '25'
        elif segment == 'fan':
            segment = '27'
        if is_on == 'on' or is_on == 'off':
            print(f'{url}{segment}/{is_on}')
            res = self.session.get(f'{url}{segment}/{is_on}')
            return res
        else:
            raise ValueError(f"something went wrong in electrical control -> {segment} and {is_on}")

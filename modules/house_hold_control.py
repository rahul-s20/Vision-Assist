import requests
from utils.config import ELECTRICAL_CONN


class HouseHold:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36",
            "Accept-Encoding": "*",
            "Connection": "keep-alive"
        }

    def el_control_func(self, alias: str, pin_no: str,  is_on: str, url: str = ELECTRICAL_CONN):
        """
        segment = 25(light) / 27(fan)
        is_on = on / off
        """
        if is_on == 'on' or is_on == 'off':
            print(f'{url}{pin_no}/{is_on}')
            res = self.session.get(f'{url}{pin_no}/{is_on}')
            return res
        else:
            raise ValueError(f"something went wrong in electrical control -> {alias} and {is_on}")

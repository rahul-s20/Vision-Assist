import requests
from utils.config import ELECTRICAL_CONN


class HouseHold:
    def __init__(self):
        self.session = requests.Session()
        # self.session.headers = {
        #     "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36",
        #     "Accept-Encoding": "*",
        #     "Connection": "keep-alive"
        # }
        # self.session.headers ={
        #     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
        #                   "Chrome/51.0.2704.103 Safari/537.36"}

    def el_control_func(self, alias: str, pin_no: str,  is_on: str, url: str = 'http://192.168.1.22/'):
        """
        segment = 25(light) / 27(fan)
        is_on = on / off
        """
        if is_on == 'on' or is_on == 'off':
            print(f'{url}{alias}?state={is_on}&out_put={pin_no}')
            res = self.session.get(f'{url}{alias}?state={is_on}&out_put={pin_no}')
            return res
        else:
            raise ValueError(f"something went wrong in electrical control -> {alias} and {is_on}")
        
    def el_vision_control_func(self, device: str, mode: str, url: str = 'https://visionapi.loca.lt/api/v1/VisionHome/switch'):
        """
        segment = 25(light) / 27(fan)
        is_on = on / off
        """
        if mode == 'on' or mode == 'off':
            print(f'{url}?device={device}&mode={mode}')
            res = self.session.post(f'{url}?device={device}&mode={mode}')
            return res
        else:
            raise ValueError(f"something went wrong in electrical control -> {device} and {mode}")    

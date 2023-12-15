from utils.speech_control.audio_io import VoiceAssistant
from modules.house_hold_control import HouseHold
from brain_cell.skl_model import predict
from utils.config import MONGO_URI
from mongoengine import connect

connect(host=MONGO_URI)

print('Connected to DB')


def run():
    va_obj = VoiceAssistant()
    hh_obj = HouseHold()

    while True:
        speech = va_obj.take_speech()
        if 'vision' in speech:
            out = predict(speech)
            print(out)
            if '_func' in out:
                eval(out)
                va_obj.say("Done")
            else:
                va_obj.say(out)

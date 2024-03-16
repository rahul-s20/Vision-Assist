from utils.speech_control.audio_io import VoiceAssistant
from modules.house_hold_control import HouseHold
from brain_cell.skl_model import predict
from utils.config import MONGO_URI
from mongoengine import connect
from vosk import Model, KaldiRecognizer
import pyaudio
import json
import warnings

warnings.filterwarnings("ignore")

# connect(host=MONGO_URI)

print('Connected to DB')


def run():
    va_obj = VoiceAssistant()
    hh_obj = HouseHold()
    while True:
        speech = va_obj.take_speech()
        if 'fan' in speech or 'light' in speech:
            out = predict(speech)
            if '_func' in out:
                eval(out)
                va_obj.say("Done")
            else:
                va_obj.say(out)

        if 'vision' in speech:
            out = predict(speech)
            print(out)
            if '_func' in out:
                eval(out)
                va_obj.say("Done")
            else:
                va_obj.say(out)
        else:
            continue


def run2():

    model = Model(r"/home/rahuls/Documents/Projects/Vison2R/Vision-Assist/vosk_model/vosk-model-en-us-0.22")
    recogniser = KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()
    va_obj = VoiceAssistant()
    hh_obj = HouseHold()
    while True:
        print("Listening....")
        data = stream.read(4096, exception_on_overflow=False)
        print("Recognizing....")
        if recogniser.AcceptWaveform(data):
            out = recogniser.Result()
            out = json.loads(out)['text']
            print(f"User said : {out}\n")
            if 'vision' in out:
                out = predict(out)
                if '_func' in out:
                    eval(out)
                    va_obj.say("Done")
                else:
                    va_obj.say(out)
        # else:
        #     continue

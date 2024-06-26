import speech_recognition as sr
import pyttsx3
import multiprocessing
import keyboard
from utils.config import THRESHOLD

def callback(recognizer, audio):                          # this is called from the background thread
    try:
        print("You said " + recognizer.recognize(audio))  # received audio data, now need to recognize it
    except LookupError:
        print("Oops! Didn't catch that")


class VoiceAssistant:
    def __init__(self):
        self.r = sr.Recognizer()

    def take_speech(self):
        try:
            with sr.Microphone(device_index=1) as source:
                print("Listening....")
                self.r.adjust_for_ambient_noise(source)      
                # self.r.pause_threshold = 1
                self.r.energy_threshold = THRESHOLD
                audio = self.r.listen(source, 5, 6)
                # stop_listening = self.r.listen_in_background(source, callback)
                print("Recognizing....", audio.sample_rate)
                query = self.r.recognize_google(audio, language='en-in')
                print(f"User said : {query}\n")
                return query
        except Exception as e:
            print("Please Say that again.", e)
            return "None"

    def speak_loop(self, phrase: str):
        engine = pyttsx3.init()
        engine.setProperty('rate', 160)
        engine.say(phrase)
        engine.runAndWait()

    def say(self, phrase):
        # if __name__ == "__main__":
        print("in...............")
        p = multiprocessing.Process(target=self.speak_loop, args=(phrase,))
        p.start()
        while p.is_alive():
            if keyboard.is_pressed('q'):
                p.terminate()
                print("do something else")
                ph = self.take_speech()
                self.say(ph)
            else:
                continue
            # ph1 = self.take_speech()
            # self.say(ph1)
        p.join()

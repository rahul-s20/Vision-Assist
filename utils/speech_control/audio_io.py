import speech_recognition as sr
import pyttsx3
from queue import Queue
from threading import Thread
import multiprocessing
import keyboard


class VoiceAssistant:
    def __init__(self):
        self.r = sr.Recognizer()

    def take_speech(self):
        try:
            with sr.Microphone(device_index=1) as source:
                print("Listening....")
                self.r.pause_threshold = 1
                self.r.energy_threshold = 1000
                audio = self.r.listen(source)
                print("Recognizing....")
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

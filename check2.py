from utils.speech_control.audio_io import VoiceAssistant

if __name__ == "__main__":
    va_obj = VoiceAssistant()
    while True:
        speech = va_obj.take_speech()
        va_obj.say(speech)

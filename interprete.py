import speech_recognition as sr
from mtranslate import translate
from gtts import gTTS
import pyttsx3

#Traduce una cadena de texto al idioma q se especifica como segundo argumento
def trans3(string, lan):
    trad = translate(string, lan)
    return trad

r =  sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Hola, Soy tu Traductor :D")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("Quisiste decir: ", text)
            
            #traduce
            text_totranslate = text
            lan = "es"
            translated_text = trans3(text_totranslate, lan)
            
            #imprimimos la traduccion
            print({translated_text})
            
            #Reproduccion
            tts = gTTS(text=translated_text, lang='es')
            engine = pyttsx3.init()
            engine.say(translated_text)
            engine.runAndWait()
        except:
            print("....")
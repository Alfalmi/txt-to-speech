import pyttsx3
import PyPDF2

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voice.id)
    print('name :' + voice.name)
    for lang in voice.languages:
        print('ager :' + lang)

    engine.say('Culerisimo')
engine.runAndWait()

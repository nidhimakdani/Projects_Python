import wolframalpha
import wikipedia
import speech_recognition as sr
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak...")
        audio = r.listen(source,phrase_time_limit=5)
        audio_data = r.record(source,duration=5)
        print("Recognizing... It'll take some seconds")
        text = r.recognize_google(audio_data)

    try:
        app_id = "#add your api id here"
        client = wolframalpha.Client(app_id)

        result = client.query(text)
        answer = next(result.results).text

        print(str(answer))
        speak.Speak(answer)
        
    except:
         print (wikipedia.summary(text))    
         speak.Speak(wikipedia.summary(text))
  
            
    




 

import wolframalpha
import wikipedia
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")


while True:
    data = input("Ask: ")
    try:
        app_id = "#Use Your News Api Key here   #Read it"
        client = wolframalpha.Client(app_id)

        result = client.query(data)
        answer = next(result.results).text

        print(str(answer))
        speak.Speak(answer)
        
    except:
         print (wikipedia.summary(data))    
         speak.Speak(wikipedia.summary(data))

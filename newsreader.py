def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == "__main__":
    import requests
    import json
    speak("Todays News...")
    url = ("http://newsapi.org/v2/top-headlines?country=in&apiKey=918d7dc0bdd342dcbcb22814f655263c")
    response = requests.get(url).text
    my_news = json.loads(response)
    store_news = my_news['articles']
    for article in store_news:
        print(article['title'])
        speak(article['title'])
        speak("Next News.....")
    speak("Thanks for listening...")


import wikipedia

while True:
    data = input("Question: ")
    print (wikipedia.summary(data))
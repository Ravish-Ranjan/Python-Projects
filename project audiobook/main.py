import pyttsx3
with open('C:/sem4/vs code/Done/python projects/project audiobook/text.txt','r') as fob:
    data = fob.readlines()
engine = pyttsx3.init()

for line in data:
    engine.say(line)
    engine.runAndWait()
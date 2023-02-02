import datetime
import time
from tokenize import Token
from gtts import gTTS
from playsound import playsound
audio = "speech.mp3"
language = "en" 
now = (datetime.datetime.now())
date = str(now.day) + "th"
month = int(now.month)
if month == 1:
    month = "January"
elif month == 2:
    month = "Feburary"
elif month == 3:
    month = "March"
elif month == 4:
    month = "April"
elif month == 5:
    month = "May"
elif month == 6:
    month = "June"
elif month == 7:
    month = "July"
elif month == 8:
    month = "August"
elif month == 9:
    month = "September"
elif month == 10:
    month = "October"
elif month == 11:
    month = "November"
elif month == 12:
    month = "December"
year  = int(now.year)
hour = int(now.hour)
stat = ""
if hour>12:
    hour = str(hour-12)
    stat = "PM"
else:
    stat = "AM"
minute = int(now.minute)
seconds = int(now.second)
mic_sec = int(now.microsecond)
total = "Today is " + (str(date) + "\t" + str(month) + "\t" + str(year)) + "and Right now time is " + (str(hour) + "\t"+ str(minute) + "\t" + stat)
sp=gTTS(text = total,lang = language)
sp.save(audio)
playsound(audio)
import pyttsx3
from pyttsx3 import engine

x = pyttsx3.init()

txt = "Haha!"
for i in range(2):
    x.say(txt)
    x.runAndWait()


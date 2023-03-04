import pyttsx3
from pyttsx3 import engine

x = pyttsx3.init()

txt = "Haha!"
for i in range(2):
    x.say(txt)
    x.runAndWait()

''' 
the engine speaks whatever text is passed to it using the say() method. 

using the runAndWait() method, it blocks during the event loop and returns when the commands queue is cleared
can also use the .setproperty() to set speech rate and volume
 

 '''

from gtts import gTTS
import os
my=input("enter your string")
language='en'
out=gTTS(text=my,lang=language)
out.save("output.mp3")
os.system("start output.mp3")
from PIL import Image
import pytesseract as c
from gtts import gTTS
import os

img = Image.open('C:/Users/Aniruddha Joshi/Desktop/python project for clg/text15.png')

tex=c.image_to_string(img,lang='eng')
out=gTTS(text=tex,lang='en',slow=False)
out.save("output.mp3")
os.system("start output.mp3")
print(tex)
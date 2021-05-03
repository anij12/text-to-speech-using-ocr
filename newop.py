from tkinter import *
from tkinter import filedialog as fd
import pytesseract as c
from gtts import gTTS
import os
from PIL import Image

def get_file_name(file_entry):
    file_name = fd.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),))
    file_entry.delete(0,END)
    file_entry.insert(0,file_name)

def close(event=None):
    master.withdraw() # if you want to bring it back
    sys.exit() # if you want to exit the entire thing
    
def mcod():
    cimg=entry_csv.get()
    img = Image.open(cimg)
    tex=c.image_to_string(img,lang='eng')
    out=gTTS(text=tex,lang='en',slow=False)
    out.save("output.mp3")
    os.system("start output.mp3")
    print(tex)
master = Tk()
master.title("This is my Interface")

entry_csv=Entry(master, text="", width=50)
entry_csv.grid(row=0, column=1, sticky=W, padx=5)

Label(master, text="Input png file").grid(row=0, column=0 ,sticky=W)
Button(master, text="Browse...", width=10, command=lambda:get_file_name(entry_csv)).grid(row=0, column=2, sticky=W)

#Button(master, text="Ok",     command=run_and_close, width=10).grid(row=3, column=1, sticky=E, padx=5)
Button(master, text="Cancel", command=close, width=10).grid(row=3, column=2, sticky=W)

Button(master, text="convert",command=mcod,width=10).grid(row=3, column=1, sticky=E)
#master.bind('<Return>', run_and_close)
master.bind('<Escape>', close)
mainloop()

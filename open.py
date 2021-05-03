from tkinter import *
from tkinter import filedialog
root=Tk()
root.title('image to speak')
def open():
    global my_img
    root.filename=filedialog.askopenfilename(filetypes=(("all files","*.*")))
    if filename:
        try:
            print("""here it comes: self.settings["template"].set(filename)""")
        except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % filename)
    #print(root.filename)

my_bt = Button(root,text="Open",command=open).pack()
#print(root.filename)
root.mainloop()

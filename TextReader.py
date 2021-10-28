from tkinter import *
from tkinter import filedialog
import pyttsx3
from PIL import Image, ImageTk

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(event):
    global read
    if read=='':
        read='Please insert a text or a file'
    engine.say(read)
    engine.runAndWait()


def upload():
    global read
    read=txt.get(1.0,'end-1c')
    read=read.replace('hi','hi,')
    read=read.replace('Hi','Hi,')
    link.set('Staged the input text...')

read=''

def browseFile():
    global read
    filename=filedialog.askopenfilename(initialdir="/",title="File Explorer",filetypes=(("Text files","*.txt*"),("all files","*.*")))
    link.set("Staged File: "+filename)
    f=open(filename,"r")
    read=f.read()
    read=read.replace('hi','hi,')
    read=read.replace('Hi','Hi,')
    txt.configure(background='red')

# Initializing GUI......
window=Tk()
window.title('TextReader')
w=window.winfo_screenwidth()
h=window.winfo_screenheight()
window.geometry(f"{w}x400")
window.wm_iconbitmap('tricon.ico')
# window.attributes("-fullscreen",True)
window.config(background='white')
Label(window,width=3,background='white',text='').pack(fill=Y,side='left')
Label(window,width=3,background='white',text='').pack(fill=X,side='bottom')
Label(window,width=3,background='white',text='').pack(fill=Y,side='right')
f=Frame(window).pack(fill=BOTH)
Label(f,text='Insert Your Text Here',state=DISABLED,background='white',anchor='w').pack(fill=X)

sbr=Scrollbar(f)
sbr.pack(side=RIGHT,fill=Y)
txt=Text(f,height=10,relief=SUNKEN,border=2,background='#b8b9bb',yscrollcommand=sbr.set,padx=20,pady=20)
txt.pack(fill=BOTH,padx=10)
sbr.config(command=txt.yview)







link=StringVar()
text=StringVar()
link.set("File Explorer using Tkinter")
button_upload=Button(f,text='Upload',command=upload).pack(anchor='w')
button_explore=Button(f,text="Browse Files",command=browseFile).pack(anchor='w')
label_file_explorer=Label(f,textvariable=link,fg='blue',anchor='w').pack(side=BOTTOM,fill=X)
img=Image.open("speaker.jpg")
img=img.resize((40,40))
img1=ImageTk.PhotoImage(img,size=4)
rd=Label(window,image=img1,activeforeground='red',relief=SUNKEN)
rd.bind("<Button-1>",speak)
rd.pack()

window.mainloop()


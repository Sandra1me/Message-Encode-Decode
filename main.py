from tkinter import *


def encoding():
    text=mess.get()
    resul.delete(0, 'end')
    textR=""
    keyA=key.get()
    
    try:
        keyA=int(keyA)
    except:
        resul.insert(0, "Insert a number bigger than 1")

    if keyA > 256:
        keyA=keyA-256
    elif keyA < 0:
        resul.insert(0, "Key must be bigger than one")
        return

    for i in range(len(text)):
        textO=ord(text[i])+keyA
        
        if textO > 256:
            textO=textO-256
        elif textO < 0:
            textO=textO+256
        textR=textR+chr(textO)
    
    resul.insert(0, textR)

def decoding():
    text=mess.get()
    resul.delete(0, 'end')
    textR=""
    keyA=key.get()
    
    try:
        keyA=int(keyA)
    except:
        resul.insert(0, "Insert a number bigger than 1")

    if keyA > 256:
        keyA=keyA-256
    elif keyA < 0:
        resul.insert(0, "Key must be bigger than one")
        return

    for i in range(len(text)):
        textO=ord(text[i])-keyA
        
        if textO > 256:
            textO=textO-256
        elif textO < 0:
            textO=textO+256
        textR=textR+chr(textO)
    
    resul.insert(0, textR)

def reseting():
    resul.delete(0, 'end')
    key.delete(0, 'end')
    mess.delete(0, 'end')

root=Tk()
root.title("Message Enconde-Decode")
root.geometry("450x300")
root.config(bg="#66C4D9")
root.resizable(0,0)

text=Label(root,text="Write your message", bg="#66C4D9", foreground="#021F59")
text.grid(row=1,column=0, pady=20, columnspan=2, padx=20)

mess=Entry(root,width=40)
mess.grid(row=1,column=2, padx=10, columnspan=2)

text=Label(root,text="Key", bg="#66C4D9", foreground="#021F59")
text.grid(row=2,column=0, pady=20, columnspan=2, padx=20)

key=Entry(root,width=40)
key.grid(row=2,column=2, padx=10, columnspan=2)

encoding=Button(root, text="Encode", pady=5, padx=5, command=encoding, foreground="#021F59", bg="#0468BF")
encoding.grid(row=3,column=1, pady=20)

decoding=Button(root, text="Decode", pady=5, padx=5, command=decoding, foreground="#021F59", bg="#0468BF")
decoding.grid(row=4,column=1)

text2=Label(root,text="Result", bg="#66C4D9", foreground="#021F59")
text2.grid(row=3,column=2, pady=10, columnspan=2)

resul=Entry(root, width=40)
resul.grid(row=3,column=2, padx=10, columnspan=2, rowspan=2)

reseting=Button(root,text="Reset", pady=5, padx=20, command=reseting, foreground="#021F59", bg="#0460D9")
reseting.grid(row=6,column=2, pady=20)

exit=Button(root,text="Exit", pady=5, padx=20, command=root.destroy, foreground="#021F59", bg="#BF8069")
exit.grid(row=6,column=3, pady=20)


root.mainloop()
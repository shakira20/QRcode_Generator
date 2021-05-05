from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
root=Tk()

def generate_qrcode():
    link_name=name_entry.get()
    link=link_entry.get()
    file_name=link_name + ".png"
    url=pyqrcode.create(link)
    url.png(file_name,scale=8)
    image=ImageTk.PhotoImage(Image.open(file_name))
    image_label=Label(image=image)
    image_label.image=image
    canvase.create_window(200,450,window=image_label)



canvase=Canvas(root,width=400,height=600)
canvase.pack()
app_label=Label(root,text="QrCode Generator",font=("arial",30),fg="purple")
canvase.create_window(200,50,window=app_label)
name_entry=Entry(root)
link_entry=Entry(root)
name_label=Label(root,text="link name")
link_label=Label(root,text="link")
canvase.create_window(200,100,window=name_label)
canvase.create_window(200,150,window=link_label)

canvase.create_window(200,130,window=name_entry)
canvase.create_window(200,180,window=link_entry)

button=Button(root,text="Generate QR code",command=generate_qrcode)
canvase.create_window(200,230,window=button)
root.mainloop()
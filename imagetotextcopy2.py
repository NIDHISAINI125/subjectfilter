def search():
    
    fil=filedialog.askopenfilename(title="select image file")
    
    img=Image.open(fil)
    imagelink.set(fil)
    img.thumbnail((350,350))
    img=ImageTk.PhotoImage(img)
    
    lbl.configure(image=img)
    lbl.image=img
def textcon():
    link=imagelink.get()
    t = tess.image_to_string(link)
    display.delete(1.0,END)
    display.insert(END,t)

def sub():
    countcpp=0
    countim=0
    result=""
    ab=imagelink.get()
    tex= tess.image_to_string(ab)
    li=list(tex.split(" "))
    subject.delete(1.0,END)
    for x in li:
        if x in lst:
            countcpp+=1
        elif x in imlst:
            countim+=1
        else:
            pass
    if countcpp>0:
        result="C++"
    elif countim>0:
        result="Industrial Management"
    subject.insert(END,result)
    
            
                 


    
def widget():
    browse=Button(root,text='Search',bg='green',font=('arial',13,'bold'),width=10,bd=5,
                  activebackground='yellow',command=search)
    browse.grid(row=2,column=1,padx=20,pady=20)
    
    showtext=Button(root,text="Show text",bg='green',font=('arial',13,'bold'),width=10,bd=5,
                  activebackground='yellow',command=textcon)
    showtext.grid(row=2,column=2,padx=20,pady=20)
    

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract as tess
tess.pytesseract.tesseract_cmd= r'C:/Program Files/Tesseract-OCR/tesseract.exe'


root = Tk()
root.title("Image to Text")
root.geometry("900x900")
root.configure(bg='black')
lbl = Label(root)
lbl.grid(row=0,column=1,padx=15,pady=15)
display=Text(root,height=20,width=40,font=('arial',13,'bold'))
display.grid(row=0,column=2,padx=15,pady=15)
subject=Text(root,height=5,width=40,font=('arial',13,'bold'))
subject.grid(row=4,column=2,padx=15,pady=15)
showsub=Button(root,text="Show subject",bg='green',font=('arial',13,'bold'),width=10,bd=5,
                  activebackground='yellow',command=sub)
showsub.grid(row=5,column=2,padx=15,pady=15)
lst=['STL','templates','C++']
imlst=['Union','Managemet','Workers']

imagelink=StringVar()

widget()


root.mainloop()







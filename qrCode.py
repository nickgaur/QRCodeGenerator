from tkinter import *
from tkinter import ttk
import qrcode

def submit():
    qr = (entry.get())
    img = qrcode.make(qr)
    img.save(save_file_as.get() +".png")
    img.show()
    quit()


root = Tk()
root.geometry("400x200")
root.title("QR code generator")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')

frame = ttk.Frame(root)
frame.grid(padx=10,pady=10)

link = Label(root, text = 'Enter your Link: ', font=('calibre',10, 'bold'))
entry = Entry(root, textvariable=StringVar,font=('calibre',10,'normal'))

filename = Label(root, text = 'Save file as: ', font=('calibre',10, 'bold'))
save_file_as = Entry(root, textvariable=StringVar,font=('calibre',10,'normal'))

submit_button = Button(root, text="Generate", command=submit)

link.grid(column=0, row=0, pady=(20,5))
entry.grid(column=1,row=0, pady=(20,5))

filename.grid(column=0,row=1, pady=5)
save_file_as.grid(column=1,row=1, pady=5)

submit_button.grid(column=1,row=3)

root.mainloop()

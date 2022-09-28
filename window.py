import tkinter as tk
from PIL import Image, ImageTk
from demo import demo
from tkinter import filedialog
from PIL import Image

window = tk.Tk()
window.title('CAT or DOG ?')
window.geometry('1000x800')
align_mode = 'nswe'
pad = 5
img_path = ''
imTK = None
CoD = ''
div_size = 200
img_size = div_size * 3

div1 = tk.Frame(window,  width=img_size , height=img_size , bg='blue')
div2 = tk.Frame(window,  width=div_size , height=div_size , bg='orange')
div3 = tk.Frame(window,  width=div_size , height=div_size , bg='green')

window.update()


div1.grid(column=0, row=0, padx=pad, pady=pad, rowspan=2, sticky=align_mode)
div2.grid(column=1, row=0, padx=pad, pady=pad, sticky=align_mode)
div3.grid(column=1, row=1, padx=pad, pady=pad, sticky=align_mode)

def define_layout(obj, cols=1, rows=1):
    def method(trg, col, row):
        for c in range(cols):    
            trg.columnconfigure(c, weight=1)
        for r in range(rows):
            trg.rowconfigure(r, weight=1)
    if type(obj)==list:        
        [ method(trg, cols, rows) for trg in obj ]
    else:
        trg = obj
        method(trg, cols, rows)
        
# button event
def chooser_event():
    global img
    global image_main
    global imTK
    img_path = filedialog.askopenfilename()
    print(img_path)
    img = Image.open(img_path)
    imTK = ImageTk.PhotoImage(img.resize( (img_size, img_size) ) )
    image_main.configure(image=imTK)
    
    
def start_event():
    global CoD
    global img
    global lbl_title2
    CoD = demo(img)
    lbl_title2.configure(text=CoD)
    
def reset_event():
    global img_path
    global imTK
    global img
    global image_main
    global CoD
    global lbl_title2
    img_path = ''
    imTK = None
    img = None
    CoD = ''
    image_main.configure(image=imTK)
    lbl_title2.configure(text=CoD)
    
    
def quit_event():
    window.destroy()
    

define_layout(window, cols=2, rows=2)
define_layout([div1, div2, div3])

# image set
img_path = "./data/demo/test1.jpg"
img = Image.open(img_path)
imTK = ImageTk.PhotoImage(img.resize( (img_size, img_size) ) )
image_main = tk.Label(div1, image=imTK)
image_main['height'] = img_size
image_main['width'] = img_size
image_main.grid(column=0, row=0, sticky=align_mode)

# word set
lbl_title1 = tk.Label(div2, text='This is a ...', bg='orange', fg='white', font=('Arial', 24))
lbl_title2 = tk.Label(div2, text=CoD, bg='orange', fg='white', font=('Arial', 48))

lbl_title1.grid(column=0, row=0, sticky=align_mode)
lbl_title2.grid(column=0, row=1, sticky=align_mode)

# button set
bt1 = tk.Button(div3, text='Choose File', bg='green', fg='white', font=('Arial', 18), command=chooser_event)
bt2 = tk.Button(div3, text='Start', bg='green', fg='white', font=('Arial', 18), command=start_event)
bt3 = tk.Button(div3, text='Reset', bg='green', fg='white', font=('Arial', 18), command=reset_event)
bt4 = tk.Button(div3, text='Quit', bg='green', fg='white', font=('Arial', 18), command=quit_event)

bt1.grid(column=0, row=0, sticky=align_mode)
bt2.grid(column=0, row=1, sticky=align_mode)
bt3.grid(column=0, row=2, sticky=align_mode)
bt4.grid(column=0, row=3, sticky=align_mode)


define_layout(window, cols=2, rows=2)
define_layout(div1)
define_layout(div2, rows=2)
define_layout(div3, rows=4)

window.mainloop()
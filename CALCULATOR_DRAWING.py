from tkinter import *
from tkinter import Menu
from tkinter import filedialog
from tkinter import messagebox
import math
import tkinter as tk

root = Tk()
root.geometry = ("1000×500+100+200")
root.title("Calculator")
root.resizable(0, 0)
input_text = StringVar()

Mainf = Frame(root, bg = "lavender", width = 400, height = 400)
Mainf.pack(fill= "both",expand = True)

Drawf = Frame(root, bg = "lavender", width = 400, height = 400)
canvas = Canvas(Drawf, bg = "White", height = 400, width = 400)

"""canvas.bind("<Button-1>", start_draw())
canvas.bind("<B1-Motion>", draw())
canvas.bind("<ButtonRelease-1>", stop_draw())"""


coord = 10,10,300,300
canvas = Canvas(Drawf,bg="White",height=600,width=600)
#arc = canvas.create_arc(coord,start = 0, extent = 150, fill = "red")
#arc2 = canvas.create_arc(coord,start =150, extent =215,fill = "green")
canvas.pack(fill=BOTH, expand=True)
drawing = False
last_x = None
last_y = None
canvas.old_coords = None
def start_draw(event):
    x,y = event.x, event.y
    if canvas.old_coords :
        x1, y1 = canvas.old_coords
        canvas.create_line(x,y, x1,y1,fill=pen_color,width = 5)
    canvas.old_coords = x, y
    #last_x, last_y = event.x, event.y

def draw(event, last_x=None,last_y = None):
    if drawing:
        x, y = event.x, event.y
        line = canvas.create_line(last_x, last_y, x, y, fill=pen_color, width=2)
        lines.append(line)  # Store the drawn line
        last_x, last_y = x, y
def erase():
    canvas.delete("all")

erase_button = Button(Drawf,text = "Erase",command = erase)
erase_button.pack(side=LEFT)
pen_color = "Green"

lines = []
root.bind("<Delete>", erase())
root.bind("<ButtonPress-1>", start_draw)
root.bind("<B1-Motion>",draw)


Main_entry = Entry(Mainf, bg = "White", width = 27,textvariable = input_text, font = ("Arial",24), justify= "right")
Main_entry.grid(row=0, column=0, columnspan=6)
Main_entry.insert(0,'0')

Button_entry = Frame(Mainf)
Button(Mainf,text = "=",width = 15, height = 2,  bg = "#FF6347", cursor = "hand2",command = lambda: btn_equal(),font=("Arial", 14)).grid(row=4, column=4, columnspan = 4)
        #Button(master,text = "C",fg = "black",width = 8, height = 2, bd = 0, bg = "sky blue", cursor = "hand2", command = self.clearall(), font = ("Arial",14)).grid(row=1, column=4,columnspan = 3)
Button(Mainf, text='AC', width=6,height = 2,bg = "sky blue",cursor = "hand2",command = lambda: btn_clear(),font=("Arial", 14)).grid(row=1, column=4)
Button(Mainf, text='C', width=6,height = 2,bg = "sky blue", cursor = "hand2",command = lambda: clear(),font=("Arial", 14)).grid(row=1, column=5)
Button(Mainf, text="+", width = 6, height =2, bg = "#1E90FF",cursor = "hand2",command = lambda: btn_click("+"),font=("Arial", 14)).grid(row=4, column=3)
Button(Mainf, text="x", width = 6, height =2, bg = "#1E90FF",command = lambda: btn_click("x"),font=("Arial", 14)).grid(row=2, column=3)
Button(Mainf, text="-", width = 6, height =2, bg = "#1E90FF",command = lambda: btn_click("-"),font=("Arial", 14)).grid(row=3, column=3)
Button(Mainf, text="÷", width = 6, height =2, bg = "#1E90FF",command = lambda: btn_click("÷"),font=("Arial", 14)).grid(row=1, column=3)
Button(Mainf, text="%", width = 6, height =2, bg = "#1E90FF",command = lambda: btn_click(" % "),font=("Arial", 14)).grid(row=4, column=2)
Button(Mainf, text="7", width = 6,height = 2, bg = "#fff", cursor = "hand2",command = lambda: btn_click(7),font=("Arial", 14)).grid(row=1, column=0)
Button(Mainf, text="8", width = 6, height =2,bg = "#fff", cursor = "hand2",command = lambda: btn_click(8),font=("Arial", 14)).grid(row=1, column=1)
Button(Mainf, text="9", width = 6, height =2,bg = "#fff", cursor = "hand2",command = lambda: btn_click(9),font=("Arial", 14)).grid(row=1, column=2)
Button(Mainf, text="4", width = 6, height =2,bg = "#fff", cursor = "hand2",command = lambda: btn_click(4),font=("Arial", 14)).grid(row=2, column=0)
Button(Mainf, text="5", width = 6, height =2,bg = "#fff", cursor = "hand2",command = lambda: btn_click(5),font=("Arial", 14)).grid(row=2, column=1)
Button(Mainf, text="6", width = 6, height =2,bg = "#fff", cursor = "hand2",command = lambda: btn_click(6),font=("Arial", 14)).grid(row=2, column=2)
Button(Mainf, text = "1",width = 6, height = 2, bg = "#fff", cursor = "hand2",command = lambda: btn_click(1),font=("Arial", 14)).grid(row=3, column=0)
        #Button(master, text="1", width=3, command=lambda: self.action('1')).grid(row=3, column=0)
Button(Mainf, text = "2",width = 6, height = 2, bg = "#fff", cursor = "hand2",command = lambda: btn_click(2),font=("Arial", 14)).grid(row=3, column=1)
        #Button(master, text="2", width=3, command=lambda: self.action('2')).grid(row=3, column=1)
Button(Mainf, text="3", width=6, height =2,bg = "#fff", cursor = "hand2",command = lambda: btn_click(3),font=("Arial", 14)).grid(row=3, column=2)
Button(Mainf, text="0", width=6, height =2,bg = "#fff", cursor = "hand2",command = lambda: btn_click(0),font=("Arial", 14)).grid(row=4, column=1)
Button(Mainf, text=".", width=6, height =2,bg = "#1E90FF", cursor = "hand2",command = lambda: btn_click("."),font=("Arial", 14)).grid(row=4, column=0)
Button(Mainf, text="(", width=6, height =2,bg = "#1E90FF", cursor = "hand2",command = lambda: btn_click("("),font=("Arial", 14)).grid(row=2, column=4)
Button(Mainf, text=")", width=6, height =2,bg = "#1E90FF", cursor = "hand2",command = lambda: btn_click(")"),font=("Arial", 14)).grid(row=2, column=5)
Button(Mainf, text="√", width=6, height =2,bg = "#1E90FF", cursor = "hand2",command = lambda: squart(),font=("Arial", 14)).grid(row=3, column=4)
Button(Mainf, text="x²", width=6, height =2,bg = "#1E90FF",command = lambda: square(),font=("Arial", 14)).grid(row=3, column=5)

root.bind("<Return>",lambda event: btn_equal())
root.bind("<BackSpace>",lambda event: clear())
root.bind("1",lambda event: btn_click("1"))
root.bind("2",lambda event: btn_click("2"))
root.bind("3",lambda event: btn_click("3"))
root.bind("4",lambda event: btn_click("4"))
root.bind("5",lambda event: btn_click("5"))
root.bind("6",lambda event: btn_click("6"))
root.bind("7",lambda event: btn_click("7"))
root.bind("8",lambda event: btn_click("8"))
root.bind("9",lambda event: btn_click("9"))
root.bind("0",lambda event: btn_click("0"))
root.bind(".",lambda event: btn_click("."))
root.bind("(",lambda event: btn_click("("))
root.bind(")",lambda event: btn_click(")"))
root.bind("+",lambda event: btn_click("+"))
root.bind("-",lambda event: btn_click("-"))
root.bind("/",lambda event: btn_click("÷"))
root.bind("*",lambda event: btn_click("x"))
root.bind("<Delete>",lambda event: btn_clear())
root.bind("<KP_Delete>",lambda event: btn_clear())
root.bind("d",lambda event: btn_clear())


root.bind("<KP_1>",lambda event: btn_click("1"))
root.bind("<KP_2>",lambda event: btn_click("2"))
root.bind("<KP_3>",lambda event: btn_click("3"))
root.bind("<KP_4>",lambda event: btn_click("4"))
root.bind("<KP_5>",lambda event: btn_click("5"))
root.bind("<KP_6>",lambda event: btn_click("6"))
root.bind("<KP_7>",lambda event: btn_click("7"))
root.bind("<KP_8>",lambda event: btn_click("8"))
root.bind("<KP_9>",lambda event: btn_click("9"))
root.bind("<KP_0>",lambda event: btn_click("0"))
root.bind("<KP_Decimal>",lambda event: btn_click("."))
root.bind("<KP_Add>",lambda event: btn_click("+"))
root.bind("<KP_Subtract>",lambda event: btn_click("-"))
root.bind("<KP_Divide>",lambda event: btn_click("÷"))
root.bind("<KP_Multiply>",lambda event: btn_click("x"))


def btn_click(item):
    global expression
    expression = str(expression) + str(item)
    input_text.set(expression)


def btn_clear():
    global expression
    expression = ""
    input_text.set("0")


def btn_equal():
    global expression
    expression = expression.replace("x", "*")
    expression = expression.replace("÷", "/")
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("")
        Main_entry.insert(0, "Error!")
        pass


def square():
    global expression

    expression = math.pow(float(expression), 2)
    input_text.set(expression)


def squart():
    global expression

    expression = math.sqrt(float(expression))
    input_text.set(expression)


def mod():
    global expression

    expression = math.modf(float(expression))
    input_text.set(expression)


expression = ""


def quit():
    root.quit()
    root.destroy()
    exit()


def openFile():
    Main_entry.delete(0, END)
    filepath = filedialog.askopenfilename(initialdir="/hme", title="Open",
                                          filetypes=(("Text Files", "*.txt"), ("All Files", "*,*")))
    file = open(filepath, 'r')
    stuff = file.read()
    Main_entry.insert(END, stuff)
    print(file.read())
    file.close()


def INFO():
    messagebox.showinfo("About", "This app is Developed by Sreejeet Shome")


def cal():
    root.title("Calculator")
    Drawf.pack_forget()
    canvas.pack_forget()
    Mainf.pack()


def draw():
    root.title("Drawing")
    Mainf.pack_forget()
    erase()
    Drawf.pack(fill=BOTH, expand=True)
    canvas.pack(fill=BOTH,expand = True)


def clear():
    numlen = len(str(Main_entry.get()))
    Main_entry.delete(numlen - 1, "end")
    if numlen == 1:
        global expression
        expression = ""
        input_text.set("0")


menuBar = Menu(root)
root.config(menu=menuBar)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)
menuBar.add_cascade(label="File", menu=fileMenu)
# Help Menu
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=INFO)
menuBar.add_cascade(label="Help", menu=helpMenu)
toolsMenu = Menu(menuBar, tearoff=0)
toolsMenu.add_command(label="Draw", command=draw)
toolsMenu.add_command(label="Calculator", command=cal)
menuBar.add_cascade(label="Tools", menu=toolsMenu)

root.mainloop()
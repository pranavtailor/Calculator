import tkinter as tk
import tkinter.font as font

HEIGHT = 800
WIDTH = 460

root = tk.Tk()

def button_click(number):
    current = entry.get()
    entry.delete(0, "end")
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, "end")

def button_add():
    first_number = entry.get()
    global f_num
    f_num = int(first_number)
    entry.delete(0, "end")
    global op
    op = '1'

def button_subtract():
    first_number = entry.get()
    global f_num
    f_num = int(first_number)
    entry.delete(0, "end")
    global op
    op = '2'

def button_multiply():
    first_number = entry.get()
    global f_num
    f_num = int(first_number)
    entry.delete(0, "end")
    global op
    op = '3'

def button_divide():
    first_number = entry.get()
    global f_num
    f_num = int(first_number)
    entry.delete(0, "end")
    global op
    op = '4'


def button_equals():
    second_number = entry.get()
    entry.delete(0, "end")

    if op == '1':
        answer = int(f_num) + int(second_number)
    elif op == '2':
        answer = int(f_num) - int(second_number)
    elif op == '3':
        answer = int(f_num) * int(second_number)
    elif op == '4':
        answer = int(f_num) / int(second_number)

    
    entry.insert(0, answer)



# Define font
myFont = font.Font(family='Helvtica', size=30)

# Entire footprint
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Top number label
top_frame = tk.Frame(root, bg = 'grey')
top_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = .27)

entry = tk.Entry(top_frame, font=40, text="Entry", bg = 'grey')
entry.place(relwidth = 1, relheight = 1)
entry['font'] = myFont

# Bottom frame for buttons
lowframe = tk.Frame(root, bg = "black", bd = 2)
lowframe.place(relx = 0, rely = .27, relwidth = 1, relheight = .73)


# Buttons
AC_button = tk.Button(lowframe, text = "AC", bg = "white", command=button_clear)
AC_button.place(relx = 0, rely = 0, relwidth = .25, relheight = .20)
AC_button['font'] = myFont

neg_button = tk.Button(lowframe, text = "+/-", bg = "white", command=lambda: button_click())
neg_button.place(relx = .25, rely = 0, relwidth = .25, relheight = .20)
neg_button['font'] = myFont

mod_button = tk.Button(lowframe, text = "%", bg = "white", command=lambda: button_click())
mod_button.place(relx = .5, rely = 0, relwidth = .25, relheight = .20)
mod_button['font'] = myFont

divide_button = tk.Button(lowframe, text = "/", bg = "orange", command = button_divide)
divide_button.place(relx = .75, rely = 0, relwidth = .25, relheight = .20)
divide_button['font'] = myFont

button7 = tk.Button(lowframe, text = "7", bg = "white", command=lambda: button_click(7))
button7.place(relx = 0, rely = .2, relwidth = .25, relheight = .20)
button7['font'] = myFont

button8 = tk.Button(lowframe, text = "8", bg = "white", command=lambda: button_click(8))
button8.place(relx = .25, rely = .2, relwidth = .25, relheight = .20)
button8['font'] = myFont

button9 = tk.Button(lowframe, text = "9", bg = "white", command=lambda: button_click(9))
button9.place(relx = .5, rely = .2, relwidth = .25, relheight = .20)
button9['font'] = myFont

multiply_button = tk.Button(lowframe, text = "x", bg = "orange", command = button_multiply)
multiply_button.place(relx = .75, rely = .2, relwidth = .25, relheight = .20)
multiply_button['font'] = myFont

button4 = tk.Button(lowframe, text = "4", bg = "white", command=lambda: button_click(4))
button4.place(relx = 0, rely = .4, relwidth = .25, relheight = .20)
button4['font'] = myFont

button5 = tk.Button(lowframe, text = "5", bg = "white", command=lambda: button_click(5))
button5.place(relx = .25, rely = .4, relwidth = .25, relheight = .20)
button5['font'] = myFont

button6 = tk.Button(lowframe, text = "6", bg = "white", command=lambda: button_click(6))
button6.place(relx = .5, rely = .4, relwidth = .25, relheight = .20)
button6['font'] = myFont

subtract_button = tk.Button(lowframe, text = "-", bg = "orange", command = button_subtract)
subtract_button.place(relx = .75, rely = .4, relwidth = .25, relheight = .20)
subtract_button['font'] = myFont

button1 = tk.Button(lowframe, text = "1", bg = "white", command=lambda: button_click(1))
button1.place(relx = 0, rely = .6, relwidth = .25, relheight = .20)
button1['font'] = myFont

button2 = tk.Button(lowframe, text = "2", bg = "white", command=lambda: button_click(2))
button2.place(relx = .25, rely = .6, relwidth = .25, relheight = .20)
button2['font'] = myFont

button3 = tk.Button(lowframe, text = "3", bg = "white", command=lambda: button_click(3))
button3.place(relx = .5, rely = .6, relwidth = .25, relheight = .20)
button3['font'] = myFont

add_button = tk.Button(lowframe, text = "+", bg = "orange", command = button_add)
add_button.place(relx = .75, rely = .6, relwidth = .25, relheight = .20)
add_button['font'] = myFont

button0 = tk.Button(lowframe, text = "    0", bg = "white", anchor = 'w', command=lambda: button_click(0))
button0.place(relx = 0, rely = .8, relwidth = .5, relheight = .20)
button0['font'] = myFont

dot_button = tk.Button(lowframe, text = ".", bg = "white", command=lambda: button_click())
dot_button.place(relx = .5, rely = .8, relwidth = .25, relheight = .20)
dot_button['font'] = myFont

equals_button = tk.Button(lowframe, text = "=", bg = "orange", command = button_equals)
equals_button.place(relx = .75, rely = .8, relwidth = .25, relheight = .20)
equals_button['font'] = myFont

root.mainloop()

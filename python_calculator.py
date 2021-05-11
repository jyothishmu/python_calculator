# MY FIRST PYTHON PROJECT- CALCULATOR
# AUTHOR : JYOTHISH M.U.
# START FROM 09/05/2021

from tkinter import *

root = Tk()
root.resizable(0, 0)
root.title("CALCULATOR")

# DEFINE TEXT INPUT

my_entry = Entry(root, width=37, font="calibri", justify=RIGHT, insertontime=0)
my_entry.grid(row=0, column=0, columnspan=4, padx=24, pady=15, ipady=15)


# DEFINE BUTTON CLICKS
def button_click(number):
    current_number = my_entry.get()
    my_entry.delete(0, END)
    my_entry.insert(0, str(current_number) + str(number))


def button_clear():
    my_entry.delete(0, END)


def button_add():
    first_number = my_entry.get()
    global first_num
    global math
    math = "addition"
    first_num = int(first_number)
    my_entry.delete(0, END)


def button_substraction():
    first_number = my_entry.get()
    global first_num
    global math
    math = "substraction"
    first_num = int(first_number)
    my_entry.delete(0, END)


def button_multiplicatin():
    first_number = my_entry.get()
    global first_num
    global math
    math = "multiplication"
    first_num = int(first_number)
    my_entry.delete(0, END)


def button_division():
    first_number = my_entry.get()
    global first_num
    global math
    math = "division"
    first_num = int(first_number)
    my_entry.delete(0, END)


def button_equal():
    second_number = my_entry.get()
    my_entry.delete(0, END)

    if math == "addition":
        my_entry.insert(0, first_num + int(second_number))
    if math == "substraction":
        my_entry.insert(0, first_num - int(second_number))
    if math == "multiplication":
        my_entry.insert(0, first_num * int(second_number))
    if math == "division":
        my_entry.insert(0, first_num / int(second_number))


# DEFINE THE BUTTONS

my_button7 = Button(root, text="7", padx=30, pady=10, font="calibri", command=lambda: button_click(7))
my_button8 = Button(root, text="8", padx=30, pady=10, font="calibri", command=lambda: button_click(8))
my_button9 = Button(root, text="9", padx=30, pady=10, font="calibri", command=lambda: button_click(9))
my_button_division = Button(root, text="/", padx=30, pady=10, font="calibri", command=button_division)

my_button4 = Button(root, text="4", padx=30, pady=10, font="calibri", command=lambda: button_click(4))
my_button5 = Button(root, text="5", padx=30, pady=10, font="calibri", command=lambda: button_click(5))
my_button6 = Button(root, text="6", padx=30, pady=10, font="calibri", command=lambda: button_click(6))
my_button_multiplication = Button(root, text="x", padx=30, pady=10, font="calibri", command=button_multiplicatin)

my_button1 = Button(root, text="1", padx=30, pady=10, font="calibri", command=lambda: button_click(1))
my_button2 = Button(root, text="2", padx=30, pady=10, font="calibri", command=lambda: button_click(2))
my_button3 = Button(root, text="3", padx=30, pady=10, font="calibri", command=lambda: button_click(3))
my_button_substraction = Button(root, text="-", padx=30, pady=10, font="calibri", command=button_substraction)

my_button00 = Button(root, text="00", padx=30, pady=10, font="calibri", command=lambda: button_click("00"))
my_button0 = Button(root, text="0", padx=30, pady=10, font="calibri", command=lambda: button_click(0))
my_button_dot = Button(root, text=".", padx=30, pady=10, font="calibri", command=lambda: button_click("."))
my_button_addition = Button(root, text="+", padx=30, pady=10, font="calibri", command=button_add)

my_button_equal = Button(root, text="=", padx=75, pady=8, font="calibri", bg="lightgreen", activebackground="green",
                         command=button_equal)
my_button_clear = Button(root, text="Clear", padx=75, pady=8, font="calibri", bg="pink", activebackground="red",
                         command=button_clear)

# BUTTON ON THE SCREEN

my_button7.grid(row=1, column=0)
my_button8.grid(row=1, column=1)
my_button9.grid(row=1, column=2)
my_button_division.grid(row=1, column=3)

my_button4.grid(row=2, column=0)
my_button5.grid(row=2, column=1)
my_button6.grid(row=2, column=2)
my_button_multiplication.grid(row=2, column=3)

my_button1.grid(row=3, column=0)
my_button2.grid(row=3, column=1)
my_button3.grid(row=3, column=2)
my_button_substraction.grid(row=3, column=3)

my_button00.grid(row=4, column=0)
my_button0.grid(row=4, column=1)
my_button_dot.grid(row=4, column=2)
my_button_addition.grid(row=4, column=3)

my_button_clear.grid(row=5, column=0, columnspan=2)
my_button_equal.grid(row=5, column=2, columnspan=2)

root.mainloop()

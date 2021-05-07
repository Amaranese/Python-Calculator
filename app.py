from tkinter import *
import parser
root = Tk()
root.title("Calculator")
# Input Fields
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)
# Get Numbers to Display
i = 0
def get_numbers(n):
    global i
    display.insert(i, n)
    i += 1
def get_operation(operator):
    global i
    opertor_length = len(operator)
    display.insert(i, operator)
    i+=opertor_length
def calculate():
    display_state = display.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        clear_display()
        display.insert(0, result)
    except Exception:
        clear_display()
        display.insert(0, 'Error')
def clear_display():
    display.delete(0, END)
def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, 'Error')
# Numeric Buttons
Button(root, text="1", command=lambda: get_numbers(1)).grid(row=2, column=0)
Button(root, text="2", command=lambda: get_numbers(2)).grid(row=2, column=1)
Button(root, text="3", command=lambda: get_numbers(3)).grid(row=2, column=2)
Button(root, text="4", command=lambda: get_numbers(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda: get_numbers(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda: get_numbers(6)).grid(row=3, column=2)
Button(root, text="7", command=lambda: get_numbers(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda: get_numbers(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda: get_numbers(9)).grid(row=4, column=2)
# Bottom Buttons
Button(root, text="AC", command=lambda: clear_display()).grid(row=5, column=0)
Button(root, text="0", command=lambda: get_numbers(0)).grid(row=5, column=1)
Button(root, text="%", command=lambda: get_operation("%")).grid(row=5, column=2)
Button(root, text="+", command=lambda: get_operation("+")).grid(row=2, column=3)
Button(root, text="-", command=lambda: get_operation("-")).grid(row=3, column=3, sticky=W+E)
Button(root, text="*", command=lambda: get_operation("*")).grid(row=4, column=3, sticky=W+E)
Button(root, text="/", command=lambda: get_operation("/")).grid(row=5, column=3, sticky=W+E)
# More Math Operators
Button(root, text="⟵", command=lambda: undo()).grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(root, text="exp", command=lambda: get_operation("**")).grid(row=3, column=4)
Button(root, text="^2", command=lambda: get_operation("**2")).grid(row=3, column=5)
Button(root, text="(", command=lambda: get_operation("(")).grid(row=4, column=4,sticky=W+E)
Button(root, text=")", command=lambda:get_operation(")")).grid(row=4, column=5, sticky=W+E)
Button(root, text="=", command=lambda: calculate()).grid(row=5, column=4, sticky=W+E, columnspan=2)
root.mainloop()
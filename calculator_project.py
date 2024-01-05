import tkinter as tk
import math

#left blank as users input something, if something was inputted, a would be in front of it!#
calculation = ""

#function to add something to calculation, add a symbol to this, it would add something in the input, it would also be converted to a string
#this is also a global function as it is to be used outside the scope of this function
#insert/delete within the 1.0 range (first line of the GUI)
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

#gloal function for the calculation of the calculatior, this prints the calculation as mentioned prior up front
# if else for sin and cos, use the math library to calculate the sine or cos of a number#
# use "EVAL" method to evaluate everything, and convert it into a string 
def evaluate_calculation():
    global calculation
    print(calculation) 
    try:
        if "sin" in calculation:
            angle_in_degrees = float(calculation.replace("sin", ""))
            result = math.sin(math.radians(angle_in_degrees))

        elif "cos" in calculation:
            angle_in_degrees =float(calculation.replace("cos", ""))
            result = math.cos(math.radians(angle_in_degrees))
        else:
            result = str(eval(calculation))
        
        calculation = str(result)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except Exception as e:
        print(f"Error: {e}")
        clear_field()
        text_result.insert("1.0", "Error")

#function to clear everything
def clear_field():
    global calculation 
    calculation = ""
    text_result.delete(1.0, "end")

#design for the calculator GUI, font, size, height and width, and colspan
root = tk.Tk()
root.geometry("600x500")
text_result = tk.Text(root, height=1.5, width=32, font=("Arial", 24))
text_result.grid(columnspan=10)

#ALL the buttons are here, what each button outputs, what it adds to a calculation, size of a button and font, and ALSO, the row, col pos of the btn
btn_1 = tk.Button(root, text="1", command = lambda: add_to_calculation(1), width = 5, font = ("Arial", 25))
btn_1.grid(row =2, column = 1)

btn_2 = tk.Button(root, text="2", command = lambda: add_to_calculation(2), width = 5, font = ("Arial", 25))
btn_2.grid(row =2, column = 2)

btn_3 = tk.Button(root, text="3", command = lambda: add_to_calculation(3), width = 5, font = ("Arial", 25))
btn_3.grid(row =2, column = 3)

btn_4 = tk.Button(root, text="4", command = lambda: add_to_calculation(4), width = 5, font = ("Arial", 25))
btn_4.grid(row =3, column = 1)

btn_5 = tk.Button(root, text="5", command = lambda: add_to_calculation(5), width = 5, font = ("Arial", 25))
btn_5.grid(row =3, column = 2)

btn_6 = tk.Button(root, text="6", command = lambda: add_to_calculation(6), width = 5, font = ("Arial", 25))
btn_6.grid(row =3, column = 3)

btn_7 = tk.Button(root, text="7", command = lambda: add_to_calculation(7), width = 5, font = ("Arial", 25))
btn_7.grid(row =4, column = 1)

btn_8 = tk.Button(root, text="8", command = lambda: add_to_calculation(8), width = 5, font = ("Arial", 25))
btn_8.grid(row =4, column = 2)

btn_9 = tk.Button(root, text="9", command = lambda: add_to_calculation(9), width = 5, font = ("Arial", 25))
btn_9.grid(row =4, column = 3)

btn_0 = tk.Button(root, text="0", command = lambda: add_to_calculation(0), width = 5, font = ("Arial", 25))
btn_0.grid(row =5, column = 2)

btn_plus = tk.Button(root, text="+", command = lambda: add_to_calculation("+"), width = 5, font = ("Arial", 25))
btn_plus.grid(row =2, column = 4)

btn_minus = tk.Button(root, text="-", command = lambda: add_to_calculation("-"), width = 5, font = ("Arial", 25))
btn_minus.grid(row =3, column = 4)

btn_mul = tk.Button(root, text="*", command = lambda: add_to_calculation("*"), width = 5, font = ("Arial", 25))
btn_mul.grid(row =4, column = 4)

btn_div = tk.Button(root, text="/", command = lambda: add_to_calculation("/"), width = 5, font = ("Arial", 25))
btn_div.grid(row =5, column = 4)

btn_open = tk.Button(root, text="(", command = lambda: add_to_calculation("("), width = 5, font = ("Arial", 25))
btn_open.grid(row =5, column = 1)

btn_close = tk.Button(root, text=")", command = lambda: add_to_calculation(")"), width = 5, font = ("Arial", 25))
btn_close.grid(row =5, column = 3)

btn_clr = tk.Button(root, text="clr", command= clear_field, width=5, font=("Arial", 25))
btn_clr.grid(row=6, column=1)

btn_eql = tk.Button(root, text="=", command = evaluate_calculation, width = 5, font = ("Arial", 25))
btn_eql.grid(row =6, column = 2)

btn_sin = tk.Button(root, text="sin", command = lambda: add_to_calculation("sin"), width = 5, font = ("Arial", 25))
btn_sin.grid(row =6, column = 3)

btn_cos = tk.Button(root, text="cos", command = lambda: add_to_calculation("cos"), width = 5, font = ("Arial", 25))
btn_cos.grid(row =6, column = 4)



root.mainloop()

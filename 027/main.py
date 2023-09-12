#######################################
# CLASS PROJECT
# Miles to Kilometers Converter
#######################################

# Day 27 - Miles to Kilometers Converter #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

from tkinter import *

window = Tk()
window.title("mi2km")
# window.minsize(width=300, height=150)
window.config(padx=50, pady=50)


# Component Definition


# Functions
def miles_to_km():
    miles = input_miles.get()
    if miles != "":
        km = round(float(miles) * 1.609344)
        label_result_km.config(text=f"{km}")


# input
input_miles = Entry(width=7)

# labels
label_miles = Label(text="Miles")
label_km = Label(text="KM")
label_result_km = Label(text="0")
label_is_equal = Label(text="is equal to")

# button
btn_calculate = Button(text="Calculate", command=miles_to_km)


# Layout
input_miles.grid(column=1, row=0)
label_miles.grid(column=2, row=0)
label_is_equal.grid(column=0, row=1)
label_result_km.grid(column=1, row=1)
label_km.grid(column=2, row=1)
btn_calculate.grid(column=1, row=2)


window.mainloop()

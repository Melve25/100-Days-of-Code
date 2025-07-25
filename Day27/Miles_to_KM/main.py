from tkinter import *


def calculate():
    km = int(user_input.get()) * 1.60934
    label_converted.config(text=round(km, 1))


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady=20)

user_input = Entry()
user_input.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)
label_equal_text = Label(text=f"is equal to")
label_equal_text.grid(column=0, row=1)
label_converted = Label(text="0")
label_converted.grid(column=1, row=1)
label_km_text = Label(text="Km")
label_km_text.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()

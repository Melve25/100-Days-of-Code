from tkinter import *


def button_clicked():
    label.config(text=user_input.get())


# Starter window itself
window = Tk()
window.title("My firs GUI program")
window.minsize(height=300, width=500)
window.config(padx=20, pady=20)

# Label
label = Label(text="I Am a Label", font=("Arial", 24))
# label.pack() takes "side=" arg which is a string like "right", "left", "bottom", "top"
# label.place(x=200, y=0) - same as pack but takes coordinates
label.grid(column=0, row=0)  # columns nad rows doesn't matter until there are other elements placed grid like
label.config(padx=20, pady=20)

label["text"] = "New Text"
label.config(text="New Text")

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=2, row=2)
new_button = Button(text="Click me new")
new_button.grid(column=3, row=0)


# Entry
user_input = Entry(width=30)
user_input.grid(column=4, row=4)

# Loop to make everything work, otherwise window will not appear
window.mainloop()

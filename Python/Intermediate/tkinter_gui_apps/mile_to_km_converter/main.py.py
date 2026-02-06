from tkinter import *

# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=160)

# Entry
input = Entry(width=8, font=("Fira Code", 13))
input.grid(column=5, row=1)

# Miles Label
miles_label = Label(text="Miles", font=("Fira Code", 10), padx=8)
miles_label.grid(column=6, row=1)

# Another Label
is_equal_label = Label(text="is equal to", font=("Fira Code", 10), padx=17, pady=5, )
is_equal_label.grid(column=4, row=2)

# Calculated Km Label
value_label = Label(text="0")
value_label.grid(column=5, row=2)

# Km Label
km_label = Label(text="Km", font=("Fira Code", 10),pady=5)
km_label.grid(column=6, row=2)

# Calculate Button
def km():
    user = float(input.get())
    km = str(round(user * 1.60934))
    value_label.config(text=km)

cal_button = Button(text="Calculate", width=9, command=km)
cal_button.grid(column=5, row=3)


# Temp Label for Space
label = Label(text="")
label.grid(column=0, row=0)

window.mainloop()
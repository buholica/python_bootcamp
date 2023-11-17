from tkinter import *


def calculate():
    km = float(miles_input.get()) * 1.609344
    result_label["text"] = round(km, 2)


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)

# Labels
miles_label = Label(text="Miles", font=("Arial", 14))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 14))
equal_label.grid(column=0, row=1)

km_label = Label(text="Km", font=("Arial", 14))
km_label.grid(column=2, row=1)

result_label = Label(text="0", font=("Arial", 14))
result_label.grid(column=1, row=1)

#Input
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
miles_input.insert(END, string="0")

#Button
calculate_bt = Button(text="Calculate", command=calculate)
calculate_bt.grid(column=1, row=2)

window.mainloop()
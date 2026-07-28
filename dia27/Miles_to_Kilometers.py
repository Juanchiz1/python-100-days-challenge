from tkinter import *

from dia27.PlayGround import calculate

window=Tk()
window.title("Miles to Kilometers Converter")
window.geometry("280x100")
window.config(padx=20, pady=20)

def miles_to_km():
    miles=float(miles_input.get())
    km=miles*1.60934
    km_result_label.config(text=f"{km}")


miles_input=Entry()
miles_input.grid(row=0,column=1)

miles_label= Label(text="Miles")
miles_label.grid(row=0,column=2)

is_equal_label=Label(text="Is Equal")
is_equal_label.grid(row=1,column=0)

km_result_label=Label(text="0")
km_result_label.grid(row=1,column=1)
km_label=Label(text="Kilometers")
km_label.grid(row=2,column=1)

calculate_button=Button(text="Calculate",command=miles_to_km)
calculate_button.grid(row=1,column=2)







window.mainloop()
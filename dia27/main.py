import tkinter as tk

window=tk.Tk()
window.title("FIRST GUI PROGRAM")
window.minsize(500, 300)
my_label=tk.Label(window, text="Student Name",font=("Arial",20,"bold"))
my_label.pack()

#Entry
input= tk.Entry(width=40)
input.pack()

def button_clicked():
    print("Button was clicked")
    my_label.config(text=input.get())

button=tk.Button(text="Click Me",command=button_clicked)
button.pack()

















window.mainloop()
import math
from tkinter import *

from fontTools.designspaceLib.statNames import BOLD_ITALIC_TO_RIBBI_STYLE

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    count_down(work_sec)
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=GREEN)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=RED)






# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"



    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
        check_mark.config(text=marks)







#UI SET UP ---------------------------------------------------
window=Tk()
window.title("POMODORO")




title_label=Label(text="Timer",foreground=GREEN,background=YELLOW,font=(FONT_NAME,50))
title_label.grid(row=0,column=1)

canvas=Canvas(window,width=206,height=234,background=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(106,112,image=tomato)
canvas.grid(row=1,column=1)
timer_text=canvas.create_text(106,130,text="00:00",font=(FONT_NAME,30),fill="white")
window.config(padx=130,pady=55,bg=YELLOW)



start_botton=Button(text="START",highlightthickness=0,command=start_timer)
start_botton.grid(row=2,column=0)

reset_botton=Button(text="RESET",highlightthickness=0,command=reset_timer)
reset_botton.grid(row=2,column=2)

check_mark=Label(foreground=GREEN,background=YELLOW,font=(FONT_NAME,30))
check_mark.grid(row=3,column=1)



window.mainloop()
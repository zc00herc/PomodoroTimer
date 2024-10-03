from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    reps = 0
    label.config(text="Timer")
    checks.config(text="")
    start_button["state"]="normal"

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start_button["state"]="disabled"
    global reps
    reps += 1
    window.attributes("-topmost",True)
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_secs)
        label.config(text="Break",fg=RED)
        window.attributes("-topmost",False)
    elif reps % 2 == 0:
        countdown(short_break_secs)
        label.config(text="Break",fg=PINK)
        window.attributes("-topmost",False)
    else:
        countdown(work_secs)
        label.config(text="Work",fg=GREEN)
        window.attributes("-topmost",False)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for something in range(work_sessions):
            marks += CHECKMARK
        checks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(bg=YELLOW,padx=100,pady=50)
window.title("Pomodoro")

label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,"bold"))
label.grid(column=1,row=0)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text = "00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

checks = Label(fg=GREEN,bg=YELLOW)
checks.grid(column=1,row=3)

window.mainloop()

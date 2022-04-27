import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

laps = 0
tick_array = [""]
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global tick_array, laps
    window.after_cancel(timer)
    heading.config(text="Timer")
    tick_array = [""]
    tick_label.config(text="")
    laps = 0
    canvas.itemconfig(count_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def set_timer(count):
    global timer
    minitus = math.floor(count / 60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = f'0{seconds}'
    canvas.itemconfig(count_text, text=f'{minitus}:{seconds}')
    if count > 0:
        if not timer:
            timer = window.after(1000, set_timer, count - 1)
    else:
        start_timer()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    global laps, tick_array
    laps += 1
    if laps % 2 != 0:
        heading.config(text="WORKING", fg=GREEN)
        set_timer(WORK_MIN * 60)
    elif laps % 8 == 0:
        heading.config(text="Take A Long Brak", fg=PINK)
        set_timer(LONG_BREAK_MIN * 60)
    else:
        heading.config(text="Take A short Break", fg=RED)
        set_timer(SHORT_BREAK_MIN * 60)
    if laps % 9 == 0:
        tick_array = [""]
    elif laps % 2 == 0:
        tick_array.append("✓")
    tick_label.config(text="".join(tick_array))
    tick_label.pack()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

heading = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 20, "bold"))
heading.pack()

bg = PhotoImage(file="tomato.png")
canvas = Canvas(width=210, height=250, bg=YELLOW, highlightthickness=0)
canvas.create_image(103, 130, image=bg)
canvas.pack()

count_text = canvas.create_text(103, 142, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.pack()

button_frame = Frame(window, bg=YELLOW, highlightthickness=0)
button_frame.pack(fill=X)

tick_label = Label(text='', bg=YELLOW, highlightthickness=0, fg=GREEN, font=(FONT_NAME, 15, "bold"))
start_button = Button(button_frame, bg="white", text="start", command=start_timer, highlightthickness=0)
start_button.pack(side="left")

reset_button = Button(button_frame, bg="white", text="reset", command=reset_timer, highlightthickness=0)
reset_button.pack(side="right")

window.mainloop()

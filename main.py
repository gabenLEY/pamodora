from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_s = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work_s)
        title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(cnt):
    cnt_min = math.floor(cnt / 60)
    cnt_s = cnt % 60

    if cnt_s < 10:
        cnt_s = f"0{cnt_s}"

    canvas.itemconfig(timer_text, text=f"{cnt_min}:{cnt_s}")
    print(cnt)
    if cnt > 0:
        global timer
        timer = window.after(1000, count_down, cnt - 1)
    else:
        start_timer()
        mark = ""
        work_ses = math.floor(reps / 2)
        for _ in range(work_ses):
            mark += "✔️"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 20, 'bold'), bg=YELLOW)
title.grid(column=2, row=0)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=1)

btn_start = Button(text="Start", bg="green", fg="white", command=start_timer)
btn_start.grid(column=1, row=3)

btn_start = Button(text="Reset", bg="red", fg="white", command=reset_timer)
btn_start.grid(column=3, row=3)

check = Label(fg="green", bg=YELLOW, font=20)
check.grid(column=2, row=3)
window.mainloop()

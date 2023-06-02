import tkinter
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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    global reps
    window.after_cancel(timer)
    reps = 0
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_list.clear()
    checkmark.config(text="".join(checkmark_list))


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = round(LONG_BREAK_MIN * 60) * 2

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)

    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text="%02d:%02d" % (count_min, count_sec))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            add_checkmark()
            checkmark.config(text="".join(checkmark_list))


# ---------------------------- UI SETUP ------------------------------- #
checkmark_list = []
def add_checkmark():
    checkmark_list.append("✔")
    # checkmark_text = "".append(checkmarks)


window = tkinter.Tk()
# window.minsize(width=400, height=300)
window.title("My Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tkinter.Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(row=1, column=2)

canvas = tkinter.Canvas()
canvas.config(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(102, 130, text=f"00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canvas.grid(row=2, column=2)

start_button = tkinter.Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(row=3, column=1)

reset_button = tkinter.Button(text="reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=3, column=3)

checkmark = tkinter.Label(bg=YELLOW, fg=GREEN)
checkmark.grid(row=4, column=2)

window.mainloop()

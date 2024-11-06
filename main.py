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
reps = 0
timer = None
marks = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(text_canvas, text="00:00")
    title_label.config(text="TIMER")
    tick_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global reps
  reps += 1
  global  marks
  work_sec = WORK_MIN*60
  short_break_secs = SHORT_BREAK_MIN * 60
  long_break_secs = LONG_BREAK_MIN * 60
  #if its 1st, 3rd,5th,7th rep
  if reps % 8 == 0:
      countdown_timer(long_break_secs)
      title_label.config(text = "LONG BREAK", fg= RED)
  elif reps % 2 == 0:
      countdown_timer(short_break_secs)
      title_label.config(text="SHORT BREAK", fg=PINK)
  else:
      title_label.config(text="WORK TIMER", fg=GREEN)
      countdown_timer(work_sec)
      marks += "✅"
      tick_label.config(text= marks)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import math
def countdown_timer(count):
  global timer
  timer_mins = math.floor(count / 60)
  timer_secs = count % 60
  canvas.itemconfig(text_canvas, text=f"{timer_mins}:{timer_secs}")
  if count > 0:
   timer = window.after(10,countdown_timer,count-1)
  else:
       start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

title_label = Label(window,bg=YELLOW,font=(FONT_NAME,50,"bold"))
title_label.grid(column=1,row=0)

canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image = tomato_img)
text_canvas = canvas.create_text(104,130,text="00:00",fill="white",font=("Courier",35,"bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="Start", command= start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", command= reset_timer)
reset_button.grid(column=2,row=2)

tick_label = Label(fg=GREEN,bg=YELLOW)
tick_label.grid(column=1,row=2)



if __name__ == "__main__":
 window.mainloop()
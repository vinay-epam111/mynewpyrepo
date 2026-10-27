import tkinter as tk
from datetime import datetime


def update_clock() -> None:
    now = datetime.now()
    time_label.config(text=now.strftime("%H:%M:%S"))
    date_label.config(text=now.strftime("%A, %B %d, %Y"))
    root.after(1000, update_clock)


root = tk.Tk()
root.title("Digital Clock")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

time_label = tk.Label(
    root,
    font=("Segoe UI", 48, "bold"),
    bg="#1e1e1e",
    fg="#ffffff",
)
time_label.pack(padx=30, pady=(25, 5))

date_label = tk.Label(
    root,
    font=("Segoe UI", 14),
    bg="#1e1e1e",
    fg="#b0b0b0",
)
date_label.pack(padx=30, pady=(0, 25))

update_clock()
root.mainloop()

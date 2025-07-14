import tkcalendar
import tkinter as tk
from dateutil import parser
from logic.logic import date_logic

# Main GUI window
root = tk.Tk()
root.title("test window")
root.geometry("1080x720")
helv_font=("Helvetica", 8, "bold")
root.config(bg="#FFFDD0")

# Adding a calendar date selector
calendar = tkcalendar.Calendar()
calendar.pack()

# Life grid view
grid_frame = tk.Frame(root)
grid_frame.pack(padx=30, pady=30)
grid_frame.config(bg="#f0f0f0")

for i in range(100):
    cols = 10
    row = i // cols
    col = i % cols
    week_button = tk.Button(grid_frame, text=f"{i}", width=4, height=2, font=helv_font)
    week_button.config(bg="white", fg="gray", activebackground="gray", relief="flat")
    week_button.grid(column=col, row=row, padx=5, pady=5)

# Button pressed function + Button component
def button_clicked():
    birthdate = parser.parse(calendar.get_date())
    print(birthdate.strftime('%d/%m/%Y'))
    date_logic(birthdate)
    calendar.destroy()
    
    
test_button = tk.Button(root, text="click me please", command=button_clicked)
test_button.pack(pady=100)


root.mainloop()
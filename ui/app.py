import tkcalendar
import tkinter as tk
from dateutil import parser
from logic import date_logic

root = tk.Tk()
root.title("test window")
root.geometry("500x500")

def button_clicked():
    birthdate = parser.parse(calendar.get_date())
    print(birthdate.strftime('%d/%m/%Y'))
    date_logic(birthdate)
    
calendar = tkcalendar.Calendar()
calendar.pack()

test_button = tk.Button(root, text="click me please", command=button_clicked)
test_button.pack(pady=100)

root.mainloop()
import tkinter as tk
from datetime import datetime, date

def get_days_word(n):
    n = abs(n)
    if n % 10 == 1 and n % 100 != 11:
        return "день"
    elif n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14]:
        return "дня"
    else:
        return "дней"

root = tk.Tk()
root.title("Что мне делать, как мне жить?")
root.geometry("650x550")
root.configure(bg="black")

title_label = tk.Label(
    root, 
    text="Мои текущие задачи", 
    font=("Arial", 22, "underline bold"), 
    fg="yellow", 
    bg="black"
)
title_label.pack(pady=25)

frame = tk.Frame(root, bg="black")
frame.pack(fill="both", expand=True, padx=50)

today = date.today()

try:
    with open("tasks.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.strip()
        if not line or ";" not in line:
            continue
            
        date_str, task_name = line.split(";", 1)
        task_date = datetime.strptime(date_str, "%d.%m.%Y").date()
        delta = (today - task_date).days
        
        if delta > 0:
            days_word = get_days_word(delta)
            text_to_show = f"Прошло {delta} {days_word} от {task_name}"
            color = "red"
            
        elif delta == 0:
            text_to_show = f"Прямо щас происходит {task_name}"
            color = "yellow"
            
        else:
            days_left = abs(delta)
            days_word = get_days_word(days_left)
            
            if days_left % 10 == 1 and days_left % 100 != 11:
                left_word = "Остался"
            else:
                left_word = "Осталось"
                
            text_to_show = f"{left_word} {days_left} {days_word} до {task_name}"
            color = "white"
        
        lbl = tk.Label(
            frame, 
            text=text_to_show, 
            font=("Arial", 13), 
            fg=color, 
            bg="black", 
            anchor="w"
        )
        lbl.pack(fill="x", pady=4)

except FileNotFoundError:
    error_lbl = tk.Label(
        frame, 
        text="Ошибка: Файл tasks.txt не найден!", 
        font=("Arial", 14), 
        fg="red", 
        bg="black"
    )
    error_lbl.pack(pady=20)

root.mainloop()

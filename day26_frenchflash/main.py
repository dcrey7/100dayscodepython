from tkinter import *
import pandas
import random
from datetime import datetime
import os
import time
import pandas as pd
import openpyxl

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    with open(r"day26_frenchflash/data/highscore.txt") as data:
            high_score = int(data.read())
except FileNotFoundError:
    with open(r"day26_frenchflash/data/highscore.txt", mode="w") as data:
                data.write("0")

with open(r"day26_frenchflash/data/highscore.txt") as data:
        high_score = int(data.read())


try:
    data = pandas.read_csv(r"day26_frenchflash/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(r"day26_frenchflash/data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer , score, high_score
    if score > high_score:
            high_score = score
            with open(r"day26_frenchflash/data/highscore.txt", mode="w") as data:
                data.write(f"{high_score}")
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(high_title, text=f"High score: {high_score}", fill="blue")
    canvas.itemconfig(score_title, text=f"Score: {score}", fill="green")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    global score
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv(r"day26_frenchflash/data/words_to_learn.csv", index=False)
    score+=1
    next_card()

start_quiz_time = time.time()

score=0
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=675)
card_front_img = PhotoImage(file=r"day26_frenchflash/images/card_front.png")
card_back_img = PhotoImage(file=r"day26_frenchflash/images/card_back.png")
card_background = canvas.create_image(400, 375, image=card_front_img)
card_title = canvas.create_text(400, 275, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 375, text="", font=("Ariel", 60, "bold"))
high_title = canvas.create_text(400, 25, text="", font=("Ariel", 35, "bold"))
score_title = canvas.create_text(400, 75, text="", font=("Ariel", 30))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file=r"day26_frenchflash/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file=r"day26_frenchflash/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()


window.mainloop()
end_quiz_time = time.time()
total_time = end_quiz_time - start_quiz_time

file_name = r'day26_frenchflash/data/dailyfrench_results.xlsx'
if os.path.exists(file_name):
    existing_results = pd.read_excel(file_name)
    final_results = pd.DataFrame({
        'Datetime': [datetime.now()],
        'Final_Score': [score],
        'High_Score': [high_score],
        'Total_Time': [round((total_time/60),2)]
    })
    updated_results = pd.concat([existing_results, final_results], ignore_index=True)
    updated_results.to_excel(file_name, index=False, header=True)
else:
    final_results = pd.DataFrame({
        'Datetime': [datetime.now()],
        'Final_Score': [score],
        'High_Score': [high_score],
        'Total_Time': [round((total_time/60),2)]
    })
    final_results.to_excel(file_name, index=False, header=True)
    print(f"Results exported to '{file_name}'")



print(f"\n ********* Todays  is {datetime.now()}**************")
print(f"\nYour final score for the day is {score}")
print(f"Total time taken to complete the quiz: {round((total_time/60),2):.2f} seconds")
    



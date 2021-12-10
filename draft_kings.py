from bs4 import BeautifulSoup
import requests
from tkinter import *
import pandas as pd
from PIL import Image, ImageTk

BACKGROUND_COLOR = "#B4C6A6"
response = requests.get("https://sportsbook.draftkings.com/leagues/basketball/88670846")
draft_kings_list = response.text
soup = BeautifulSoup(draft_kings_list, "html.parser")
matchup = soup.find_all("div", class_="event-cell__name-text")

game_day_matches = []
spreads = []
all_odds = []
all_scores = []
for matches in matchup:
    matchups = matches.getText()
    game_day_matches.append(matchups)
spread = soup.find_all("span", class_="sportsbook-outcome-cell__line")
for sp in spread:
    game_day_spreads = sp.getText()
    spreads.append(game_day_spreads)

odds = soup.find_all("span", class_="sportsbook-odds american no-margin default-color")
for odd in odds:
    game_day_odds = odd.getText()
    all_odds.append(game_day_odds)
scores = soup.find_all("span", class_="event-cell__score")
for score in scores:
    game_score = score.getText()
    all_scores.append(game_score)

    # print(game_day_matches)
final_spreads = spreads[::2]
# print(all_odds)

vals = zip(final_spreads, all_odds)
dictionary = dict(zip(game_day_matches, vals))

data = pd.DataFrame(dictionary)
pd.set_option('display.max_columns', None)
diction = list(data)

df = data.columns.to_frame().T.append(data, ignore_index=True)
df.columns = range(len(df.columns))

# UI setup
window = Tk()
window.title("Gamble the odds")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=600)
nba_img = ImageTk.PhotoImage(Image.open("nba goat.JPG"))
football_img = PhotoImage(file="nfl goats.png")
img_background = canvas.create_image(400, 263, image=nba_img)
title = canvas.create_text(400, 30, text="Today's Games", font=("Ariel", 20, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


# def teams():
#     team_1 = df[0][0]
#     team_2 = df[1][0]
#     team_3 = df[2][0]
#     team_4 = df[3][0]
#     team_5 = df[4][0]
#     team_6 = df[5][0]
#     team_7 = df[6][0]
#     team_8 = df[7][0]
#     team_9 = df[8][0]
#     team_10 = df[9][0]
#     team_11 = df[10][0]
#     team_12 = df[11][0]
#     return teams


# def find_team_spreads():
#     team_1_spreads = df[0][1]
#     team_2_spreads = df[1][1]
#     team_3_spreads = df[2][1]
#     team_4_spreads = df[3][1]
#     team_5_spreads = df[4][1]
#     team_6_spreads = df[5][1]
#     team_7_spreads = df[6][1]
#     team_8_spreads = df[7][1]
#     team_9_spreads = df[8][1]
#     team_10_spreads = df[9][1]
#     team_11_spreads = df[10][1]
#     team_12_spreads = df[11][1]
#     return find_team_spreads


# def money():
#     team_1_moneyline = df[0][2]
#     team_2_moneyline = df[1][2]
#     team_3_moneyline = df[2][2]
#     team_4_moneyline = df[3][2]
#     team_5_moneyline = df[4][2]
#     team_6_moneyline = df[5][2]
#     team_7_moneyline = df[6][2]
#     team_8_moneyline = df[7][2]
#     team_9_moneyline = df[8][2]
#     team_10_moneyline = df[9][2]
#     team_11_moneyline = df[10][2]
#     team_12_moneyline = df[11][2]
#     return money


def games():
    game_1 = Label(text=f"{df[0][0]}\n vs. \n{df[1][0]}", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    game_1.place(x=100, y=75)
    game_2 = Label(text=f"{df[2][0]}\n vs. \n{df[3][0]}", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    game_2.place(x=100, y=135)
    game_3 = Label(text=f"{df[4][0]}\n vs. \n{df[5][0]}", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    game_3.place(x=100, y=190)
    game_4 = Label(text=f"{df[6][0]}\n vs. \n{df[7][0]}", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    game_4.place(x=100, y=245)
    game_5 = Label(text=f"{df[8][0]}\n vs. \n{df[9][0]}", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    game_5.place(x=100, y=300)
    game_6 = Label(text=f"{df[10][0]}\n vs. \n{df[11][0]}", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    game_6.place(x=100, y=355)

    return games


def team_spread():
    team_1_spread = Label(text=f"{df[0][1]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_1_spread.place(x=300, y=75)
    team_2_spread = Label(text=f"{df[1][1]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_2_spread.place(x=300, y=105)
    team_3_spread = Label(text=f"{df[2][1]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_3_spread.place(x=300, y=137)
    team_4_spread = Label(text=f"{df[3][1]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_4_spread.place(x=300, y=167)
    team_5_spread = Label(text=f"{df[4][1]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_5_spread.place(x=300, y=195)
    team_6_spread = Label(text=f"{df[5][1]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_6_spread.place(x=300, y=220)
    team_7_spread = Label(text=f"{df[6][1]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_7_spread.place(x=300, y=250)
    team_8_spread = Label(text=f"{df[7][1]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_8_spread.place(x=300, y=275)
    team_9_spread = Label(text=f"{df[8][1]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_9_spread.place(x=300, y=300)
    team_10_spread = Label(text=f"{df[9][1]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_10_spread.place(x=300, y=330)
    team_11_spread = Label(text=f"{df[10][1]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_11_spread.place(x=300, y=355)
    team_12_spread = Label(text=f"{df[11][1]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_12_spread.place(x=300, y=385)
    return team_spread

def gameday_scores():
    team_1_scores = Label(text=f"{all_scores[0]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_1_scores.place(x=200, y=75)
    team_2_scores = Label(text=f"{all_scores[1]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_2_scores.place(x=200, y=105)
    team_3_scores = Label(text=f"{all_scores[3]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_3_scores.place(x=200, y=137)
    team_4_scores = Label(text=f"{all_scores[4]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_4_scores.place(x=200, y=167)
    team_5_scores = Label(text=f"{all_scores[5]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_5_scores.place(x=200, y=195)
    team_6_scores = Label(text=f"{all_scores[6]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_6_scores.place(x=200, y=220)
    team_7_scores = Label(text=f"{all_scores[7]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_7_scores.place(x=200, y=250)
    team_8_scores = Label(text=f"{all_scores[8]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_8_scores.place(x=200, y=275)
    team_9_scores = Label(text=f"{all_scores[9]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_9_scores.place(x=200, y=300)
    team_10_scores = Label(text=f"{all_scores[10]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_10_scores.place(x=200, y=330)
    team_11_scores = Label(text=f"{all_scores[11]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_11_scores.place(x=200, y=355)
    team_12_scores = Label(text=f"{all_scores[12]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_12_scores.place(x=200, y=385)
    return gameday_scores
def moneyline():
    team_1_money = Label(text=f"{df[0][2]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_1_money.place(x=500, y=75)
    team_2_money = Label(text=f"{df[1][2]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_2_money.place(x=500, y=105)
    team_3_money = Label(text=f"{df[2][2]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_3_money.place(x=500, y=130)
    team_4_money = Label(text=f"{df[3][2]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_4_money.place(x=500, y=160)
    team_5_money = Label(text=f"{df[4][2]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_5_money.place(x=500, y=190)
    team_6_money = Label(text=f"{df[5][2]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_6_money.place(x=500, y=220)
    team_7_money = Label(text=f"{df[6][2]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_7_money.place(x=500, y=250)
    team_8_money = Label(text=f"{df[7][2]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_8_money.place(x=500, y=275)
    team_9_money = Label(text=f"{df[8][2]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_9_money.place(x=500, y=300)
    team_10_money = Label(text=f"{df[9][2]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_10_money.place(x=500, y=330)
    team_11_money = Label(text=f"{df[10][2]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_11_money.place(x=500, y=365)
    team_12_money = Label(text=f"{df[11][2]} ", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR)
    team_12_money.place(x=500, y=400)
    return moneyline

canvas.create_line(30, 130, 770, 130, fill="white")
canvas.create_line(30, 190, 770, 190, fill="white")
canvas.create_line(30, 240, 770, 240, fill="white")
canvas.create_line(30, 300, 770, 300, fill="white")
canvas.create_line(30, 355, 770, 355, fill="white")
canvas.create_line(30, 410, 770, 410, fill="white")
spread_name = Label(text="Spread", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
spread_name.place(x=300, y=50)
money_label = Label(text="MoneyLine", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
money_label.place(x=500, y=50)
team_label = Label(text="Teams", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
team_label.place(x=100, y=50)
scores_label = Label(text="Scores", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
scores_label.place(x=200, y=50)
try:
    games()
except (KeyError, NameError):
    pass
try:
    moneyline()
except (ValueError,KeyError):
    pass
try:
    team_spread()
except (ValueError, KeyError):
    pass
try:
    gameday_scores()
except (ValueError, KeyError, IndexError):
    pass
    # print(diction)
    # print(data)
    # print(data)
    #


    #
    # def toggle_to_nfl():
    #     canvas.itemconfig(img_background, image=football_img)
    #
    # toggle_image = PhotoImage(file="right.png")
    # known_button = Button(image=toggle_image, highlightthickness=0, command=toggle_to_nfl)
    # known_button.grid(row=1, column=1)
    #
    #
    #
mainloop()

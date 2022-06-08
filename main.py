from bdb import Breakpoint
import random
from re import A
from tkinter import Y
from game_data import data
from art import logo, vs


win_count = 0
choice_b = random.choice(data)
is_continue = True
while is_continue:
    print(logo)
    choice_a = choice_b

    if choice_a == choice_b:
        choice_b = random.choice(data)

    choice_a_name = choice_a["name"]
    choice_a_descr = choice_a["description"]
    choice_a_country = choice_a["country"]

    choice_b_name = choice_b["name"]
    choice_b_descr = choice_b["description"]
    choice_b_country = choice_b["country"]
    # print(choice_a_name)
    print(f"You're right! Current score:  {win_count}")
    print(f"Compare A: {choice_a_name}, a {choice_a_descr}, from {choice_a_country}.")
    print(vs)
    print(f"Against B: {choice_b_name}, a {choice_b_descr}, from {choice_b_country}.")

    # print(choice_a)
    # print(choice_b)
    choice_a_followers = choice_a["follower_count"]
    choice_b_followers = choice_b["follower_count"]
    print(f"{choice_a_followers} ,{choice_b_followers}")
    choose = input("Who has more followers? Type 'A' or 'B': ").lower()

    if choose == "a":
        if choice_a_followers >= choice_b_followers:
            print("Correct")
        else:
            is_continue = False
            print(f"Sorry that's Wrong. Final score: {win_count}")
            # break
    elif choose == "b":
        if choice_a_followers >= choice_b_followers:
            is_continue = False
            print(f"Sorry that's Wrong. Final score: {win_count}")
            # break
        else:
            print("Correct")
    win_count += 1

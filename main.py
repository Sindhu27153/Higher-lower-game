import random
from replit import *
from game_data import data
from art import logo,vs



def get_account(data):
    return random.choice(data)

def format_data(account):
    name = account['name']
    description = account ['description']
    country = account['country']
    return f"{name},a {description} from {country}"


def check_answer(a_followers,b_followers,guess):
    if a_followers > b_followers:
        return guess =='a'
    else:
        return guess =='b'

def playgame():
    score = 0
    account_b = get_account(data)
    should_continue = True

    while should_continue:
        account_a = account_b
        account_b = get_account(data)
        if account_a == account_b:
            account_b.get_account(data)

        print(logo)

        print(f"compare A:{format_data(account_a)}.")
        print(vs)
        print(f"Against B:{format_data(account_b)}.")

        guess = input("Who has more Followers? Type A or B ").lower()

        print("\n" * 20)

        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']

        choose_answer = check_answer(a_follower_count,b_follower_count,guess)

        if choose_answer:
            score += 1
            print(f"your score is:{score}")

        else:
            should_continue=False
            print(f"sorry!your score is:{score}")



playgame()
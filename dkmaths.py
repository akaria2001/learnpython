from itertools import cycle
from time import sleep
import subprocess as cmd
import random
from pyfiglet import Figlet
import argparse
import pygame


def gen_number():
    return random.randint(1,10)


def print_yellow(text):
    custom_fig = Figlet(font='standard', width=180)
    print(f'\033[1;33m{custom_fig.renderText(text)}\033[0;0m')


def print_yellow_double(text):
    custom_fig = Figlet(font='big', width=180)
    print(f'\033[1;33m{custom_fig.renderText(text)}\033[0;0m')


def print_yellow_small(text):
    print(f'\033[1;33m{text}\033[0;0m')


def print_red(text):
    custom_fig = Figlet(font='standard', width=180)
    print(f'\033[1;31m{custom_fig.renderText(text)}\033[0;0m')


def print_green(text):
    custom_fig = Figlet(font='standard', width=180)
    print(f'\033[1;32m{custom_fig.renderText(text)}\033[0;0m')


def print_green_double(text):
    custom_fig = Figlet(font='big', width=180)
    print(f'\033[1;32m{custom_fig.renderText(text)}\033[0;0m')


def print_debug(text):
    custom_fig = Figlet(font='standard', width=180)
    print(f'\033[1;34m{custom_fig.renderText(text)}\033[0;0m')

def print_smiley(text):
    print(f'{text} \U0001F60F')


def print_folder():
    print('\U0001F4C1')


def print_tick(text):
    print(f'{text}\u2705')


def print_warning(text):
    print(f'\u274C\u274C\u274C\033[1;31m {text} \033[0;0m\u274C\u274C\u274C')


def print_picture():
    print_yellow_small("""

➕ ✖️️ ➖ ➗👨‍🏫📐🧪👨🏼‍💻🧑🏿‍🔬👨🏻‍🔬☣☀️
                       
.----------------------------------------------------------------------.
|_.-._.-._.-._.-._.-._.-.    _.-._.-._.-.    _.-._.-._.-._.-._.-._.-._.|
|_.-._.-._.-._.-._.-._. .::db .-._.-._. .::db .-._.-._.-._.-._.-._.-._.|
|_.-._.-._.-._.-._.-._ .::d88b -._.-._ .::d88b -._.-._.-._.-._.-._.-._.|
|_.-._.-._.-._.-._.-. .::d8888b       .::d8888b ._.-._.-._.-._.-._.-._.|
|_.-._.-._.-._.-._.- .::d88!::::::::::::d888888b _.-._.-._.-._.-._.-._.|
|_.-._.-._.-._.-._.- \  Y88\_________\  Y888888P _.-._.-._.-._.-._.-._.|
|_.-._.-._.-._.-._.-. \  Y8888P ._.-. \  Y8888P ._.-._.-._.-._.-._.-._.|
|_.-._.-._.-._.-._.-._ /dbY88Pdb _.-._ /dbY88Pdb _.-._.-._.-._.-._.-._.|
|_.-._.-._.-._.-._.-. /d8P_YP Y8b .-. /d8P_YP Y8b .-._.-._.-._.-._.-._.|
|_.-._.-._.-._.-     /d8P .-.\ Y8b   /d8P .- \ Y8b -._.-._.-._.-._.-._.|
|_.-._.-._.-._ .::db/d8P _.-. \.::db/d8P _.-. \ Y8b ._.-._.-._.-._.-._.|
|_.-._.-._.-. .::d88bYP ._.-. .::d88LSP ._.-._ \ Y8b    ._.-._.-._.-._.|
|_.-._.-._.- .::d8888b       .::d8888b`b _.-._. \ Y8b:db _.-._.-._.-._.|
|_.-._.-._. .::d88!::::::::::::d888888b`b .-._.- \ YPd88b .-._.-._.-._.|
|_.-._.-._. \  Y88\_________\  Y888888Pd8b       .::d8888b -._.-._.-._.|
|_.-._.-._.- \  Y8888P -._.- \  Y8888P!::::::::::::d888888b ._.-._.-._.|
|_.-._.-._.-. \  Y88Pdb ._.-. \  Y88Pdb_________\  Y888888P ._.-._.-._.|
|_.-._.-._.-._ \__YP Y8b _.-._ \__YP Y8b`P -._.- \  Y8888P -._.-._.-._.|
|_.-._.-._.-._.-._. \ Y8b .-._.-. /d\ Y8b .-._.-. /dbY88P .-._.-._.-._.|
|_.-._.-._.-._.-._.- \ Y8b -._.- /d8P\ Y8b -._.- /d8P_YP _.-._.-._.-._.|
|_.-._.-._.-._.-._.-. \ Y8b     /d8P _\ Y8b     /d8P _.-._.-._.-._.-._.|
|_.-._.-._.-._.-._.-._ \ Y8b:db/d8P ._ \ Y8b:db/d8P ._.-._.-._.-._.-._.|
|_.-._.-._.-._.-._.-._. \ YPd88bYP -._. \ YPd88bYP -._.-._.-._.-._.-._.|
|_.-._.-._.-._.-._.-._. .::d8888b       .::d8888b .-._.-._.-._.-._.-._.|
|_.-._.-._.-._.-._.-._ .::d88!::::::::::::d888888b -._.-._.-._.-._.-._.|
|_.-._.-._.-._.-._.-._ \  Y88\_________\  Y888888P -._.-._.-._.-._.-._.|
|_.-._.-._.-._.-._.-._. \  Y8888P .-._. \  Y8888P .-._.-._.-._.-._.-._.|
|_.-._.-._.-._.-._.-._.- \  Y88P _.-._.- \  Y88P _.-._.-._.-._.-._.-._.|
|_.-._.-._.-._.-._.-._.-. \__YP ._.-._.-. \__YP ._.-._.-._.-._.-._.-._.|
`----------------------------------------------------------------------'

                 """)


def spiner():
    count = 0
    for frame in cycle(r'-\|/'):
        count = count + 1
        print('\r', frame, sep='', end='', flush=True)
        sleep(0.1)
        if count > 65:
            break

def countdown_timer(timer_val_secs):
    for count in range(timer_val_secs, -1, -1):
        cmd.call('clear', shell=False)
        print_yellow(f"Countdown\nSeconds left : {count} ")
        sleep(1)


def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)


def display_score(score):
    print_green_double(f"Current Score : {score}")

# ToDO : Fix Scoring
def addition():
    counter = 1
    score = 0
    while (counter <= 10):
        print_yellow_double("DK School Quiz Addition Section")
        display_score(score)
        print_yellow_double(f"Addition Question {counter}")
        num1 = gen_number()
        num2 = gen_number()
        print_yellow_double(f"What is {num1} + {num2}? ")
        answer = num1 + num2
        user_answer = int(input())
        cmd.call("clear", shell=False)
        print_yellow(f"Your answered with {user_answer}")
        print_yellow(f"Correct Answer is {answer}")
        if(user_answer == answer):
            score = score + 1
        counter = counter +1
        sleep(3)
        cmd.call("clear",shell=False)
    print_green_double(f"You scored {score} out of 10, well done")


def subtraction():
    counter = 1
    score = 0
    while (counter <= 10):
        print_yellow_double("DK School Quiz Subtraction Section")
        display_score(score)
        print_yellow_double(f"Subtraction Question {counter}")
        num1 = gen_number()
        num2 = gen_number()
        print_yellow_double(f"What is {num1} - {num2}? ")
        answer = num1 - num2
        user_answer = int(input())
        cmd.call("clear", shell=False)
        print_yellow(f"Your answered with {user_answer}")
        print_yellow(f"Correct Answer is {answer}")
        if(user_answer == answer):
            score = score + 1
        counter = counter +1
        sleep(3)
        cmd.call("clear",shell=False)
    print_green_double(f"You scored {score} out of 10, well done")

def main():
    cmd.call("clear", shell=False)
    play_music()
    username = input("What is your name: ")
    print_green(f"Welcome onboard {username}")
    print_yellow("Welcome to DK School Quiz")
    print_smiley("by Devyani Karia")
    print_picture()
    print_smiley("We will get started soon ")
    spiner()
    cmd.call("clear", shell=False)
    print_yellow_double("Lets get started!!! ")
    sleep(3)
    cmd.call("clear", shell=False)
    addition()
    subtraction()
    


if __name__ == '__main__':
    main()

from itertools import cycle
from time import sleep
import subprocess as cmd
import random
from pyfiglet import Figlet
import argparse
import pygame


def print_yellow(text):
    custom_fig = Figlet(font='standard', width=160)
    print(f'\033[1;33m{custom_fig.renderText(text)}\033[0;0m')


def print_yellow_small(text):
    print(f'\033[1;33m{text}\033[0;0m')


def print_red(text):
    custom_fig = Figlet(font='standard', width=160)
    print(f'\033[1;31m{custom_fig.renderText(text)}\033[0;0m')


def print_green(text):
    custom_fig = Figlet(font='standard', width=160)
    print(f'\033[1;32m{custom_fig.renderText(text)}\033[0;0m')

def print_debug(text):
    custom_fig = Figlet(font='standard', width=160)
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


def main():
    cmd.call("clear", shell=False)
    play_music()
    print_yellow('Welcome to DK Maths Quiz')
    print_picture()
    print_smiley("We will get started soon ")
    spiner()
    countdown_timer(10)


if __name__ == '__main__':
    main()
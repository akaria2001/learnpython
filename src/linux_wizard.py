import subprocess as cmd
import getpass


def generate_username():
    username = getpass.getuser()
    return username


def print_yellow(text):
    print(f'\033[1;33m{text}\033[0;0m')


def print_red(text):
    print(f'\033[1;31m{text}\033[0;0m')


def print_green(text):
    print(f'\033[1;32m{text}\033[0;0m')


def main():
    cmd.call(['clear'], shell=False)
    print_yellow("Welcome to Linux Menu")
    print_red("Hello World")
    print_green("Written by Amit Karia www.it-howto.co.uk")


if __name__ == '__main__':
    main()

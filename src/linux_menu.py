import subprocess as cmd
import time
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


def print_blue(text):
    print(f'\033[1;34m{text}\033[0;0m')


def main():
    cmd.call("clear", shell=False)
    print_yellow(f"Hello {generate_username()}, welcome to Linux Menu")
    time.sleep(1)


if __name__ == '__main__':
    main()

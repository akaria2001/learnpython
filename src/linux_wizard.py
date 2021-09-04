import subprocess as cmd
import getpass
import time


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


cmd_list = ['ls -la',
            'df -h',
            'uname -r',
            'cat /etc/redhat-release']


def main():
    cmd.call(['clear'], shell=False)
    print_yellow(f"Hi {generate_username()}, Welcome to Linux Wizard")
    print_red("The wizard will setup your Linux Machine")
    print_green("Written by Amit Karia www.it-howto.co.uk")
    print_blue("Will run the folowing commands")
    for command in cmd_list:
        print_blue(command)
    time.sleep(2)

    for command in cmd_list:
        print_green(f"Running command: {command}")
        cmd.call(command.split(), shell=False)


if __name__ == '__main__':
    main()

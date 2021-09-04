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


def generate_menu():
    menu_items = [[1, 'OS Upgrade', 'sudo yum update -y'],
                  [2, 'Show Kernel Version', 'uname -r'],
                  [3, 'Show Disk Space', 'df -h']]
    return menu_items


def main():
    cmd.call("clear", shell=False)
    print_yellow(f"Hello {generate_username()}, welcome to Linux Menu")
    time.sleep(1)
    while(True):
        for menu_item in generate_menu():
            print_green(f"{menu_item[0]}: {menu_item[1]}")
        print_red("0: Exit Application")
        user_choice = int(input("Please select option : "))
        if user_choice == 0:
            exit()
        else:
            next


if __name__ == '__main__':
    main()

import subprocess as cmd
import time
import getpass
import platform

"""
Useful Links I referenced when writing this script

Printing Coloured text
https://stackabuse.com/how-to-print-colored-text-in-python/

Sub Process to call external commands
https://docs.python.org/3/library/subprocess.html

"""


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
                  [3, 'Show Disk Space', 'df -h'],
                  [4, 'Show Inode Usage', 'df -i'],
                  [5, 'Show OS and Version', 'cat /etc/redhat-release'],
                  [6, 'Show CPU Information', 'lscpu'],
                  [7, 'Show Memory Information', 'free -h'],
                  [8, 'Show Hardware Information', 'sudo lshw'],
                  [9, 'Show contents of current directory', 'ls -la']]
    return menu_items


def grab_os():
    osversion = "Unknown"
    try:
        with open("/etc/redhat-release") as file:
            osversion = file.read()
    except FileNotFoundError:
        print_red("Unable to detect OS Version")
        next
    return osversion.strip()


def main():
    cmd.call("clear", shell=False)
    time.sleep(1)
    while(True):
        print_yellow(f"Hello {generate_username()}, welcome to Linux Menu")
        print_blue(f"OS Version: {grab_os()}")
        print_blue(f"Python Version: {platform.python_version()}")
        for menu_item in generate_menu():
            print_green(f"{menu_item[0]}: {menu_item[1]}")
        print_red("0: Exit Application")
        try:
            user_choice = int(input("Please select option : "))
        except ValueError:
            print_red("Please enter a valid choice")
        if user_choice == 0:
            cmd.call("clear", shell=False)
            exit()
        else:
            for choice in generate_menu():
                if(user_choice == choice[0]):
                    print_blue(f"You have chosen : {choice[1]}")
                    print_blue(f"Will run command : '{choice[2]}'")
                    cmd.call(choice[2].split(), shell=False)
                    time.sleep(1)
                    input("Press any key to continue : ")
                    cmd.call("clear", shell=False)
                    break


if __name__ == '__main__':
    main()

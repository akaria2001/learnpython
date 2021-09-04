import subprocess as cmd
import getpass


def generate_username():
    username = getpass.getuser()
    return username


def main():
    cmd.call(['clear'], shell=False)
    print("Welcome to Linux Menu")


if __name__ == '__main__':
    main()

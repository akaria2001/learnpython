import subprocess as cmd
from pathlib import Path
import getpass


def get_home_dir():
    home = Path.home()
    return home


def get_username():
    username = getpass.getuser()
    return username


def main():
    cmd.call("clear", shell=False)
    print(f"Hello {get_username()} : home directory is {get_home_dir()}")


if __name__ == '__main__':
    main()

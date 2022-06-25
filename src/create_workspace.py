import shutil
import subprocess as cmd
from pathlib import Path
import getpass
import os
import time


def get_home_dir():
    home = Path.home()
    return home


def get_username():
    username = getpass.getuser()
    return username


def create_workspace():
    print("Changing to home directory")
    os.chdir(get_home_dir())
    cwd = os.getcwd()
    print(f"Current working directory is : {cwd}")
    workspace = f"{get_home_dir()}/workspaceAuto"
    print(f"Creating workspace {workspace}")
    mode = 0o766
    try:
        os.mkdir(workspace, mode)
    except FileExistsError:
        print(f"Workspace already exists at {workspace}")
        print("Will delete existing workspace and recreate it")
        shutil.rmtree(workspace, ignore_errors=True)
        os.mkdir(workspace, mode)
    os.chdir(workspace)
    for number in range(1, 21):
        icon = "\U0001F4C1"
        print(f"Creating directory in {workspace}/directory-{number} {icon}")
        os.mkdir(f"directory-{number}", mode)
        os.chdir(f"{workspace}/directory-{number}")
        for file in range(1, 11):
            print(f"Creating file-{file}.txt \u2705")
            open(f"file-{file}.txt", 'a').close()
            time.sleep(0.25)
        os.chdir(workspace)
    return os.listdir(workspace)


def main():
    workspace = f"{get_home_dir()}/workspaceAuto"
    cmd.call("clear", shell=False)
    emoji = "\U0001F60F"
    cmd.call("clear", shell=False)
    print(f"Hi {get_username()} {emoji} : home directory is {get_home_dir()}")
    print(f"Creating workspace at {workspace}")
    time.sleep(1)
    create_workspace()
    print(f"Workspace created {emoji}")
    print(f"Listing contents off new workspace : {workspace}")
    filelist = []
    for root, dir, files in os.walk(workspace):
        for file in files:
            filelist.append(os.path.join(root, file))
    for name in filelist:
        print(name)


if __name__ == '__main__':
    main()

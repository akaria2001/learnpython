import subprocess as cmd


def multiply(number, number2):
    return number * number2


def main():
    cmd.call("clear", shell=False)
    print(multiply(3, 4))


if __name__ == '__main__':
    main()

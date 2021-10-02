#!/usr/bin/env python
import subprocess as cmd
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', type=str , required=True, help="Username")
    parser.add_argument('-a', '--age', type=str, required=True, help="Age")
    parser.add_argument('-d', '--debug', required=False, help="Show debugging", action='store_true')
    args = parser.parse_args()

    debug = args.debug

    cmd.call(['clear'], shell=False)

    if(debug):
        print("Debugging is enabled")
        print(type(args))
        print(args)
        print(debug)
    else:
        print("Debugging is not enabled")

    print(f"User {args.username} is {args.age} years old")


if __name__ == '__main__':
    main()

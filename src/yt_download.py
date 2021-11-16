import pytube
import os

"""
Python Script to Download YouTube videos from a URL listing in a text file.

Grabbed information from https://dev.to/seijind/how-to-download-youtube-videos-in-python-44od
"""


def main():

    cwd = os.getcwd()

    print(f"Current Working directory :{cwd}")

    def grab_file_list():
        try:
            with open("src/links.txt") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("Unable to open file")
            exit()
        return lines

    print("Will download following YouTube Videos")

    for url in grab_file_list():
        print(url)
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download()


if __name__ == '__main__':
    main()

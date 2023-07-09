#!/bin/sh
pyinstaller -F --add-data "music.mp3:." --collect-all pyfiglet  dkmaths.py
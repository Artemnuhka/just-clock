#!/usr/bin/env python3

from re import M
import time
import subprocess

font = {
         ":": [
            "      ",
            "      ",
            "   #  ",
            "      ",
            "   #  "
        ],

        "1": [
            " mmm  ",
            "   #  ",
            "   #  ",
            "   #  ",
            " mm#mm"
        ],

        "2": [
            " mmmm ",
            "'   '#",
            "    m'",
            "   m' ",
            " m#mmm"
        ],

        "3": [
            " mmmm ",
            "*   *#",
            "  mmm*",
            "    *#",
            "*mmmm'"
        ],

        "4": [
            "    mm ",
            "   m*# ",
            "  #* # ",
            " #mmm#m",
            "     # "
        ],

        "5": [
            "mmmmm ",
            "#     ",
            "****mm",
            "     #",
            "*mmm#*"
        ],

        "6": [
            "  mmm ",
            "m*    ",
            "#m**#m",
            "#    #",
            " #mm#*"
        ],

        "7": [
            "mmmmmm",
            "    #*",
            "   m* ",
            "  m*  ",
            " m*   "
        ],

        "8": [
            " mmmm ",
            "#    #",
            "'mmmm'",
            "#   *#",
            "*#mmm'"
        ],

        "9": [
            " mmmm ",
            "#*  *m",
            "#m  m#",
            " ''' #",
            "*mmm* "
        ],

        "0": [
            " mmmm ",
            "m*  *m",
            "#  m #",
            "#    #",
            " #mm# "
        ]
    }

try:
    while True:
        subprocess.run(["clear"])
        hoy = time.strftime("%H:%M:%S")
        print()
        for rng in range(5):
            for char in hoy:
                print(font[char][rng], end=" ")
            
            print()

        time.sleep(1)

except KeyboardInterrupt:
    print()


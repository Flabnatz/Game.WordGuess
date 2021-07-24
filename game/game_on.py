import os
from WordLists.process import mk_csv


def nlet():
    print("How many letters would you like to play with? [2-15]")
    n = input()
    try:
        if int(n) in range(2,16):
            # Does the appropriate file exist?
            nlet_file(n)

    except ValueError:
        print('whoops!')
    except:
        return [0, False, "Unexpected Error Occurred...exiting game."]


def nlet_file(n):
    BASE_DIR = os.environ['PYTHONPATH']
    XL_DIR = BASE_DIR + "\Wordlists\\excel\\"
    CSV_DIR = BASE_DIR + "\Wordlists\\csv\\"

    mk_csv('4'+'-letter-words', XL_DIR, CSV_DIR)
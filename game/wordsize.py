import os
import time
from WordLists.process import mk_csv


def nlet():
    print("How many letters would you like to play with? [2-15]")
    n = input()
    try:
        if int(n) in range(2,16):
            # Does the appropriate file exist?
            nlet_file(n)
            return [n, True, "Unfortunately, the game is still in development."]

    except ValueError:
        print('whoops!')
        return [n, True, "Unfortunately, the game is still in development."]
    except FileNotFoundError:
        print("Unfortunately, the game is still in development")
        print("and is not ready for play with words of that size.")
        print("--------------------------------------------------")
        time.sleep(1)
        print("Let's play with a 4-letter word instead!")
        nlet_file(4)
        return [n, True, "Unfortunately, the game is still in development."]
    except:
        return [0, False, "Unexpected Error Occurred...exiting game."]


def nlet_file(n):
    BASE_DIR = os.environ['PYTHONPATH']
    XL_DIR = BASE_DIR + "\Wordlists\\excel\\"
    CSV_DIR = BASE_DIR + "\Wordlists\\csv\\"

    mk_csv(str(n)+'-letter-words', XL_DIR, CSV_DIR)
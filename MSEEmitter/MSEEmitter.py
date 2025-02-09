import os
import urllib
import urllib.request

from dotenv import load_dotenv
from random import randrange

load_dotenv()

ADDRESS = os.getenv('ADDRESS')
MYNAME = os.getenv('MYNAME')

def measure():
    # Here we would implement some measuring system
    print("measuring\n")
    measure = randrange(10)
    return measure

def send():

    url = ADDRESS + '/' + MYNAME + '/' + str(measure())
    print("sending: " + url + "\n")
    with urllib.request.urlopen(url) as response:
        pass
    print(response.status)

if __name__ == '__main__':
    send()

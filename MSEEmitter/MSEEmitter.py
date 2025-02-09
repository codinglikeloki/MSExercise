import os
from dotenv import load_dotenv

load_dotenv()

ADDRESS = int(os.getenv('ADDRESS'))
DEBUG = os.getenv('DEBUG')
MYNAME = os.getenv('MYNAME')

def measure():
    # Here we would implement some measuring system
    return 1

def send()
    url = ADDRESS + '/' '

schedule.every(1).minutes.do(send)

while true:
    schedule.run_pending()
    time.sleep(1)

import os
from dotenv import load_dotenv

load_dotenv()

DIRECTORYOFDB = os.getenv('DIRECTORYOFDB')
DEBUG = os.getenv('DEBUG')


def analyze():
    # still disgusting solution for data storage, but for this kind of exercise
    # this is good enough.
    measurementStorage = DIRECTORYOFDB + "/db.txt"
    print(measurementStorage)
    db = open(measurementStorage, "r")
    for line in db:
        # implement analysis
        print(line)
    db.close()
    return data

if __name__ == '__main__':
    analyze()

from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv('PORT'))
DEBUG = os.getenv('DEBUG')

app = Flask(__name__)

@app.route('/<uuid:senderId>/<int:measurement>')
def store(senderId,measurement):
    data = str(senderId) + ';' + str(measurement) + "\n"
    # disgusting solution for data storage, but for this kind of exercise this is
    # good enough.
    db = open("db.txt", "a+")
    db.write(data)
    db.close()
    return data

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)

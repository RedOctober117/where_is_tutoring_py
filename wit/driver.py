from flask import Flask, render_template, request
from enum import Enum

app = Flask(__name__)

class Room(Enum):
    CONFERENCE = 'Confernce Room 101'
    LAB_127 = 'Lab 127'
    LAB_124 = 'Lab 124'

current_room = Room.CONFERENCE.value

@app.route('/')
def where_is_tutoring():
    return render_template('index.html', room=current_room)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
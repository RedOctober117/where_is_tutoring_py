from flask import Flask, render_template, request
from enum import Enum

app = Flask(__name__)

class Room(Enum):
    CONFERENCE = 'Conference Room 101'
    LAB_127 = 'Lab 127'
    LAB_124 = 'Lab 124'

current_room = Room.CONFERENCE.value

@app.route('/')
def where_is_tutoring():
    return render_template('index.html', room=current_room)

if __name__ == "__main__":
    app.run(host='0.0.0.0', use_reloader=True, port=8080, debug=False)
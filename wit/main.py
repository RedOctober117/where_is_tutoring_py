from flask import Flask, render_template, request
from enum import Enum
import csv

csv_path = 'wit/rooms.csv'

app = Flask(__name__)

rooms = None
current_room = None

def init():
    global rooms, current_room
    rooms = read_csv(csv_path)
    current_room = rooms[0]


def refresh_rooms(path):
    global rooms
    rooms = read_csv(path)

def read_csv(path):
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        rooms = set()
        for line in reader:
            rooms.add(line[0])
        return list(rooms)

def write_csv(path:str, item: str, exclude):
    with open(path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if item[0] not in exclude:
            print(item)
            writer.writerow(item)


@app.route('/')
def where_is_tutoring():
    refresh_rooms(csv_path)
    return render_template('index.html', room=current_room)

@app.route('/ghostselect', methods=['POST', 'GET'])
def modify_room():
    refresh_rooms(csv_path)
    render = render_template('modify_room.html', options=rooms)
    keys = request.args.keys()
    print(keys)
    if len(keys) != 0:
        if 'new_room' in keys:
            print('KEY:', request.args['new_room'])
            write_csv('wit/rooms.csv', (request.args['new_room'],), rooms)
        if 'selection' in keys:
            global current_room
            current_room = request.args['selection']

    return render

if __name__ == "__main__":
    init()
    app.run(host='0.0.0.0', use_reloader=True, port=8080, debug=False)
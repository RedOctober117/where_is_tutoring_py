from flask import Flask, render_template, request
from enum import Enum
from datetime import datetime, timezone
import csv, pytz

csv_path = 'wit/rooms.csv'

app = Flask(__name__)

rooms = None
current_room = None
now = datetime.now(pytz.timezone('US/Eastern'))

def init():
    global rooms, current_room
    rooms = read_csv(csv_path)
    current_room = None


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

def write_csv(path: str, item, exclude, overwrite):
    with open(path, 'w' if overwrite else 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if type(item) is tuple:
            if item[0] not in exclude:
                writer.writerow(item)
        elif type(item) is list:
            for i in item:
                if i[0] not in exclude:
                    writer.writerow((i,))
        else:
            if item not in exclude:
                writer.writerow((item,))

@app.route('/')
def where_is_tutoring():
    refresh_rooms(csv_path)
    return render_template('index.html', room=current_room, timestamp=now.ctime())

@app.route('/ghostselect', methods=['POST', 'GET'])
def modify_room():
    global rooms, current_room
    refresh_rooms(csv_path)
    render = render_template('modify_room.html', options=rooms)
    keys = request.form.keys()
    method = request.method
    data = request.form
    print(keys)
    if method == 'POST':
        if 'selection' in keys:
            print('in selection')
            global current_room
            current_room = data['selection']
        if 'removal' in keys:
            print('in removal')
            rooms.remove(data['removal'])
            write_csv(csv_path, rooms, [], True)
        if 'new_room' in keys:
            write_csv('wit/rooms.csv', data['new_room'], rooms, False)
        global now
        now = datetime.now(pytz.timezone('US/Eastern')).isoformat()

    return render



if __name__ == "__main__":
    init()
    # app.run(host='0.0.0.0', use_reloader=True, port=8080, debug=False)
    app.run(debug=True, use_reloader=True)
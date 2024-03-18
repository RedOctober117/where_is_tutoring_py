from flask import Flask, render_template, request
from enum import Enum
import csv

app = Flask(__name__)

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

rooms = read_csv('wit/rooms.csv')

current_room = rooms[0]

@app.route('/')
def where_is_tutoring():
    return render_template('index.html', room=current_room)

@app.route('/ghostselect', methods=['POST', 'GET'])
def modify_room():
    render = render_template('modify_room.html.jinja', options=rooms)

    if len(request.args.keys()) != 0:
        global current_room
        current_room = request.args['selection']

    return render

# @app.route('/ghostwrite', methods=['POST', 'GET'])
# def modify_room():
#     render = render_template('modify_room.html.jinja', options=rooms)
#     # print('here:', request.args.keys())
#     if len(request.args.keys()) != 0:
#         current_room = request.args['selection']
#     return render

if __name__ == "__main__":
    app.run(host='0.0.0.0', use_reloader=True, port=8080, debug=False)
    # app.run(debug=True, use_reloader=True)
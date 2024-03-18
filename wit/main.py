from flask import Flask, render_template, request
from enum import Enum
import csv

app = Flask(__name__)

def read_csv(path):
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        return list(reader)

def write_csv(path:str, item: str, exclude):
    with open(path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if item not in exclude:
            writer.writerow(item)

rooms = read_csv('wit/rooms.csv')
write_csv('wit/rooms.csv', ('Conference 101',), rooms)
# print(read_csv('wit/rooms.csv'))

@app.route('/')
def where_is_tutoring():
    return render_template('index.html', room=current_room)

@app.route('/ghost', methods=['POST', 'GET'])
def modify_room():
    options = [option.value for option in Room]
    render = render_template('modify_room.html.jinja', options=options)
    # print('here:', request.args.keys())
    if len(request.args.keys()) != 0:
        current_room = request.args['selection']
    return render

if __name__ == "__main__":
    # app.run(host='0.0.0.0', use_reloader=True, port=8080, debug=False)
    app.run(debug=True, use_reloader=True)
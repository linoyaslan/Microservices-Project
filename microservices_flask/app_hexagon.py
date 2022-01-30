import os
import cv2
from flask import Flask, send_file, make_response

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

PATH = os.getcwd()
RADIUS = 60
RED = "RED"
YELLOW = "YELLOW"
GREEN = "GREEN"
BLUE = "BLUE"

@app.route('/hexagon/<color>')
def draw_hexagon(color):
    response = make_response(send_file('hexagon/hexagon.png', mimetype='image/png'))
    if color == RED:
        response = make_response(send_file('hexagon/hexagon_red.png', mimetype='image/png'))
    if color == YELLOW:
        response = make_response(send_file('hexagon/hexagon_yellow.png', mimetype='image/png'))
    if color == GREEN:
        response = make_response(send_file('hexagon/hexagon_green.png', mimetype='image/png'))
    if color == BLUE:
        response = make_response(send_file('hexagon/hexagon_blue.png', mimetype='image/png'))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response





if __name__ == '__main__':
    app.run(host="localhost", port=9987)

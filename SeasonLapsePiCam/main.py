from picamera import PiCamera
from time import sleep
import os

file_path = 'SeasonLapsePiCam/'
file_name = 'img.jpg'

def take_photo():
    os.system('fswebcam -r 4208x3120 -S 3 --jpeg 95 --save /home/pi/' + file_path + file_name) # uses Fswebcam to take picture
    # os.system('fswebcam -r 4208x3120 -S 3 --jpeg 98 --save /home/pi/to_transmit/98-%H.%M.%S.jpg') # uses Fswebcam to take picture
    # os.system('fswebcam -r 4208x3120 -S 3 --jpeg 100 --save /home/pi/to_transmit/100-%H.%M.%S.jpg') # uses Fswebcam to take picture

### Flask server

from flask import Flask, send_file
app = Flask(__name__)

@app.route('/')
def active():
    return 'Server active'

@app.route('/get_image')
def get_image():
    take_photo()
    return send_file(file_name, mimetype='image/jpg')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080)

from picamera import PiCamera
from time import sleep
import os

file_path = 'SeasonLapse/SeasonLapsePiCam/'
file_name = 'img.jpg'

camera = PiCamera()
#camera.resolution = (2592, 1944)
camera.resolution = (460, 640)
#camera.brightness = 70
#camera.contrast = 50
#camera.awb_mode = 'auto'
#camera.exposure_mode = 'auto'

def take_photo():
    #os.remove(file_path + file_name)
    camera.start_preview()
    sleep(2)
    camera.capture(file_path + file_name)
    camera.stop_preview()

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

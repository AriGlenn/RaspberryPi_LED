from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time


app = Flask(__name__, static_url_path='/static')
#app = Flask(__name__)

#-------------------------
GPIO.setmode(GPIO.BCM)
ledNumber = 21
GPIO.setup(ledNumber, GPIO.OUT)
#-------------------------
print("Running")

@app.route('/')
def index():
    print('Running... Home')
    return render_template('index.html')

@app.route('/ledOFF')
def LedOff():
    print('Running... Off')
    GPIO.output(ledNumber,GPIO.LOW)
    return 'LED off'

@app.route('/ledON')
def LedOn():
    print('Running... On')
    GPIO.output(ledNumber,GPIO.HIGH)
    return 'LED on'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

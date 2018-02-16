from flask import Flask, render_template, request


app = Flask(__name__, static_url_path='/static')

#-------------------------
import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(18,GPIO.OUT)
import time
GPIO.setmode(GPIO.BCM)
ledNumber = 21
GPIO.setup(ledNumber, GPIO.OUT)
#-------------------------
print("Running")

@app.route('/')
def index():
    print('Running...')
    GPIO.output(21,GPIO.LOW)
    return render_template('index.html')

@app.route('/ledOFF')
def LedOff():
    print('off')
    GPIO.output(21,GPIO.LOW)
    #GPIO.output(ledNumber,False)
    return 'LED off'

@app.route('/ledON')
def LedOn():
    print('on')
    GPIO.output(21,GPIO.HIGH)
    #GPIO.output(ledNumber,True)
    return 'LED on'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

from flask import Flask, render_template, request


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    print('Running...')
    return render_template('index.html')

@app.route('/ledOFF')
def LedOff():
    print('off')
    return 'LED off'

@app.route('/ledON')
def LedOn():
    print('on')
    return 'LED on'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

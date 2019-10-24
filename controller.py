from flask import Flask , request, flash, redirect, jsonify
from car import motion 

app = Flask(__name__)

def do_return(msg, val):
    dm = {"status": msg}
    resp = jsonify(dm)
    resp.status_code = val
    return resp

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/forward')
def forward():
	print("forward")
	motion.forward()
	return do_return('OK',200)

@app.route('/backward')
def backward():
	print("backward")
	return do_return('OK',200)

@app.route('/left')
def left():
	print("left")
	return do_return('OK',200)

@app.route('/right')
def right():
	print("forward")
	return do_return('OK',200)

@app.route('/stop')
def stop():
	print("stop")
	return do_return('OK',200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
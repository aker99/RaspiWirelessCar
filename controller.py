from flask import Flask ,render_template, request, flash, redirect, jsonify
from car import motion 
import socket

localip = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]
print(localip)

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
	motion.backward()
	return do_return('OK',200)

@app.route('/left')
def left():
	print("left")
	motion.left()
	return do_return('OK',200)

@app.route('/right')
def right():
	print("right")
	motion.right()
	return do_return('OK',200)

@app.route('/stop')
def stop():
	print("stop")
	motion.stop()
	return do_return('OK',200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
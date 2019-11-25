import RPi.GPIO as GPIO #Import Raspberry Pi GPIOlibrary

class Motion():
	"""docstring for ClassName"""
	def __init__(self):
		print("contructor")
		GPIO.setwarnings(False) # Ignore warning for now
		GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
		GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW)#right
		GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW)#right
		GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)#left 
		GPIO.setup(35, GPIO.OUT, initial=GPIO.LOW)#left
		
	def forward(self):
		print("forward2")
		GPIO.output(31, GPIO.LOW)#a2
		GPIO.output(33, GPIO.HIGH)#a1
		GPIO.output(37, GPIO.HIGH)#b2
		GPIO.output(35, GPIO.LOW)#b1

	def backward(self):
		print("backward2")
		GPIO.output(31, GPIO.HIGH)#a2
		GPIO.output(33, GPIO.LOW)#a1
		GPIO.output(37, GPIO.LOW)#b2
		GPIO.output(35, GPIO.HIGH)#b1

	def left(self):
		print("left2")
		GPIO.output(31, GPIO.HIGH)#a2
		GPIO.output(33, GPIO.LOW)#a1
		GPIO.output(37, GPIO.HIGH)#b2
		GPIO.output(35, GPIO.LOW)#b1

	def right(self):
		print("right2")
		GPIO.output(31, GPIO.LOW)#a2
		GPIO.output(33, GPIO.HIGH)#a1
		GPIO.output(37, GPIO.LOW)#b2
		GPIO.output(35, GPIO.HIGH)#b1

	def stop(self):
		print("stop2")
		GPIO.output(31, GPIO.LOW)#a2
		GPIO.output(33, GPIO.LOW)#a1
		GPIO.output(37, GPIO.LOW)#b2
		GPIO.output(35, GPIO.LOW)#b1

motion = Motion()
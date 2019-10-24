#import RPi.GPIOas GPIO# Import Raspberry Pi GPIOlibrary

class Motion():
	"""docstring for ClassName"""
	def __init__(self):
		print("contructor")
		#GPIO.setwarnings(False) # Ignore warning for now
		#GPIO.setmode(#GPIO.BOARD) # Use physical pin numbering
		#GPIO.setup(16, #GPIO.OUT, initial=#GPIO.LOW)#right
		#GPIO.setup(18, #GPIO.OUT, initial=#GPIO.LOW)#right
		#GPIO.setup(13, #GPIO.OUT, initial=#GPIO.LOW)#left 
		#GPIO.setup(15, #GPIO.OUT, initial=#GPIO.LOW)#left
		
	def forward(self):
		print("forward2")
		#GPIO.output(16, #GPIO.LOW)#a2
		#GPIO.output(18, #GPIO.HIGH)#a1
		#GPIO.output(13, #GPIO.HIGH)#b2
		#GPIO.output(15, #GPIO.LOW)#b1

	def backward(self):
		print("backward2")
		#GPIO.output(16, #GPIO.HIGH)#a2
		#GPIO.output(18, #GPIO.LOW)#a1
		#GPIO.output(13, #GPIO.LOW)#b2
		#GPIO.output(15, #GPIO.HIGH)#b1

	def left(self):
		print("left2")
		#GPIO.output(16, #GPIO.HIGH)#a2
		#GPIO.output(18, #GPIO.LOW)#a1
		#GPIO.output(13, #GPIO.HIGH)#b2
		#GPIO.output(15, #GPIO.LOW)#b1

	def right(self):
		print("right2")
		#GPIO.output(16, #GPIO.LOW)#a2
		#GPIO.output(18, #GPIO.LOW)#a1
		#GPIO.output(13, #GPIO.LOW)#b2
		#GPIO.output(15, #GPIO.LOW)#b1

	def stop(self):
		print("stop2")
		#GPIO.output(16, #GPIO.LOW)#a2
		#GPIO.output(18, #GPIO.LOW)#a1
		#GPIO.output(13, #GPIO.LOW)#b2
		#GPIO.output(15, #GPIO.LOW)#b1

motion = Motion()
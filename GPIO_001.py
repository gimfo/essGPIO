import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
configuration=GPIO.getmode()
print(configuration)
GPIO.setup(5,GPIO.OUT)
GPIO.output(5,GPIO.HIGH)



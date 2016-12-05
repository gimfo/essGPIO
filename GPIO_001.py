import RPi.GPIO as GPIO  #librairie
GPIO.setmode(GPIO.BCM) # mode identification
configuration=GPIO.getmode()
print(configuration)
GPIO.setup(5,GPIO.OUT)
GPIO.output(5,GPIO.HIGH)



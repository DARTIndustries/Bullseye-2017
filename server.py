import socket 
import RPi.GPIO as GPIO

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ("0.0.0.0", 3000)

sock.bind(server)
sock.listen(1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
p = GPIO.PWM(26, 50)
p.start(50)

while True:
	connection, address = sock.accept()
	data = connection.recv(6)
	while len(data) > 0:
		data = connection.recv(6)
		i = int(data.split(",")[1])
		p.ChangeDutyCycle(i)
		
		
	
		

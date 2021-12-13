#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int8
import Jetson.GPIO as GPIO
import time
from datetime import datetime, timedelta
import csv
import os 


def low(lent,pub):
	GPIO.output(output_pin, 0) 
	for x in range(lent):	
		pub.publish(1)
		time.sleep(0.02)	


def high(lent,pub):
	GPIO.output(output_pin,1) 
	for x in range(lent):	
		pub.publish(0)
		time.sleep(0.02)

def start(pub):
	low(200,pub)
	high(10,pub)
	low(50,pub)

def intreval(pub):
		high(2,pub)
		low(50,pub)

def long(pub):
		high(20,pub)
		low(50,pub)

def talker():
	pub = rospy.Publisher('bits', Int8, queue_size=10) 
	rospy.init_node('Bit_Node', anonymous=False)
	i = 0 
	start(pub)
	while not rospy.is_shutdown():
		intreval(pub)
		i+=1
		if i == 10:
			long(pub)
			i = 0 




if __name__ == '__main__':
	start_time = str(datetime.now())[11:19]            
	GPIO.setwarnings(False)	
	output_pin = 29  
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(output_pin, GPIO.OUT)
	GPIO.output(output_pin, GPIO.LOW)
	time.sleep(1)
	try:
		talker()
	except KeyboardInterrupt:
			print("GPIO cleanup,Data saved")
	print("GPIO cleanup,Data saved")
	GPIO.cleanup(22)










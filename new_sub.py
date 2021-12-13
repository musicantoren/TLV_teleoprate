#!/usr/bin/env python
import rospy
from datetime import datetime, timedelta
from geometry_msgs.msg import TwistStamped 
from std_msgs.msg import Int8
import csv
import os
import message_filters


def callback1(msg):
	global listi
	stamp_time = str(datetime.now())[11:23]
	temp = (stamp_time,msg.data)  
	print(temp)  	
	listi.append(temp)

def shutdown_handler():
	print("finish")

if __name__ == '__main__':
    listi = list()
    start_time = str(datetime.now())[11:19]
    rospy.init_node('testNode', anonymous=False)
    rospy.Subscriber("/bits", Int8 , callback1)
    rospy.on_shutdown(shutdown_handler)
    rospy.spin()
    end_time = str(datetime.now())[11:19]
    os.chdir("/home/omer/logs")
    with open('rosgps-('+start_time+'-'+end_time+').csv', 'wb') as myfile:
    	wr = csv.writer(myfile)
    	wr.writerow(listi)

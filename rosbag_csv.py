#!/usr/bin/env python
import rospy
from datetime import datetime, timedelta
import rosbag
import rosbag_pandas
from std_msgs.msg import Int8
from std_msgs.msg import String
from geometry_msgs.msg import TwistStamped
from geometry_msgs.msg import PoseStamped 
import os 


dir_list = os.listdir(os.getcwd())
name_list = list()
for x in dir_list:
	if x.endswith('.bag'):
		name_list.append(os.path.join(os.getcwd(),x))
for x in name_list:
	df = rosbag_pandas.bag_to_dataframe(x) 
	name = os.path.join(os.getcwd(),"logs","local_GPS",x[16:x.find(".bag")]+".csv")
	print("SAVED->"+name)
	df.to_csv(name)



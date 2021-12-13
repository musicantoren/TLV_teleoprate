#!/bin/bash
rosbag record /gnss_velocity /gnss_pose /gnss_acceleration /gps_time --split --duration 60
python rosbag_csv.py



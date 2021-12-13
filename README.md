### sort.py
Python script for sort and merge data of TLV teleoprate  
  
**GPS_df("GPS_record.csv"):**  
Gets the GPS record file (csv) of all the day. Create CSV file for GPS record with timestamp,named "GPS_data_clock.csv".

**merge_df("mindware text file.txt","jetson mindware signal file.csv"):**  
Gets mindware text file from the mindware device, and gets jetson signal CSV file. Create CSV file of mindware signal with timestamp, named "merged_" and mindware file name.     

### gps_only.launch  
Start connection to the GPS.  

### rosbag_csv.py  
Start saving all GPS data to the jetson in 30 minute intervals.

### signal.launch  
Start transmit signal from the jetson to the mindware, by starting new_sub.py and mindwars.py.  

### merge_GPS_of_day.py 
Merges all GPS csv files to one sorted file. 

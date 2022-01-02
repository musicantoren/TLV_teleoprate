## Post processing
### sort.py
Python script for offline processing, sort and merge data from GPS and Mindware of TLV teleoprate experiment.  
  
- **GPS_df("GPS_record.csv"):**  
Gets the GPS record file (csv) of all the day. Create CSV file for GPS record with timestamp,named "GPS_data_clock.csv".

- **merge_df("mindware text file.txt","jetson mindware signal file.csv"):**  
Gets mindware text file from the mindware device, and gets jetson signal CSV file. Create CSV file of mindware signal with timestamp, named "merged_" and mindware file name.     

## Jetson system files  
# Start of the day omer
### gps_only.launch  
- Start connection to the GPS.  
- Activate with `gps_start` (open the first terminal + change headline).  

### rosbag_csv.py  
- Start saving all GPS data to the jetson in 30 minute intervals.  
- Saves data at "logs/local_GPS" folder with timestamp.  
- Activate with `gps_save` (split terminal + change headline). 

###  Check GPS
- activate with 'ros' (split terminal)
- 
# End of the day omer
### merge_GPS_of_day.py 
- Merges all GPS csv files to one sorted file.  
- Saves data at "logs/local_GPS" folder with the name "all_day_GPS.csv". with date    

### See if the GPS works
-- 
# Tehila  
### signal.launch  
- Start transmit signal from the jetson to the mindware, by starting new_sub.py and mindwars.py.   
- Saves data at "logs/jetson_signal" folder with timestamp.  
- Activate with `start` (new terminal + change heafline to tehile start).  and control+C to end  

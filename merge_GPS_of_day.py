import os
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
import warnings
warnings.filterwarnings('ignore')
import os
from datetime import datetime

os.chdir("/home/omer/logs/local_GPS")
dir_list = os.listdir(os.getcwd())
name_list = list()
for x in dir_list:
    if x.endswith('.csv'):
        name_list.append(os.path.join(os.getcwd(),x))
name_list.sort()
df = pd.read_csv(name_list[0])
print(name_list[0])
for x in name_list[1:]:
    df_temp = pd.read_csv(x)
    df = df.append(df_temp, ignore_index = True)
    print(x)
df.rename(columns = {'Unnamed: 0':'Time'}, inplace = True)
df.reset_index()
df['jetson_Time'] =" "
del df['/gnss_acceleration/header/frame_id']
del df['/gnss_acceleration/header/seq']
del df['/gnss_acceleration/header/stamp/nsecs']
del df['/gnss_acceleration/header/stamp/secs']
del df['/gnss_pose/header/frame_id']
del df['/gnss_pose/header/seq']
del df['/gnss_pose/header/stamp/nsecs']
del df['/gnss_pose/header/stamp/secs']
del df['/gnss_velocity/header/frame_id']
del df['/gnss_velocity/header/seq']
del df['/gnss_velocity/header/stamp/nsecs']
del df['/gnss_velocity/header/stamp/secs']
del df['/gps_time/header/frame_id']
del df['/gps_time/header/seq']
del df['/gps_time/header/stamp/nsecs']
del df['/gps_time/header/stamp/secs']

#for x in df.index:
#    y = datetime.fromtimestamp(df.Time[x])
#    stri =str(y.hour)+":"+str(y.minute)+":"+str(y.second)+":"+str(y.microsecond)[:3]
#    df.jetson_Time[x] = stri
#    print(df.jetson_Time[x])
#print("add time stamp")
df.to_csv(os.path.join(os.getcwd(),'final_GPS.csv'))
print("Saved")

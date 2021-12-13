#!/usr/bin/env python
import os
import pandas as pd
from os import path
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
import warnings
warnings.filterwarnings('ignore')
from datetime import datetime 
from datetime import timedelta
import time

def jetson_df(name):            
    df = pd.read_csv(name)
    my_list = df.columns.values.tolist()
    df1 = pd.DataFrame(my_list,my_list, columns = ['jetson_Time'])
    df1["bits"] = "-"
    df1 = df1.reset_index()
    del df1['index']
    for x in df1.index:
        df1.bits[x] = int(df1.jetson_Time[x][16:18])
        df1.jetson_Time[x] = df1.jetson_Time[x][2:14]
    return df1

def mindware_df(name):
    timelist=list()
    bio1list=list()    
    bio2list=list()
    GSC_list=list()
    X_Axis_list=list()
    Y_Axis_list=list()
    Z_Axis_list=list()
    with open(name, "r") as file:
        file.readline()
        file.readline()
        for l in file:
            x=l.strip().split("\t")
            timelist.append(float(x[0]))
            bio1list.append(float(x[1]))
            bio2list.append(float(x[2]))
            GSC_list.append(float(x[3]))
            X_Axis_list.append(float(x[4]))
            Y_Axis_list.append(float(x[5]))
            Z_Axis_list.append(float(x[6]))
    return pd.DataFrame({'time': timelist,'bio1': bio1list,'bio2': bio2list,'GSC': GSC_list, 'X_Axis':X_Axis_list, 'Y_Axis':Y_Axis_list, 'Z_Axis':Z_Axis_list})

def mindware_peak(mindware):    
    bitsc=0
    s_peak_index=0
    b_peak_index=0
    mindware["peak"]=" "
    mindware["p_index"]="-"
    for i in mindware.index[:len(mindware.index)-1]:
        if mindware.bio2[i]!=0.599922:
            bitsc+=1
            if mindware.bio2[i]!=0.599922 and mindware.bio2[i+1]==0.599922:
                if 95<bitsc<110:
                    mindware.peak[i]="start"
                    mindware.p_index[i]='s'
                    save_i=i
                    break
    bitsc=0
    s_peak_index=0
    b_peak_index=0
    smallp=0
    for i in mindware.index[save_i+1:len(mindware.index)-1]:
        if mindware.bio2[i]!=0.599922:
            bitsc+=1
            if mindware.bio2[i]!=0.599922 and mindware.bio2[i+1]==0.599922:
                pindex= f'{b_peak_index}.{s_peak_index}'
                if 17<bitsc<27:
                    mindware.peak[i]="small"
                    mindware.p_index[i]=pindex
                    s_peak_index+=1
                if 195<bitsc<220:
                    b_peak_index+=1
                    mindware.peak[i]="big"
                    mindware.p_index[i]=str(b_peak_index)
                bitsc=0
                if s_peak_index==10:s_peak_index=0
    return mindware

def jetson_peak(jetson):    
    bitsc=0
    s_peak_index=0
    b_peak_index=0
    jetson["peak"]=" "
    jetson["p_index"]="--"
    for i in jetson.index[:len(jetson.index)-1]:
        if jetson.bits[i]!=1:
            bitsc+=1
            if jetson.bits[i]==0 and jetson.bits[i+1]==1:
                if bitsc==10:
                    jetson.peak[i]="start"
                    jetson.p_index[i]='s'
                    save_i=i
                    break
    bitsc=0
    s_peak_index=0
    b_peak_index=0
    smallp=0
    for i in jetson.index[save_i+1:len(jetson.index)-1]:
        if jetson.bits[i]!=1:
            bitsc+=1
            if jetson.bits[i]!=1 and jetson.bits[i+1]==1:
                pindex= f'{b_peak_index}.{s_peak_index}'
                if bitsc==2:
                    jetson.peak[i]="small"
                    jetson.p_index[i]=pindex
                    s_peak_index+=1
                if bitsc==20:
                    b_peak_index+=1
                    jetson.peak[i]="big"
                    jetson.p_index[i]=str(b_peak_index)
                bitsc=0
                if s_peak_index==10:s_peak_index=0
    return jetson

def merge_df(mindware_name,jetson_name):
    mindware_basic=mindware_df(mindware_name)
    jetson_basic = jetson_df(jetson_name)
    merge = pd.merge(mindware_peak(mindware_basic), jetson_peak(jetson_basic), how = "left")
    del merge['peak']
    del merge['bits']
    merge.to_csv("merged_"+mindware_name[:len(mindware_name)-4]+".csv")
#     display(merge.loc[(merge['p_index']!='-')])

def GPS_df(name):
    df = pd.read_csv(name)
    for x in df.index:
        y = datetime.fromtimestamp(df.Time[x])
        stri =str(y.hour)+":"+str(y.minute)+":"+str(y.second)+":"+str(y.microsecond)[:3]
        df.jetson_Time[x] = stri
    del df["Unnamed: 0"]
    df.to_csv("GPS_data_clock.csv")

GPS_df("GPS file of the day.csv")
merge_df("mindware text file.txt","jetson mindware signal file.csv")


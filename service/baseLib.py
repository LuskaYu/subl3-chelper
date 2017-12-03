#!/usr/bin/python

import time

TIME_LIB_ISOFORMAT = "%Y-%m-%d-%H:%M:%S"

def getStdTimeStr():
    global TIME_LIB_ISOFORMAT
    return time.strftime(TIME_LIB_ISOFORMAT, time.localtime())
def getFileNameFromPath(filePath):
    strArray = filePath.split('/')
    if len(strArray) == 1:
        strArray = filePath.split('\\')
        
    return strArray[-1]
def getFileNamePart(filename_with_type):
    strArray = filename_with_type.split('.')
    if  strArray is not None:
        return strArray[0]

    return filename_with_type

def alignStr2Width(input_str, width, fill):
    oldLen = len(input_str)
    if oldLen >= width:
        return input_str
    
    for count in range(0, width-oldLen): 
        input_str += fill
    return input_str


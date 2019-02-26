import pandas as pd
import os
import time
import datetime

def init_log(log_name, log_folder_dir="default"):
    # Does the log folder already exist? If not then make a new one
    if log_folder_dir == "default":
        if os.path.isdir(os.getcwd() + "//" + "logs"):
            pass
        else:
            os.mkdir("logs")
    else:
        if os.path.isdir(log_folder_dir + "//" + "logs"):
            pass
        else:
            os.mkdir(log_folder_dir + "//" + "logs")
    
    # Get log_path
    if log_folder_dir == "default":
        log_path = os.getcwd() + "//logs//" + log_name + ".txt"
    else:
        log_path = log_folder_dir + "//logs//" + log_name + ".txt"
    
    # Create a .txt file at specified path
    with open(log_path, "w") as f:
        # Write headers, TODO: make these customizable as well
        f.write("   Date    |   Time   | Log Name  | Event Name | Message | Status")

def log_event(log_name, event_name, message, status, directory="default"): # make some of these params default / optional using special optional params
    # Get log_path
    if directory == "default":
        log_path = os.getcwd() + "//logs//" + log_name + ".txt"
    else:
        log_path = directory + "//logs//" + log_name + ".txt"
    
    # Get day and time
    time_seconds = time.time()
    time_string = datetime.datetime.fromtimestamp(time_seconds).strftime("%m-%d-%Y %H:%M:%S")
    time_list = time_string.split()
    date = time_list[0]
    timestamp = time_list[1]

    with open(log_path, "a") as f:    
        f.write("\n" + date + " | " + timestamp + " | " +  log_name + " | " + event_name + " | " + message + " | " + status)

def analyze_log(log_name, directory="default"):
    # Get log_path
    if directory == "default":
        log_path = os.getcwd() + "//logs//" + log_name + ".txt"
    else:
        log_path = directory + "//logs//" + log_name + ".txt"

    log_list = pd.read_csv(log_path)
    print(log_list)

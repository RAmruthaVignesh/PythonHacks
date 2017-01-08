import os

LOG_DIR_PATH = 'logs/today_logs'
FILE_NAME = 'amrutha_logs.txt'

# check if the directory exists, if not create
if not os.path.exists(LOG_DIR_PATH):
    os.makedirs(LOG_DIR_PATH)    

# open the file in write mode
logfile = open(os.path.join(LOG_DIR_PATH, FILE_NAME), 'w')

# Write to the file
str_value = 10.0
string_to_write = 'sensor_name : ' + str(str_value)
logfile.write(string_to_write)

# Close the file handler
logfile.close()

# Testcase

expected_value = 10.0
print expected_value == str_value
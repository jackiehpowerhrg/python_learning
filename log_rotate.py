#!/usr/bin/env python3

# To run this script, type 'py log_rotation.py <file name you want to rotate>'. 
# The command line arguement of the file name will be put into sys.argv, the path is stored as a string. 

# Pull the built-in modules needed for the script. We only need one of the logging handlers. 
import os
import glob
import logging
from logging.handlers import RotatingFileHandler
import sys

# If theres exactly 2 arguments within sys.argv object, the python script being the first and the file name being the second, then get the 
# second one and make it a the file variable. If the variable has either more than one argument or no arguements outside of the script itself, set the variable to empty. 

if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    file = ""

# If the file variable is empty, end the program with the message that the user must provide a file arguement.
if not file:
    sys.exit(logging.warning(" No single arguement provided, please supply one file name as an arguement."))

# Create a logger and set the log level
logger = logging.getLogger('MyLogger')
logger.setLevel(logging.INFO)

# Check if log exists and should therefore be rolled. If not, create new file.
needRoll = os.path.isfile(file)

# Add the log message handler to the logger, the backup count is the maximum amount of log files of that name to keep. 
handler = logging.handlers.RotatingFileHandler(file, backupCount=10)

logger.addHandler(handler)

# This is a stale log, so roll it
if needRoll:    
    # Roll over on application start
    logger.handlers[0].doRollover()

# Create a list of the log files that exist and have been created
logfiles = glob.glob('%s*' % file)

print '\n'.join(logfiles)

#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : Basic usage of logging
# Author:       Denny Vettom
# Dependencies: Python3
#

"""
basicConfig( format = formatstr, datefmt = date_format_str) 
Formating of output log and Date format

%(asctime)s      : Human readable date format when log record was created
%(filename)s     : File name where log message originated
%(funcName)s     : Function name where log message originated
%(levelname)s    : String representation of message level (DEBUG,INFO, etc)
%(levelno)d      : Numeric of log level
%(lineno)d       : Line number where logging call was issued
%(message)s      : Logged message string
%(module)s       : module name portion of the file

filename : Defines file to store logs
filemode : Default is append. Configure if need overwrite at each run
level : Defined what is level
format : Defines formatting of output message
datefmt:  define format of date

"""

import logging

def main():
    # # Define format string
    formatstr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s "
    datestr = "%m/%d/%Y %I:%M:%S %p"

    logging.basicConfig(filename="output.log", level=logging.DEBUG, 
                        filemode="w", format=formatstr, datefmt=datestr)

    # Simple logging some message to file
    logging.info("Info level message") #INFO:root:Info level message
    logging.debug("Warning message") # WARNING:root:Warning message




if __name__ == "__main__":
    main() 
# normallogger (logium) - A simple logging library
[![PyPI version 0.5](https://badge.fury.io/py/normallogger.svg)](https://pypi.org/project/logium/)
A simple logging library for recording and displaying log messages.

This library provides a Logger class that allows you to log messages with various severity levels. The log messages can be output to the console and/or saved to a log file with timestamps.

## Usage:
1. Create an instance of the Logger class by providing the log file name and optional settings.
2. Use the logger instance to call different logging methods based on the severity level.
3. The log messages will be printed to the console and/or appended to the log file.

## logger
Initializes an instance of the Logger class.  
Args:
- file (str): The name of the log file.  
- console_enabled (bool): Whether logging is enabled in the console (default: True).  
- datetime_format (str): The format of the date and time for the logs (default: '%d.%m.%Y %H:%M:%S').  
- date_in_console (bool): Whether to include date and time in the console output (default: True).  
- file_enable (bool): Whether to enable log file writing (default: True).  
- date_in_file (bool): Whether to include date and time in the file output (default: True).  
- wrap (str): The character to wrap the log message (default: '[message]').


### Methods:
- Logger.d(self) -> None:  <br> &nbsp;&nbsp;&nbsp;&nbsp;
    Method for debug messages.
- Logger.e(self) -> None:  <br> &nbsp;&nbsp;&nbsp;&nbsp;
    Method for error messages.
- Logger.i(self) -> None:  <br> &nbsp;&nbsp;&nbsp;&nbsp;
    Method for informational messages.
- Logger.s(self) -> None:  <br> &nbsp;&nbsp;&nbsp;&nbsp;
    Method for settings messages.
- Logger.w(self) -> None:  <br> &nbsp;&nbsp;&nbsp;&nbsp;
    Method for warning messages.
- Logger.c(self) -> None:  <br> &nbsp;&nbsp;&nbsp;&nbsp;
    Method for critical messages.

### Example Usage:
#### Basic Usage:

The path to the log file must be specified in logger()

```python
from logium import logger

# Create an instance of the Logger
log = logger('log.log')

# Log messages
log.d('This is a debug message')          # dd.mm.yyyy hh:mm:ss [DEBUG] This is a debug message
log.e('This is an error message')         # dd.mm.yyyy hh:mm:ss [ERROR] This is an error message
log.i('This is an informational message') # dd.mm.yyyy hh:mm:ss [INFO] This is an informational message
log.s('This is a settings message')       # dd.mm.yyyy hh:mm:ss [SETTINGS] This is a settings message
log.w('This is a warning message')        # dd.mm.yyyy hh:mm:ss [WARNING] This is a warning message
log.c('This is a critical message')       # dd.mm.yyyy hh:mm:ss [CRITICAL] This is a critical message
```

#### Advanced Usage:
```python

from logium import logger

path_file = 'log.log'
log = logger(path_file, console_enabled=False, date_in_console=False, date_in_file=False, wrap = '-message-')

log.d('tag', 'This is a debug message')    # -DEBUG- tag: This is a debug message (in file only)
...
```
For datetime_format see: [datetime documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)  
There can be as many tags as you want
```python
from logium import logger

path_file = 'log.log'
log = logger(path_file, datetime_format='%d %b %H:%M:%S', file_enable=False)

log.d('tag','This is a debug message')    # 16 Jul 02:31:35 [DEBUG] tag: This is a debug message (in console only)
log.e('tag','tag2','This is an error message')   # 16 Jul 02:31:35 [ERROR] tag: tag2: This is an error message (in console only)e
```

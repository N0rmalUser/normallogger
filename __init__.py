"""
A simple logging library for recording and displaying log messages.

Author: N0rmalUser
Version: 0.2

This library provides a Logger class that allows you to log messages with various severity levels. The log messages can be output to the console and/or saved to a log file with timestamps.

Usage:
1. Create an instance of the Logger class by providing the log file name and optional settings.
2. Use the logger instance to call different logging methods based on the severity level.
3. The log messages will be printed to the console and/or appended to the log file.

Classes:
- logger: Class for logging and recording logs.
- help: Provides detailed information about the methods of the Logger class.

Methods:
- Logger.__init__(self, *file: str, console_enabled=True, datetime_format='%d.%m.%Y %H:%M:%S',
                   date_in_console=True, file_enable=True, date_in_file=True):
    Initializes an instance of the Logger class.
    Args:
        file (str): The name of the log file.
        console_enabled (bool): Whether logging is enabled in the console (default: True).
        datetime_format (str): The format of the date and time for the logs (default: '%d.%m.%Y %H:%M:%S').
        date_in_console (bool): Whether to include date and time in the console output (default: True).
        file_enable (bool): Whether to enable log file writing (default: True).
        date_in_file (bool): Whether to include date and time in the file output (default: True).

- Logger.d(self) -> None:
    Method for debug messages.

- Logger.e(self) -> None:
    Method for error messages.

- Logger.i(self) -> None:
    Method for informational messages.

- Logger.s(self) -> None:
    Method for settings messages.

- Logger.w(self) -> None:
    Method for warning messages.

- Logger.c(self) -> None:
    Method for critical messages.

Example Usage:
```python
from logium import Logger
в
# Create an instance of the Logger
my_logger = Logger('log.txt')

# Log messages
my_logger.d('This is a debug message')
my_logger.e('This is an error message')
my_logger.i('This is an informational message')
my_logger.s('This is a settings message')
my_logger.w('This is a warning message')
my_logger.c('This is a critical message')
```
"""

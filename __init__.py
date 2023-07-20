"""
A simple logging library for recording and displaying log messages.
Author: N0rmalUser
Version: 1.1

A guide is in my GitHub repository: https://github.com/N0rmalUser/normallogger
        or logium.GitHub
"""
from datetime import datetime
import webbrowser


def _printer(self):
    """
    The inner function for printing the message to the console and/or file
    """
    if self.console_enabled:
        print(f'{self.datetime} {self.message}' if self.console_enabled and self.date_in_console else self.message)
    if self.file_enable:
        file_output = f'{self.datetime} {self.message}' if self.file_enable and self.date_in_file else self.message
        with open(self.logfile[0], "a", encoding='utf-8') as f:
            f.write(f'{file_output}\n')


def _tagger(func):
    """
    The inner decorator function tagger takes a function and adds a tag to the message.
    """

    def wrapper(self, *args):
        message = ' '.join(str(arg) + (':' if i != len(args) - 1 else '') for i, arg in enumerate(args))
        self.message = message
        return func(self)

    return wrapper


class logger:
    """
    Class for logging and recording logs
    """

    def __init__(self, *logfile: str, console_enabled=True, datetime_format='%d.%m.%Y %H:%M:%S',
                 date_in_console=True, file_enable=True, date_in_file=True, wrap='[message]'):
        """
        Initializes an instance of the logger class.

        Args:
            logfile (str): The name of the log file.
            console_enabled (bool): Whether logging is enabled in the console (default: True).
            datetime_format (str): The format of the date and time for the logs (default: '%d.%m.%Y %H:%M:%S').
            date_in_console (bool): Whether to include date and time in the console output (default: True).
            file_enable (bool): Whether to enable log file writing (default: True).
            date_in_file (bool): Whether to include date and time in the file output (default: True).
        """
        if not all(isinstance(var, bool) for var in (console_enabled, date_in_console, file_enable, date_in_file)):
            raise ValueError("console_enabled, date_in_console, date_in_file, and file_enabled must be of bool type")
        if not all(isinstance(var, str) for var in (datetime_format, wrap)):
            raise ValueError("datetime_format, wrap must be of str type")
        if not isinstance(datetime_format, str):
            raise ValueError("datetime_format must be of str type")
        self.logfile = logfile
        self.datetime = datetime.now().strftime(datetime_format)
        self.console_enabled = console_enabled
        self.file_enable = file_enable
        self.date_in_console = date_in_console
        self.date_in_file = date_in_file
        self.wrap = wrap
        self.message = ''

    @_tagger  # debug
    def d(self) -> None:
        """
        Decorator method for debug messages
        """
        self.message = self.wrap.replace("message", 'DEBUG') + ' ' + self.message
        _printer(self)

    @_tagger  # error
    def e(self) -> None:
        """
        Decorator method for error messages
        """
        self.message = self.wrap.replace("message", 'ERROR') + ' ' + self.message
        _printer(self)

    @_tagger  # info
    def i(self) -> None:
        """
        Decorator method for informational messages
        """
        self.message = self.wrap.replace("message", 'INFO') + ' ' + self.message
        _printer(self)

    @_tagger  # settings
    def s(self) -> None:
        """
        Decorator method for settings messages
        """
        self.message = self.wrap.replace("message", 'SETTINGS') + ' ' + self.message
        _printer(self)

    @_tagger  # warning
    def w(self) -> None:
        """
        Decorator method for warning messages
        """
        self.message = self.wrap.replace("message", 'WARNING') + ' ' + self.message
        _printer(self)

    @_tagger  # critical
    def c(self) -> None:
        """
        Decorator method for critical messages
        """
        self.message = self.wrap.replace("message", 'CRITICAL') + ' ' + self.message
        _printer(self)

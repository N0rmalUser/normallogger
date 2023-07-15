from decorators import _decorator
from datetime import datetime


class logger:
    """
    Class for logging and recording logs
    """
    def __init__(self, *file: str, console_enabled=True, datetime_format='%d.%m.%Y %H:%M:%S',
                 date_in_console=True, file_enable=True, date_in_file=True):
        """
        Initializes an instance of the logger class.

        Args:
            file (str): The name of the log file.
            console_enabled (bool): Whether logging is enabled in the console (default: True).
            datetime_format (str): The format of the date and time for the logs (default: '%d.%m.%Y %H:%M:%S').
            date_in_console (bool): Whether to include date and time in the console output (default: True).
            file_enable (bool): Whether to enable log file writing (default: True).
            date_in_file (bool): Whether to include date and time in the file output (default: True).
        """
        if not all(isinstance(var, bool) for var in (console_enabled, date_in_console, file_enable, date_in_file)):
            raise ValueError("console_enabled, date_in_console, date_in_file, and file_enabled must be of bool type")
        if not all(isinstance(file, str) for file in file):
            raise ValueError("logfiles must be of str type")
        if not isinstance(datetime_format, str):
            raise ValueError("datetime_format must be of str type")
        self.file = file
        self.time = datetime.now().strftime(datetime_format)
        self.console_enabled = console_enabled
        self.file_enable = file_enable
        self.date_in_console = date_in_console
        self.date_in_file = date_in_file
        self.message = ''

    @_decorator.tagger  # debug
    def d(self) -> None:
        """
        Decorator method for debug messages
        """
        self.message = '-DEBUG-' + self.message
        _printer(self)

    @_decorator.tagger  # error
    def e(self) -> None:
        """
        Decorator method for error messages
        """
        self.message = '-ERROR- ' + self.message
        _printer(self)

    @_decorator.tagger  # info
    def i(self) -> None:
        """
        Decorator method for informational messages
        """
        self.message = '-INFO- ' + self.message
        _printer(self)

    @_decorator.tagger  # settings
    def s(self) -> None:
        """
        Decorator method for settings messages
        """
        self.message = '-SETTINGS-' + self.message
        _printer(self)

    @_decorator.tagger  # warning
    def w(self) -> None:
        """
        Decorator method for warning messages
        """
        self.message = '-WARNING- ' + self.message
        _printer(self)

    @_decorator.tagger  # critical
    def c(self) -> None:
        """
        Decorator method for critical messages
        """
        self.message = '-CRITICAL- ' + self.message
        _printer(self)


def _printer(self):
    """
    The inner function for printing the message to the console and/or file
    """
    console_output = f'{self.time} {self.message}' if self.console_enabled and self.date_in_console else self.message
    if self.console_enabled:
        print(console_output)
    if self.file_enable:
        file_output = f'{self.time} {self.message}' if self.file_enable and self.date_in_file else self.message
        with open(self.file, "a", encoding='utf-8') as f:
            f.write(f'{file_output}\n')

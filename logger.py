from decorators import _decorator
from datetime import datetime


class logger:
    """
    TODO: Добавить описание класса logger
    """
    def __init__(self, file: str, console_enabled=True, datetime_format='%d.%m.%Y %H:%M:%S',
                 date_in_console=True, file_enable=True, date_in_file=True):
        """
        TODO: Добавить описание функции __init__
        """
        if not all(isinstance(var, bool) for var in (console_enabled, date_in_console, file_enable, date_in_file)):
            raise ValueError("console_enabled, date_in_console, dste_in_file и file_enabled должны быть типа bool")
        if not all(isinstance(file, str) for file in file):
            raise ValueError("logfiles должны быть типа str")
        if not isinstance(datetime_format, str):
            raise ValueError("datetime_format должен быть типа str")
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
        TODO: Добавить описание функции d
        """
        self.message = '-DEBUG-' + self.message
        _printer(self)

    @_decorator.tagger  # error
    def e(self) -> None:
        """
        TODO: Добавить описание функции e
        """
        self.message = '-ERROR- ' + self.message
        _printer(self)

    @_decorator.tagger  # info
    def i(self) -> None:
        """
        TODO: Добавить описание функции i
        """
        self.message = '-INFO- ' + self.message
        _printer(self)

    @_decorator.tagger  # settings
    def s(self) -> None:
        """
        TODO: Добавить описание функции s
        """
        self.message = '-SETINGS-' + self.message
        _printer(self)

    @_decorator.tagger  # warning
    def w(self) -> None:
        """
        TODO: Добавить описание функции w
        """
        self.message = '-WARNING- ' + self.message
        _printer(self)

    @_decorator.tagger  # critical
    def c(self) -> None:
        """
        TODO: Добавить описание функции c
        """
        self.message = '-CRITICAL- ' + self.message
        _printer(self)


def _printer(self):
    """
    TODO: Добавить описание функции _printer
    """
    console_output = f'{self.time} {self.message}' if self.console_enabled and self.date_in_console else self.message
    if self.console_enabled:
        print(console_output)
    if self.file_enable:
        file_output = f'{self.time} {self.message}' if self.file_enable and self.date_in_file else self.message
        with open(self.file, "a", encoding='utf-8') as f:
            f.write(f'{file_output}\n')

from datetime import datetime
__autor__ = 'N0rmalUser'
__version__ = '0.2'

def _tagger(func):
    def wrapper(self, *args):
        message = ' '.join(str(arg) + (':' if i != len(args) - 1 else '') for i, arg in enumerate(args))
        self.message = message
        return func(self)
    return wrapper

def _printer(self):
    console_output = f'{self.time} {self.message}' if self.console_enabled and self.date_in_console else self.message
    if self.console_enabled:
        print(console_output)
    if self.file_enable:
        file_output = f'{self.time} {self.message}' if self.file_enable and self.date_in_file else self.message
        with open(self.file, "a", encoding='utf-8') as f:
            f.write(f'{file_output}\n')

class help():
    """Подробная информация о функциях модуля"""
    def __init__(self):
        print('Методы класса Logger:\ndebug -> d\nerror -> e\ninfo -> ai\nsettings -> s\nwarning -> w\ncritical -> c')
    
class Logger(object):
    def __init__(self, file:str, console_enabled=True,  datetime_format='%d.%m.%Y %H:%M:%S',
        date_in_console=True, file_enable=True, date_in_file=True):
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
        
    @_tagger # debug
    def d(self) -> None:
        self.message = '-DEBUG-' + self.message
        _printer(self)
    
    @_tagger # error
    def e(self) -> None:
        self.message = '-ERROR- ' + self.message
        _printer(self)
    
    @_tagger # info
    def i(self) -> None:
        self.message = '-INFO- ' + self.message
        _printer(self)

    @_tagger # settings
    def s(self) -> None:
        self.message = '-SETINGS-' + self.message
        _printer(self)

    @_tagger # warning
    def w(self) -> None:
        self.message = '-WARNING- ' + self.message
        _printer(self)

    @_tagger # critical
    def c(self) -> None:
        self.message = '-CRITICAL- '+ self.message
        _printer(self)
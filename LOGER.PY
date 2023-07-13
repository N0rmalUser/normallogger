from datetime import datetime
__autor__ = "N0rmalUser"
__version__ = "0.2"
__methods__ = ("DEBUG","ERROR","INFO","SETINGS","WARNING","CRITICAL")

def _tagger(func):
    def wrapper(self, *args):
        i=0
        message = ''
        while i < len(args):
            if i == len(args)-1:
                qwe = f'{args[i]}'
            else:
                qwe = f'{args[i]}:'
            message = message + str(qwe) + ' '
            i+=1
        self.message = message
        return func(self)
    return wrapper     

def _printer(self):
    if self.ConsoleEnable[1]:
        if self.DateConsole[1]:
            print(f'{self.time} {self.message}')
        else:
            print(self.message)
    with open(self.file[0], "a") as f:
        f.write(f'{self.time} {self.message}\n')

class help():
    """Подробная информация о функциях модуля"""
    def __init__():
        print('Методы класса Logger:\ndebug -> d\nerror -> e\ninfo -> i\nsettings -> s\nwarning -> w\ncritical -> c')

def _qqq(var,int,name):
    if not isinstance(var, int):
        raise TypeError(f"{name} должно быть {int}")
    


class logger():
    def __init__(self, *logfile:str, ConsoleEnable = True, DateTimeFormat = "%d.%m.%Y %H:%M:%S", DateInConsole = True, UseError = True):
        """Методы класса Logger: debug -> d, error -> e, info -> i, settings -> s, warning -> w """
        _qqq(ConsoleEnable,bool,'ConsoleEnable')
        if not isinstance(ConsoleEnable|DateInConsole|UseError, bool):
            raise TypeError("Значение должно быть булевым")
        self.file = logfile 
        self.time = datetime.now().strftime(DateTimeFormat)
        self.ConsoleEnable = "ConsoleEnable", ConsoleEnable
        self.DateConsole = "DateInConsole", DateInConsole
        self.UseError = "UseError", UseError

    def help(self) -> None:
        print('Методы класса Logger:\ndebug -> d\nerror -> e\ninfo -> i\nsettings -> s\nwarning -> w\ncritical -> c')

    @_tagger # debug
    def d(self) -> None:
        self.message = f'-DEBUG- {self.message}'
        _printer(self)
    
    @_tagger # error
    def e(self) -> None:
        self.message = f'-ERROR- {self.message}'
        _printer(self)
    
    @_tagger # info
    def i(self) -> None:
        self.message = f'-INFO- {self.message}'
        _printer(self)

    @_tagger # settings
    def s(self) -> None:
        self.message = f'-SETINGS- {self.message}'
        _printer(self)

    @_tagger # warning
    def w(self) -> None:
        self.message = f'-WARNING- {self.message}'
        _printer(self)

    @_tagger # warning
    def c(self, *message) -> None:
        self.message = f'-CRITICAL- {self.message}'
        _printer(self)



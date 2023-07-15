class _decorator(object):
    """
    TODO: добавить описание класса _decorator
    """
    def tagger(func):
        """
        TODO: добаввить описание tagger
        """
        def wrapper(self, *args):
            message = ' '.join(str(arg) + (':' if i != len(args) - 1 else '') for i, arg in enumerate(args))
            self.message = message
            return func(self)
        return wrapper

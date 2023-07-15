class _decorator(object):
    """
    The inner class _decorator represents a decorator that adds a tag to the message.
    """
    def tagger(func):
        """
        The inner decorator function tagger takes a function and adds a tag to the message.
        """
        def wrapper(self, *args):
            message = ' '.join(str(arg) + (':' if i != len(args) - 1 else '') for i, arg in enumerate(args))
            self.message = message
            return func(self)
        return wrapper

class Secret:
            def __init__(self):
              self._secret=99
              self.__top_secret=100


x=Secret()

x._secret

x.__top_secret

x._Secret__top_secret
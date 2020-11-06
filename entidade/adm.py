

class Adm:
    def __init__ (self):
        self.__login = "adm"
        self.__senha = "bobi"

    @property
    def login (self):
        return self.__login

    @property
    def senha (self):
        return self.__senha
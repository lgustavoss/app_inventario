class Colaborador():
    def __init__(self, nome, cpf, status):
        self.__nome = nome
        self.__cpf = cpf
        self.__status = status

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__cpf = status

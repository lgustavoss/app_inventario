class Empresa():
    def __init__(self, nome, cnpj, status):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__status = status

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

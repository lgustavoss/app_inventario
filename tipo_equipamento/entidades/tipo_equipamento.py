class TipoEquipamento():
    def __init__(self, tipo, status):
        self.__tipo = tipo
        self.__status = status

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

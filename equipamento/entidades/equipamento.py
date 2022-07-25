class Equipamento():
    def __init__(self, tag_patrimonio, tipo_equipamento, pedido, data, situacao, empresa, colaborador,
                marca, modelo, especificacoes, acesso_remoto, acesso_id, acesso_senha, observacao, status):
        self.__tag_patrimonio = tag_patrimonio
        self.__tipo_equipamento = tipo_equipamento
        self.__pedido = pedido
        self.__data = data
        self.__situacao = situacao
        self.__empresa = empresa
        self.__colaborador = colaborador
        self.__marca = marca
        self.__modelo = modelo
        self.__especificacoes = especificacoes
        self.__acesso_remoto = acesso_remoto
        self.__acesso_id = acesso_id
        self.__acesso_senha = acesso_senha
        self.__observacao = observacao
        self.__status = status

    @property
    def tag_patrimonio(self):
        return self.__tag_patrimonio

    @tag_patrimonio.setter
    def tag_patrimonio(self, tag_patrimonio):
        self.__tag_patrimonio = tag_patrimonio

    @property
    def tipo_equipamento(self):
        return self.__tipo_equipamento

    @tipo_equipamento.setter
    def tipo_equipamento(self, tipo_equipamento):
        self.__tipo_equipamento = tipo_equipamento

    @property
    def pedido(self):
        return self.__pedido

    @pedido.setter
    def pedido(self, pedido):
        self.__pedido = pedido

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def situacao(self):
        return self.__situacao

    @situacao.setter
    def situacao(self, situacao):
        self.__situacao = situacao

    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, empresa):
        self.__empresa = empresa

    @property
    def colaborador(self):
        return self.__colaborador

    @colaborador.setter
    def colaborador(self, colaborador):
        self.__colaborador = colaborador

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def especificacoes(self):
        return self.__especificacoes

    @especificacoes.setter
    def especificacoes(self, especificacoes):
        self.__especificacoes = especificacoes

    @property
    def acesso_remoto(self):
        return self.__acesso_remoto

    @acesso_remoto.setter
    def acesso_remoto(self, acesso_remoto):
        self.__acesso_remoto = acesso_remoto

    @property
    def acesso_id(self):
        return self.__acesso_id

    @acesso_id.setter
    def acesso_id(self, acesso_id):
        self.__acesso_id = acesso_id

    @property
    def acesso_senha(self):
        return self.__acesso_senha

    @acesso_senha.setter
    def acesso_senha(self, acesso_senha):
        self.__acesso_senha = acesso_senha

    @property
    def observacao(self):
        return self.__observacao

    @observacao.setter
    def observacao(self, observacao):
        self.__observacao = observacao

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

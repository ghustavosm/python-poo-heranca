class Pessoa:
    def __init__(self, nome, cpf, data_nasc):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nasc = data_nasc

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
    def data_nasc(self):
        return self.__data_nasc

    @cpf.setter
    def data_nasc(self, data_nasc):
        self.__data_nasc = data_nasc

    def __str__(self):
        return f'Nome: {self.__nome}\nCPF: {self.__cpf}\nData de nascimento: {self.__data_nasc}'
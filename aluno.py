from pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, nome, cpf, data_nasc, matricula):
        super().__init__(nome, cpf, data_nasc)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    def __str__(self):
        return f'{super().__str__()}\nMatricula: {self.__matricula}'
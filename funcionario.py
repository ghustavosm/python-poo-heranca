from pessoa import Pessoa

class Funcionario(Pessoa):

    def __init__(self, nome, cpf, data_nasc, matricula, data_admissao, salario):
        super().__init__(nome, cpf, data_nasc)
        self.__matricula = matricula
        self.__data_admissao = data_admissao
        self.__salario = salario

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def data_admissao(self):
        return self.__data_admissao

    @data_admissao.setter
    def data_admissao(self, data_admissao):
        self.data_admissao = data_admissao

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.salario = salario

    def __str__(self):
        return f'{super().__str__()}\nMatricula: {self.__matricula}\nDada de admissão: {self.__data_admissao}\nSalário: {self.__salario}'
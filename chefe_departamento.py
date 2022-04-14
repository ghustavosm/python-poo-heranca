from funcionario import Funcionario

class ChefeDepartamento(Funcionario):

    def __init__(self, nome, cpf, data_nasc, matricula, data_admissao, salario, departamento, data_promocao, gratificacao):
        super().__init__(nome, cpf, data_nasc, matricula, data_admissao, salario)
        self.__departamento = departamento
        self.__data_promocao = data_promocao
        self.__gratificacao = gratificacao

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, departamento):
        self.__departamento = departamento

    @property
    def data_promocao(self):
        return self.__data_promocao

    @data_promocao.setter
    def data_promocao(self, data_promocao):
        self.__data_promocao = data_promocao

    @property
    def gratificacao(self):
        return self.__gratificacao

    @gratificacao.setter
    def gratificacao(self, gratificacao):
        self.__gratificacao = gratificacao

    def __str__(self):
        return f'{super().__str__()}\nDepartamento: {self.__departamento}\nData de promocao: {self.__data_promocao}\nGratificação: {self.__gratificacao}'
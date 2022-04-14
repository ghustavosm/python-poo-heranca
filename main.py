from pessoa import Pessoa
from aluno import Aluno
from funcionario import Funcionario
from chefe_departamento import ChefeDepartamento

if __name__ == '__main__':
    pessoas = []

    pessoa = Pessoa('Maria', '12345678912', '01/01/1990')
    pessoas.append(pessoa)

    aluno = Aluno('João', '12345678913', '01/01/1991', 1234567)
    pessoas.append(aluno)

    funcionario = Funcionario('José', '12345678914', '01/01/1992', 1234568, '22/01/2021', 1500)
    pessoas.append(funcionario)

    chefe_departamento = ChefeDepartamento('Gustavo', '12345678915', '01/01/1992', 1234569, '22/01/2021', 2500, 'Computação', '22/05/2021', 500)
    pessoas.append(chefe_departamento)

    print('Listagem de pessoas:')
    for pessoa in pessoas:
        print(f'{pessoa}\n')
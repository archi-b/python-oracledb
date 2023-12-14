import os
import pandas
from business.pessoaBusiness import PessoaBusiness

if __name__ == '__main__':
    pessoa = PessoaBusiness()
    pessoa.importAndSavePessoa()
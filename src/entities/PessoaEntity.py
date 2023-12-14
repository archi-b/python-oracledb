
class PessoaEntity():

    @property
    def id_arquivo(self):
        return self.__id_arquivo

    @property
    def cnpj_cpfusufinalrecbdr_titlar(self):
        return self.__cnpj_cpfusufinalrecbdr_titlar

    @property
    def cnpjcreddrsub(self):
        return self.__cnpjcreddrsub

    @property
    def cnpjfincdr(self):
        return self.__cnpjfincdr

    @property
    def codinstitdrarrajpgto(self):
        return self.__codinstitdrarrajpgto

    @property
    def dtoptin(self):
        return self.__dtoptin

    @property
    def dtinioptin(self):
        return self.__dtinioptin

    @id_arquivo.setter
    def id_arquivo(self, value):
        self.__id_arquivo = value
        
    @cnpj_cpfusufinalrecbdr_titlar.setter
    def cnpj_cpfusufinalrecbdr_titlar(self, value):
        self.__cnpj_cpfusufinalrecbdr_titlar = value
        
    @cnpjcreddrsub.setter
    def cnpjcreddrsub(self, value):
        self.__cnpjcreddrsub = value
        
    @cnpjfincdr.setter
    def cnpjfincdr(self, value):
        self.__cnpjfincdr = value
        
    @codinstitdrarrajpgto.setter
    def codinstitdrarrajpgto(self, value):
        self.__codinstitdrarrajpgto = value
        
    @dtoptin.setter
    def dtoptin(self, value):
        self.__dtoptin = value
        
    @dtinioptin.setter
    def dtinioptin(self, value):
        self.__dtinioptin = value

    def __init__(self):
        self.id_arquivo = None
        self.cnpj_cpfusufinalrecbdr_titlar = None
        self.cnpjcreddrsub = None
        self.cnpjfincdr = None
        self.codinstitdrarrajpgto = None
        self.dtoptin = None
        self.dtinioptin = None

    def to_dict(self):
        return {
            'id_arquivo': self.id_arquivo,
            'cnpj_cpfusufinalrecbdr_titlar': self.cnpj_cpfusufinalrecbdr_titlar,
            'cnpjcreddrsub': self.cnpjcreddrsub,
            'cnpjfincdr': self.cnpjfincdr,
            'codinstitdrarrajpgto': self.codinstitdrarrajpgto,
            'dtoptin': self.dtoptin,
            'dtinioptin': self.dtinioptin
        }

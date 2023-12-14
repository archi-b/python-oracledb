import os
import pandas as panda

class ImportCsvFile:

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        self.__data = value

    def __init__(self):
        file = os.getenv("input_file_csv")
        self.data = panda.read_csv(file, sep=';', skiprows=1, header=None)
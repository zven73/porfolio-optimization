import pandas as pd

class file_repository:

    def __init__(self, directory):
        self.__writer = pd.ExcelWriter(directory, engine='xlsxwriter')

    def save_to_file(self, data, sheet_name=None):
        data.to_excel (self.__writer, sheet_name=sheet_name, header=True)

    def save_to_file_transposed(self, data, sheet_name=None):
        data_transposed = data.T
        print(data_transposed)
        data_transposed.to_excel (self.__writer, sheet_name=sheet_name, header=True)

    def close(self):
        self.__writer.save()

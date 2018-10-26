import pandas as pd

class data_input():

    def __init__(self):
        self.data = None

    def _data_input(self):

        _data = pd.read_csv('data.csv')
        self.data = _data
        return self.data
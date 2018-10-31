import warnings
warnings.filterwarnings('ignore')
from Data_Input import data_input

class data_process_function():

    def __init__(self):
        self._ = data_input()
        self.data = self._._data_input()

    def basic_cleaning(self,data):
        data = data.drop_duplicates(['group_id', 'estate_id', 'final_status'], keep = 'first')
        data = data.fillna(0.0)
        return data

    def Fix_Price1(self, asking_price, final_price, final_status):
        if asking_price == 0 and final_status == 'Contract Signed':
            asking_price = final_price
        else:
            asking_price = asking_price
        return asking_price

    # Filling asking_price == 0 and final_status == 'Sold' #
    def Fix_Price2(self,data):
        asking_0_id = list(data[(data.asking_price == 0) & (data.final_status == 'Sold')].estate_id)
        for i in asking_0_id:
            p = list(data[(data.estate_id == i) & (data.final_status == 'Contract Signed')]['asking_price'])
            if p:
                data.ix[(data.estate_id == i) & (data.final_status == 'Sold'), 'asking_price'] = p[0]
            else:
                data.ix[(data.estate_id == i) & (data.final_status == 'Sold'), 'asking_price'] = 0.0
        return data

    ## Filling final_price == 0 and  final_status == 'Contract Signed'
    def Fix_Price3(self,asking_price, final_price, final_status):
        if final_price == 0 and final_status == 'Contract Signed':
            final_price = asking_price
        else:
            final_price = final_price
        return final_price

    ## Filling final_price == 0 and final_status == 'Sold'
    def Fix_Price4(self,data):
        final_0_id = list(data[(data.final_price == 0) & (data.final_status == 'Sold')].estate_id)
        for i in final_0_id:
            p = list(data[(data.estate_id == i) & (data.final_status == 'Contract Signed')]['final_price'])
            if p:
                data.ix[(data.estate_id == i) & (data.final_status == 'Sold'), 'final_price'] = p[0]
            else:
                data.ix[(data.estate_id == i) & (data.final_status == 'Sold'), 'final_price'] = 0.1
        return data

    ## Fixing abnomal values in asking_price
    def Fix_Price5(self,asking_price, final_price):
        diff = len(str(final_price)) - len(str(asking_price))
        if diff > 1:
            asking_price = asking_price * (10 ** diff)
        else:
            asking_price = asking_price
        return asking_price

    ## Fixing abnomal values in final_price
    def Fix_Price6(self,asking_price, final_price):
        diff = len(str(final_price)) - len(str(asking_price))
        if diff < -1:
            final_price = final_price * (10 ** abs(diff))
        else:
            final_price = final_price
        return final_price


    def _start(self):
        self.data = self.basic_cleaning(self.data)
        self.data['asking_price'] = self.data.apply(lambda row: self.Fix_Price1(row['asking_price'],row['final_price'], row['final_status']), axis=1)
        self.data = self.Fix_Price2(self.data)
        self.data['final_price'] = self.data.apply(lambda row: self.Fix_Price3(row['asking_price'],row['final_price'], row['final_status']), axis=1)
        self.data = self.Fix_Price4(self.data)
        self.data = self.data[(self.data.asking_price != 0) | (self.data.final_price != 0)]
        self.data['asking_price'] = self.data.apply(lambda row: self.Fix_Price5(row['asking_price'],row['final_price']), axis=1)
        self.data['final_price'] = self.data.apply(lambda row: self.Fix_Price6(row['asking_price'],row['final_price']), axis=1)
        return self.data

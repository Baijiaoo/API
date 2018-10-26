from Data_Processing import data_process_function
import warnings
warnings.filterwarnings('ignore')

class final_cleaning():

    def __init__(self):
        self._ = data_process_function()
        self.data = self._._start()

    def merging_data(self):
        data_sign = self.data[self.data.final_status == 'Contract Signed']
        data_sold = self.data[self.data.final_status == 'Sold']
        data_merge = data_sign.merge(data_sold, on=['group_id', 'estate_id'], how='left')

        columns = ['agent_id_x', 'brokerage_name_x','final_price_x','agent_id_y','brokerage_name_y','listing_create_date_y','asking_price_y']
        data_merge.drop(columns, inplace=True, axis=1)
        data_merge.columns = ['group_id','property_id','listing_create_date','asking_price','status_1','final_price','status_2']
        data_merge['final_price'] = data_merge['final_price'].fillna(0.0)
        data_merge['status_2'] = data_merge['status_2'].fillna('Fail')
        data_merge['price_differences'] = data_merge.ix[:, 'final_price'] - data_merge.ix[:, 'asking_price']

        return data_merge

    def Date_Modification(self,date):
        date = str(date)
        date = date[0:10]
        return date

    def start(self):
        from datetime import datetime

        data_merge = self.merging_data()
        data_merge['listing_create_date'] = data_merge.loc[:, 'listing_create_date'].apply(lambda x: self.Date_Modification(x))
        data_merge['listing_create_date'] = data_merge.loc[:, 'listing_create_date'].apply(lambda x: datetime.strptime(str(x), '%Y-%m-%d'))
        return data_merge
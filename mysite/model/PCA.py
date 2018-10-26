import pandas as pd
import numpy as np
from Data_Merging import final_cleaning
import warnings
warnings.filterwarnings('ignore')

class pca():

    def __init__(self):
        self._ = final_cleaning()
        self.data = self._.start()

    def Create_Features(self,data):

        a = data.set_index(['listing_create_date'], inplace=False)

        # Every quarter total property price agent sold out
        a_1 = a[a.status_2 == 'Sold']['final_price'].resample('Q').sum()

        # Every quarter the rise of total property price comparing with the last year
        a_3 = pd.DataFrame(np.array(a_1[1:]) - np.array(a_1[:-1]), columns=['money_rise_up'])
        a_3.index = a_1.index[1:]

        # Every quarter total differences of property price between asking_price and listing_price
        a_4 = a['price_differences'].resample('Q').sum()

        # Every quarter number of cumstomers sign the contract
        a_5 = a['status_1'].resample('Q').size()

        # Every quarter number of customers buy the estate finally
        a_6 = a['status_2'].resample('Q').size()

        # Every quarter average property price agent sold out
        a_2 = a_1 / a_6

        # Transactioin Conversion percentage
        a_7 = a_6 / a_5 * 100

        result = pd.concat((a_4, a_5, a_6, a_1, a_3, a_7, a_2), axis=1).fillna(0.1)
        columns = result.columns.tolist()
        for col in columns:
            d_ = result[col]
            MAX = d_.max()
            MIN = d_.min()
            result[col] = ((d_ - MIN) / (MAX - MIN)).tolist()
        result = result.reset_index(drop=False)
        result = result.fillna(0.1)

        return result

    def PCA(self, data):
        from sklearn.decomposition import PCA
        import pandas as pd
        import numpy as np

        data_ = data.drop(columns=['listing_create_date'], inplace=False)
        X = np.array(data_)
        n = min(len(X), len(X[0]))
        pca = PCA(n_components=n)
        pca.fit(X)

        component = pca.components_
        variance_ratio = pca.explained_variance_ratio_
        component = abs(component.T)

        for i in range(0, n):
            component[:, i] = variance_ratio[i] * component[:, i]
        a = pd.DataFrame(component)
        b = a.sum(axis=1)
        c = b / b.sum(axis=0)
        for i in range(0, len(data_.loc[0, :])):
            data_.ix[:, i] = data_.ix[:, i].apply(lambda x: x * c[i])
        data_['grade'] = 0.0
        for i in range(0, len(data_.loc[:, 0])):
            data_['grade'][i] = data_.ix[i, :].sum()
        final_data = data_['grade']

        return final_data

    def Last_Cleaning(self, data):
        cols = ['grade', 'Ave_Price', 'Conver_Percentage', 'money_rise_up',
                'price_differences', 'final_price', 'listing_create_date', 'group_id']
        data.drop(columns=['Contract_Signed', 'Sold'], inplace=True)
        for i in cols:
            data_i = data.ix[:, i]
            data.drop(columns=i, inplace=True)
            data.insert(0, i, data_i)
        data.columns = ['Group_ID', 'Date', 'Total_Sold_Price', 'Price_Diff', 'Rise_UP','Ave_Price', 'Conver_Percentage', 'Grade']
        data_ = data[['Date','Group_ID','Grade']]
        return data_

    def start(self):
        import pandas as pd

        group_id = list(self.data.group_id.unique())

        df = pd.DataFrame(columns=['listing_create_date', 'price_differences', 'Contract_Signed', 'Sold',
                                   'final_price', 'money_rise_up', 'Ave_Price', 'Conver_Percentage', 'grade','group_id'])
        for i in group_id:
            data_input_1 = self.data[self.data.group_id == i]
            data_input_2 = self.Create_Features(data_input_1)
            data_grade = self.PCA(data_input_2)
            data_output_1 = pd.concat((data_input_2, data_grade), axis=1)
            data_output_1['group_id'] = str(i)
            data_output_1.columns = ['listing_create_date', 'price_differences', 'Contract_Signed','Sold','final_price','money_rise_up','Ave_Price','Conver_Percentage','grade','group_id']
            df = df.append(data_output_1)

        data_output = self.Last_Cleaning(df)
        data_output = data_output.set_index('Date')
        return data_output




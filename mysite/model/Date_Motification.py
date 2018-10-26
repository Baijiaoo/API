class date_motify():

    def __init__(self):
        from Data_Merging import final_cleaning
        self._ = final_cleaning()
        self.data = self._.merging_data()

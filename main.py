import pandas as pd

class Portfolio:

    def __init__(self, assets_list, past_data=None):
        self.assets_list = assets_list
        self.past_data = past_data

    def retrieve_past_data(self, length):
        pass
        # list_of_list
        # self.past_data = pd.DataFrame()
        # for ticker in self.assets_list:
        #     self.past_data. = yf.download(self.ticker, start=str(date.today()- timedelta(days=length)), end=str(date.today()), auto_adjust=True)
        # return self


from sklearn.decomposition import PCA
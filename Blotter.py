import pandas as pd
class Blotter:
    #default constructor
    def __init__(self, df):
        self.Data = df
    #method determines if data can be formed into a blotter (boolean)
    def isBlotter(self):
        x = 0
        cols = self.Data.columns
        if 'Date/Time' not in cols:
            print('Error: No Date/Time Column')
            x+=1
        for index, row in self.Data.iterrows():
            if (row["Action"] != 'BUY' and row["Action"]!= 'SELL'):
                print(row["Action"])
                print('Error: Action Must be BUY or SELL')
                x+=1
            if isinstance(row["Price"],str):
                if row["Price"].isnumeric() == False:
                    print(row["Price"])
                    print('Error: Price Must be Numeric')
                    x+=1
            else:
                if isinstance(row["Price"], (int, float)) == False:
                    print(row["Price"])
                    print('Error: Price Must be Numeric')
                    x+=1
        if x == 0:
            print('This is a Blotter')
            return True
        else:
            print('This is Not a Blotter')
            return False
data = pd.read_csv('testdata.csv')
df = Blotter(data)
print(df.isBlotter())
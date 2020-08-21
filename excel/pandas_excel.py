import pandas as pd
from pandas import DataFrame


# Read excel
df = pd.read_excel(r'.\excel\data_read.xlsx',sheet_name=0)

print(df.head())

#Write excel
data = {
    'name':['A','B','C'],
    'age':[11,12,13],
    'sex':['male','female','male']
}

df = DataFrame(data)
df.to_excel(r'.\excel\data_write.xlsx')

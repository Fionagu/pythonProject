import pandas as pd

col_labels = pd.Index(['name','age','alary'])
print(col_labels, type(col_labels))

row_labels = pd.Index(['ID'+str(i) for i in range(1,3)])
print(row_labels, type(row_labels))

lname = pd.Series(data=['Hunt','Smith'], 
            name='Last Name', index=row_labels)
print(lname,type(lname),type(lname.index.))
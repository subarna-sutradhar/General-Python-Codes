import pandas as pd
df1=pd.read_csv("cars01.csv")
df2=pd.read_csv("cars02.csv")
df=df1.merge(df2,on='Company')
print(df)
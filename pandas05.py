import pandas as pd
data = [{'name': 'aa', 'email': 'ss@ww'},{'name': 'yy', 'email': 'ww@qq', 'mobile': 2009}]
df = pd.DataFrame(data, index=['001', '002'])
print(df)
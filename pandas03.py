import pandas as pd
data = [['Subarna','subarna@gmail.com'],['Debanshu','debanshu@gmail.com'],['Ahana','ahana@gmail.com']]
df = pd.DataFrame(data,columns=['Name','Email Address'])
print(df)
import csv
fields = ['Company','Model','RatePerHour']
rows = [ ['Telsa','2019 Model 3','56'],['Volvo','2020 XC 60','59'],['BMW','2019 BMW 5 Series','62']]
filename = "mynewcarmaster.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
    csvfile.close()

import pandas as pd
df=pd.read_csv(filename)
print(df)
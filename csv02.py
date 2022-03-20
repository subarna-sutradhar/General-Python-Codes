"""Code for the second one that will create cars02.csv"""
#------------------------------------------------------------------------
import csv 
fields = ['Company','RatePerHour'] 
rows = [ ['Lexus','67'],['Mercedes','75'],['Audi','100']] 
filename = "cars02.csv"
with open(filename, 'w') as csvfile: 
	csvwriter = csv.writer(csvfile) 
	csvwriter.writerow(fields) 
	csvwriter.writerows(rows)
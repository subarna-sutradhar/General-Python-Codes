"""Code for the first one that will create cars01.csv"""
#------------------------------------------------------------------
import csv 
fields = ['Company','Model'] 
rows = [ ['Lexus','2020 LS'],['Mercedes','2019 Mercedes S Class'],['Audi','2019 Audi A8']] 
filename = "cars01.csv"
with open(filename, 'w') as csvfile: 
	csvwriter = csv.writer(csvfile) 
	csvwriter.writerow(fields) 
	csvwriter.writerows(rows)
#import Modules
import os
import csv

#Define Variables
month_count = 0
net_revenue = 0
profit = 0
max_rev = 0
min_rev = 0
monthly_change = 0

#create lists
month = []
revenue = []
avg_Chnage = []

#location of resources
data_csv = os.path.join("Resources", "budget_data.csv")
with open(data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

#Find headers
    csv_header = next(csvreader)
    firstrow = next(csvreader) 
    rowbefore = (int(firstrow[1]))

    revenue.append(int(firstrow[1]))

#Create for loop to loop through data
    for row in csv_reader:
        #count the months
        month_count = month_count +1

        #Revenue
        revenue.append(row[1])
        #month
        month.append(row[0])
        #Avg_change
        avg_Chnage.append(row[1])

max_rev = revenue.max()
min_rev = revenue.min()
monthly_change = 

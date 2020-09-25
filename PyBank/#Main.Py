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
dates = []
revenue = []

#location of resources
data_csv = os.path.join("Resources", "budget_data.csv")
with open(data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

#Read headers
    csv_header = next(csvreader)

#Read First Row
    firstrow = next(csvreader) 
    month_count += 1
    net_revenue += int(firstrow[1])
    profit = int(firstrow[1])

#Create for loop to loop through data
    for row in csv_reader:
        
        #add date to list
        dates.append(row[0])
        
        #Add count for row to represent month
        month_count += 1

        # Calc Profit/loss and add to list
        monthly_change = int(row[1]-profit)
        revenue.append(monthly_change)
        profit = (int(row[1]))

        # Total Net Profit/Loss
        net_revenue = net_revenue + int(row[1])

#Greatest Profit
max_rev = max(net_revenue)
max_index = net_revenue.index(max_rev)
Max_date = dates[max_index]

#Greatest Loss
min_rev = min(net_revenue)



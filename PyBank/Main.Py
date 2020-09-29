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
data_csv = os.path.join( "Resources", "budget_data.csv")
with open(data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

#Read headers
    csv_header = next(csv_reader)

#Read First Row
    firstrow = next(csv_reader) 
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
        monthly_change = int(row[1]) - profit
        revenue.append(monthly_change)
        profit = (int(row[1]))

        # Total Net Profit/Loss
        net_revenue = net_revenue + int(row[1])

#Greatest Profit
max_rev = max(revenue)
max_index = revenue.index(max_rev)
max_date = dates[max_index]

#Greatest Loss
min_rev = min(revenue)
min_index = revenue.index(min_rev)
min_date = dates[min_index]

#Average Profti/Loss
avg_profit = sum(revenue)/len(revenue)

#Setup output strings
report= (
f"Financial Analysis\n"
f"---------------------------\n"
f"Total Months: {str(month_count)}\n"
f"Total Funds: ${str(net_revenue)}\n"
f"Average Change: ${str(round(avg_profit,2))}\n"
f"Greatest Increase in Profits: {max_date} (${str(max_rev)})\n"
f"Greatest Decrease in Profits: {min_date} (${str(min_rev)})\n"
)

print(report)

#Set output path
output_txt = os.path.join('output.txt')

#output file
with open(output_txt, 'w') as txtfile:
    txtwriter = txtfile.write(report)
    txtfile.close()
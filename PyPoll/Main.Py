#import Modules
import os
import csv
import numpy as np

# Define the variables
votes = []
total_votes = 0
candidates =[]
cand_count = 0


# Path of data file
data_csv = os.path.join( "Resources", "election_data.csv")
with open(data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

#Read headers
    csv_header = next(csv_reader)

#Read First Row
    firstrow = next(csv_reader) 


#Create a lopop to read the voting data
    for row in csv_reader:
        
        #add candidate to list
        votes.append(row[2])

        #add vote for row to running count
        total_votes = total_votes + 1

# Unique candidate list
#candidates = (votes).Unique
print(total_votes)

candidates = np.Unique([votes])
print(candidates)

# vote count
#cand_count = ()
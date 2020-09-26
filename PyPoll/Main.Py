#import Modules
import os
import csv

# Define the variables
total_votes = 0
candidates =[]
cand_count = 0
cand_votes = []
percent_votes = []


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

        #Add to unique list
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index (row[2])
            cand_votes.append(1)
        else:
            index = candidates.index(row[2])
            cand_votes[index] +=1

        #add vote for row to running count
        total_votes = total_votes + 1

#Calculate percentage of total votes for each candidate
for votes in cand_votes:
    percent = round(votes/total_votes)
    percent_votes.append(percent)

#Find Winning Candidate
winner = max(cand_votes)
index = cand_votes.index(winner)
winning_cand = candidates[index]

print(winning_cand)

print(total_votes)
print(candidates)

# vote count

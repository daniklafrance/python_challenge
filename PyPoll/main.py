#import dependencies
import os
import csv

#path to data file
csvpath = os.path.join('Resources', 'election_data.csv')

#create lists/dictionaries for data
ballotid = []
candlist = []
candvote = {}

#open and read the data file
with open(csvpath, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvfile)

#loop the rows 
    for row in csvreader:

#count total votes by adding each row to a list and then counting the length of the list
        ballotid.append(row[0])
        votes = len(ballotid)

#create list of candidates and count their votes, if the name isn't in the list, add the name to the list
#count the votes for each candidate, if the candidate is in the list, count their name as a vote in the dictionary
        candname = row[2]

        if candname not in candlist:
            candlist.append(candname)
            candvote[candname] = 0

        else: candvote[candname] += 1

#calculate the percentages of each candidate based on the dictionary data found
perc0 = 100 * (candvote[candlist[0]] / votes)
perc0 = int(perc0)

perc1 = 100 * (candvote[candlist[1]] / votes)
perc1 = int(perc1)

perc2 = 100 * (candvote[candlist[2]] / votes)
perc2 = int(perc2)

#calculate the winner by finding the highest vote number in the candidatevote dictionary
winner = max(candvote, key=candvote.get)

#print the analysis to the terminal
print('Election Results')
print("----------------------------")
print('Total Votes:', votes)
print("----------------------------")
print(candlist[0],':', perc0,'%', '(',candvote[candlist[0]],')')
print(candlist[1],':', perc1,'%', '(',candvote[candlist[1]],')')
print(candlist[2],':', perc2,'%', '(',candvote[candlist[2]],')')
print("----------------------------")
print('Winner:', winner)
print("----------------------------")

#export the file
exportfile = os.path.join('Analysis', 'main.txt')
with open(exportfile, 'w') as file:
    file.write(f'Election Results\n')
    file.write(f'----------------------------\n')
    file.write(f'Total Votes: {votes}\n')
    file.write(f'----------------------------\n')
    file.write(f'{candlist[0]}: {perc0}% ({candvote[candlist[0]]})\n')
    file.write(f'{candlist[1]}: {perc1}% ({candvote[candlist[1]]})\n')
    file.write(f'{candlist[2]}: {perc2}% ({candvote[candlist[2]]})\n')
    file.write(f'----------------------------\n')
    file.write(f'Winner: {winner}\n')
    file.write(f'----------------------------')
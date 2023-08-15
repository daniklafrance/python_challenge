#import dependencies
import os
import csv

#path to data file
csvpath = os.path.join('Resources', 'budget_data.csv')

#create lists for data from colums
profit = []
date = []
changes = []

#create variables to start the values at 0
lastmonth = 0
thismonth = 0
profitvar = 0

#open and read the data file
with open(csvpath, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvfile)

#loop the rows
    for row in csvreader:

#count total months by adding each row to a list and then counting the list
        date.append(row[0])
        months = len(date)
        
#count net amount by adding each months profit to a list and then adding the total amount
        profit.append(int(row[1]))
        totalprofit = sum(profit)

#if/else statement to calculate the changes in profit
        thismonth = int(row[1])

        if ():

#if the current month is equal to the previous month, continue to loop            
            lastmonth = thismonth
            continue

#and if they aren't, calculate the difference and add to a list and then reset by making this month the previous month
        else:

            profitvar = thismonth - lastmonth
            changes.append(profitvar)
            lastmonth = thismonth

#The changes in "Profit/Losses" over the entire period, and then the average of those changes (need to delete the first element of the list, value and month)
del changes[0]
totalchange = sum(changes)
averagechange = (totalchange/(months -1))
averagechange = int(averagechange)

#The greatest increase in profits (date and amount) over the entire period, find the highest number in all month to month changes       
maxprofit = max(changes)

#The greatest decrease in profits (date and amount) over the entire period, find the lowest number in all month to month changes
minprofit = min(changes)

#print the analysis to the terminal
print('Financial Analysis')
print("----------------------------")
print('Total Months:', months)
print('Total: $',totalprofit)
print('Average Change: $', averagechange )
print('Greatest Increase in Profits:', '($',maxprofit,')')
print('Greatest Decrease in Profits:', '($',minprofit,')')

#export the file
exportfile = os.path.join('Analysis', 'main.txt')
with open(exportfile, 'w') as file:
    file.write(f'Financial Analysis\n')
    file.write(f'----------------------------\n')
    file.write(f'Total Months: {months}\n')
    file.write(f'Total: $ {totalprofit}\n')
    file.write(f'Average Change: $ {averagechange}\n')
    file.write(f'Greatest Increase in Profits: (${maxprofit})\n')
    file.write(f'Greatest Decrease in Profits: (${minprofit})')
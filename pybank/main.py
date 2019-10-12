import os
import csv


revenue_changes  = []

pybankcsvpath = r'C:\Users\francisco.tangbustil\Documents\personal documents\Data analytics\Homework\homework_3\budget_data.csv'

#variables
nettotalammount = 0
totalmo = 0
previousrevenue = 0
firstrevenuecell = 867884 #number of the first cell.. This is the only variable that is fixed, and would need to be change if I analyzed another variable
max_revenue = 0
min_revenue = 0


#making calculations of total month, total profit, etc
with open(pybankcsvpath, newline='') as pybankfile:
    next(pybankfile, None)
    reader = csv.reader(pybankfile, delimiter = ',')
    for row in reader:
        totalmo += 1
        nettotalammount += int(row[1])

        revenue_change = int(row[1]) - previousrevenue
        previousrevenue = int(row[1])
        
        revenue_changes.append(revenue_change)
        

        if revenue_change > max_revenue:
            max_date = row[0]
            max_revenue = revenue_change

        if revenue_change < min_revenue:
            min_date = row[0]
            min_revenue = revenue_change

    #calculate total changes and average
    total_changes = sum(revenue_changes) - firstrevenuecell
    netaverage = (total_changes)/(totalmo - 1) # changes are one less than the total months
    
#format change
netaverage = "{:0.2f}".format(netaverage)

#print results
print("Financial Analysis")
print("--------------------------")
print(f'Total months: {totalmo}')
print(f'Total: ${nettotalammount}')
print(f'Averange change: ${netaverage}')
print(f'Greatest Increase in Profits: {max_date} (${max_revenue})')
print(f'Greatest Decrease in Profits: {min_date} (${min_revenue})')




#write results in csv file
path = "C:/Users/francisco.tangbustil/Documents/personal documents/Data analytics/Homework/homework_3/main.txt" 

file = open(path, 'w')

file.write("Financial Analysis\n")
file.write("--------------------------\n")
file.write(f'Total months: {totalmo}\n')
file.write(f'Total: ${nettotalammount}\n')
file.write(f'Averange change: ${netaverage}\n')
file.write(f'Greatest Increase in Profits: {max_date} (${max_revenue})\n')
file.write(f'Greatest Decrease in Profits: {min_date} (${min_revenue})\n')


import os
import csv


#naming the candidates.. this is the only variables that are fixed. I knew that this were the only ones due to the "candidate_list" 
firstcandidate = "Khan"
secondcandidate = "Correy"
thirdcandidate = "Li"
fourthcandidate = "O'Tooley"

#setting variables to 0
totalvote = 0
firstcandidatevotes = 0
secondcandidatevotes = 0
thirdcandidatevotes = 0
fourthcandidatevotes = 0
all_votes = []
candidate_list = []



pypollcsvpath = r'C:\Users\francisco.tangbustil\Documents\personal documents\Data analytics\Homework\homework_3\election_data.csv'


#calculating the total votes and the votes for each candidates
with open(pypollcsvpath, newline='') as pypollfile:
    next(pypollfile, None)
    reader = csv.reader(pypollfile, delimiter = ',')
    for row in reader:
        totalvote = totalvote + 1
        all_votes.append(row[2])
        
        if row[2] == firstcandidate:
            firstcandidatevotes += 1
        if row[2] == secondcandidate:
            secondcandidatevotes += 1
        if row[2] == thirdcandidate:
            thirdcandidatevotes += 1
        if row[2] == fourthcandidate:
            fourthcandidatevotes += 1
            

    #I got the candidates' name using the below function, and then printing it out
    for i in set(all_votes):
        candidate_list.append(i)


    # calculate percentage
    percentage_first = firstcandidatevotes / totalvote
    percentage_second = secondcandidatevotes / totalvote
    percentage_third = thirdcandidatevotes / totalvote   
    percentage_fourth = fourthcandidatevotes / totalvote

    # %c format
    percentage_first = "{:.3%}".format(percentage_first)
    percentage_second = "{:.3%}".format(percentage_second)
    percentage_third = "{:.3%}".format(percentage_third)
    percentage_fourth = "{:.3%}".format(percentage_fourth)


#determining the winner

if (percentage_first > percentage_second and percentage_first > percentage_third and percentage_first > percentage_fourth):
    winner = firstcandidate
elif (percentage_second > percentage_first and percentage_second > percentage_third and percentage_second > percentage_fourth):
    winner = secondcandidate
elif (percentage_third > percentage_first and percentage_third > percentage_second and percentage_third > percentage_fourth):
    winner = thirdcandidate
elif (percentage_fourth > percentage_first and percentage_fourth > percentage_second and percentage_fourth > percentage_third):
    winner = fourthcandidate




#print results
print("Election Results")
print("--------------------------")
print(f'Total Votes: {totalvote}')
print("--------------------------")
print(f"{firstcandidate}: {percentage_first} ({firstcandidatevotes})")
print(f"{secondcandidate}: {percentage_second} ({secondcandidatevotes})")
print(f"{thirdcandidate}: {percentage_third} ({thirdcandidatevotes})")
print(f"{fourthcandidate}: {percentage_fourth} ({fourthcandidatevotes})")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")

#print(candidate_list)  --> kept it, but commented it out as you don't ask for this.




#write results in csv file
pypollpath = "C:/Users/francisco.tangbustil/Documents/personal documents/Data analytics/Homework/homework_3/pypoll.txt" 

file = open(pypollpath, 'w')



    # Write the first row (column headers)
file.write(f"Election Results\n")
file.write(f"--------------------------\n")
file.write(f'Total Votes: {totalvote}\n')
file.write(f"--------------------------\n")
file.write(f"{firstcandidate}: {percentage_first} ({firstcandidatevotes})\n")
file.write(f"{secondcandidate}: {percentage_second} ({secondcandidatevotes})\n")
file.write(f"{thirdcandidate}: {percentage_third} ({thirdcandidatevotes})\n")
file.write(f"{fourthcandidate}: {percentage_fourth} ({fourthcandidatevotes})\n")
file.write("--------------------------\n")
file.write(f"Winner: {winner}\n")
file.write("--------------------------\n")




#Import the moduels
import os
import csv

#Set the path for csv file
election_csv = os.path.join('Resources', 'election_data.csv')

#Store data as lists
list_of_candidates = []
candidate = []
percentage_vote = []
num_votes = []

#Create variable and set it equal to zero
count = 0

#Read in csv file and declare header
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

#Begin the for loop    
    for row in csv_reader:
        
#Tally the total votes
        count = count + 1
        
#Add each candidate to the list of candidates
        list_of_candidates.append(row[2])
    
#We need to get only 3 candidates, so we need to find the unique names. We use the set function to do this
    for i in set(list_of_candidates):
        candidate.append(i)

#Calculate the number of votes for each candidate
        v = list_of_candidates.count(i)
        num_votes.append(v)
        
#Calculate the percentage of votes each candidate got and round to 3 decimal places
        x = round((v/count) * 100, 3)
        percentage_vote.append(x)
        
#Calculate the winning vote count
    winning_number = max(num_votes)

#From the winning vote count we can determine the winner using index function
    winning_candidate = candidate[num_votes.index(winning_number)]


#Print results to terminal
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(count))
for row in range(len(candidate)):
    print(candidate[row] + ": " + str(percentage_vote[row]) +"% (" +str(num_votes[row])+ ")")
print("-------------------------")
print("The Winner is: " + winning_candidate)
print("-------------------------")

#Write the text file with the final analysis
with open("Analysis/analysis.txt", "w") as out_file:
    out_file.write("Election Results")
    out_file.write("-------------------------")
    out_file.write("Total Votes: " + str(count))
    for row in range(len(candidate)):
        out_file.write(candidate[row] + ": " + str(percentage_vote[row]) +"% (" +str(num_votes[row])+ ")")
    out_file.write("-------------------------")
    out_file.write("The Winner is: " + winning_candidate)
    out_file.write("-------------------------")





     


    
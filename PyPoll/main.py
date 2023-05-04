import os
import csv

election_csv = os.path.join('Resources', 'election_data.csv')

count = 0
candidate = []
unique_candidate = []
percentage_vote = []
votes = []

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    
    for row in csv_reader:
        count = count + 1
        candidate.append(row[2])
    for i in set(candidate):
        unique_candidate.append(i)
        v = candidate.count(i)
        votes.append(v)
        x = round((v/count) * 100, 3)
        percentage_vote.append(x)
        

    win = max(votes)
    winning_candidate = unique_candidate[votes.index(win)]

    print("Total Votes: " + str(count))
    for i in range(len(unique_candidate)):
        print(unique_candidate[i] + ": " + str(percentage_vote[i]) +"% (" + str(votes[i])+ ")")
    print("The Winner is: " + winning_candidate)

        


    
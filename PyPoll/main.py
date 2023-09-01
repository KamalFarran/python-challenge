# Dependencies
import os
import csv

TotalVotes = 0
candidates = []
Output = []

#Specify the file path
csvPath = os.path.join("Resources", "election_data.csv")

#Open CSV file
with open(csvPath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    next(csvreader)

    #Loop through rows in the file
    for row in csvreader:

        newCandidate = True
        CandidateIndex = 0

        #Count the votes
        TotalVotes += 1

        #Get name of candidate who won the vote
        VoteFor = row[2]

        #Check if the candidate is already in list of dictionaries
        for candidate in candidates:
            if candidate["name"] == VoteFor:
                newCandidate = False
                break
            CandidateIndex += 1

        #If the candidate is already in the list, update the vote count
        if not newCandidate:
            candidates[CandidateIndex]["NumberOfVotes"] += 1
        #Else create a new dictionary for the candidate and add to the list
        else:
            addCandidate = {"name": VoteFor, "NumberOfVotes": 1 }
            candidates.append(addCandidate)


#Prepare output content
Output.append("Election Results")
Output.append("----------------------------")
Output.append(f'Total Votes: {TotalVotes}')
Output.append("----------------------------")

MaxVotes = 0
Winner = ""
for candidate in candidates:

    #For each candidate Calculate percentage of the vote for each candidate and user number of votes to get winner
    if candidate["NumberOfVotes"] > MaxVotes:
        MaxVotes = candidate["NumberOfVotes"]
        Winner = candidate["name"]
    Percentage = round(candidate["NumberOfVotes"]*100/TotalVotes, 3)
    Output.append(f'{candidate["name"]}: {Percentage}% ({candidate["NumberOfVotes"]})')

Output.append("----------------------------")
Output.append(f'Winner: {Winner}')
Output.append("----------------------------")

#Specify output path
OutputPath = os.path.join("analysis", "results.txt")

#Open output file
with open(OutputPath, "w") as OutputFile:

    #Print each line to the terminal and add it to the file
    for row in Output:
        print(row)
        OutputFile.write(row+'\n')
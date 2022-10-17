#import os and csv
import os
import csv

#set path for csv file to be read 
electionData_csv = os.path.join('Resources', 'election_data.csv')

#open csv
with open(electionData_csv) as csv_file:
   
    #read csv
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    #skip header row
    csv_header = next(csv_reader)

    #variables
    total_vote_count = 0

    #make empty dicts
    candidate_votes = {}
    percent_votes = {}

    #Loop through rows
    for row in csv_reader:

        #Objective 1: The total number of votes cast
        total_vote_count += 1

        #Objective 2: A complete list of candidates who received votes
            #candidates will be key from candidate_votes dict
        #Objective 4: The total number of votes each candidate won
            #candidate_votes[key] will bring up total votes for each candidate
       
        if row[2] in candidate_votes:
            candidate_votes[row[2]] += 1
        else:
            candidate_votes[row[2]] = 1

        #Objective 3: The percentage of votes each candidate won
        for key, votes in candidate_votes.items():
            percent_votes[key] = round((votes/total_vote_count)* 100 , 3)
        
        #Objective 5: The winner of the election based on popular vote.
        max_key = max(percent_votes, key=percent_votes.get)
        winner = max_key

    # print like example
    print(f"Election Results")
    print(f"----------------------------")
    print(f"Total Votes: {total_vote_count}")
    print(f"----------------------------")
    for key, votes in candidate_votes.items():
        print(key,':' , str(percent_votes[key]),'%','','(',candidate_votes[key],')')
    print(f"-------------------------")
    print(f"Winner: {winner}")
    print(f"-------------------------")

#write 'Election Results Analysis' to a txt file in 'Analysis' folder
#set path so analysis file goes to 'Analysis' folder
election_results_txt = "Analysis/Election Results.txt"

with open(election_results_txt, "w") as text:
    text.write(f"Election Results\n")
    text.write(f"-------------------------\n")
    text.write(f"Total Votes: {total_vote_count}\n")
    text.write("-------------------------\n")
    for key, velue in candidate_votes.items():
        text.write(f"{key}: {str(percent_votes[key])}%   ({candidate_votes[key]})\n")
    text.write(f"-------------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write(f"-------------------------\n")
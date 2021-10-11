import csv
import os

#Open file
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#initialize variables
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
#read the file 
    file_reader = csv.reader(election_data)

#read the header row
    headers = next(file_reader)

#loop through each row, tally all votes and list the candidates that received votes
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        #if the candidate is not in list, add them to the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

#variable outputs
print(candidate_options)
print(candidate_votes)
print(total_votes)

#percentage of votes each candidate won
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = (float(votes) / float(total_votes)) * 100
    print(f"{candidate_name}: {round(vote_percentage,1)}% ({votes:,})\n")

    #winner of election based on popular vote 
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name


winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
print(f"{winning_candidate} has won the election with {winning_count} votes, {round(winning_percentage,1)}% of the total {total_votes} votes.")

#Close the file
#election_data.close()
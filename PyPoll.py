import csv
import os

#Open file
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
#Perform analysis

#read the file 
    file_reader = csv.reader(election_data)

#print the header row
    headers = next(file_reader)
    print(headers)


#total number of votes cast

#a complete list of candidates who received votes

#percentage of votes each candidate won

#total number of votes each candidate won

#winner of election based on popular vote 

#Close the file
election_data.close()
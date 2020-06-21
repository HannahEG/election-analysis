# How to get the information we need for election results
# 1.Total number of votes cast
# 2.A complete list of candidates who received votes
# 3.Total number of votes each candidate received
# 4.Percentage of votes each candidate won
# 5.The winner of the election based on popular vote

# file_to_load = 'resources/election_results.csv'
# with open(file_to_load) as election_data:
    # print(election_data)

#code to read a file, dependencies 
import os
import csv
#assign a variable for the file to load and the path, create the file object
file_to_load = os.path.join('Resources/election_results.csv')
total_votes = 0
candidate_options = []


#open the election results and read file, 'as' function is using the file object in this case "election_data"
with open(file_to_load) as election_data:
    #print the file object which is 'election data'
    # print(election_data)

    #read file object with reader function
    file_reader = csv.reader(election_data)

    #read the "header" rows names
    headers = next(file_reader)
    # print(headers)
    
    #print each row in csv file
    for row in file_reader:
        # print(row)
        # add accumulator to ad to the total vote count
        total_votes = total_votes + 1
        #get candidate name from each row in column 3
        candidate_name = row[2]
    # print total votes
    # print(total_votes)
        #if candidate doesn't match existing candidatess
        if candidate_name not in candidate_options:
            # add to list of candidates
            candidate_options.append(candidate_name)
print(candidate_options)

#code for writing to a file
#Created filename variable to direct or indirect path to file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#with statement to open the file as a text file.
with open(file_to_save, "w") as analysistxt_file:

    analysistxt_file.write('Counties in the Election\n')
    analysistxt_file.write('--------------------------------\n')
    # Write some data to the file.
    analysistxt_file.write("Arapahoe\nDenver\nJefferson")
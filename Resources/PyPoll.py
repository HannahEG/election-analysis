# How to get the information we need for election results
# 1.Total number of votes cast
# 2.A complete list of candidates who received votes
# 3.Total number of votes each candidate received
# 4.Percentage of votes each candidate won
# 5.The winner of the election based on popular vote

# file_to_load = 'resources/election_results.csv'
# with open(file_to_load) as election_data:
    # print(election_data)

#code to read a file
import os
import csv
#assign a variable for the file to load and the path, create the file object
file_to_load1 = os.path.join('Resources/election_results.csv')
#open the election results and read file, 'as' function is using the file object in this case "election_data"
with open(file_to_load1) as election_data:
    #print the file object which is 'election data'
    # print(election_data)

    #read file object with reader function
    file_reader = csv.reader(election_data)
    #print each row in csv file
    # for row in file_reader:
        # print(row)
    #print the "header" rows names
    headers = next(file_reader)
    print(headers)
#code for writing to a file
#Created filename variable to direct or indirect path to file.
    file_to_save = os.path.join("analysis", "election_analysis.txt")

#with statement to open the file as a text file.
with open(file_to_save, "w") as analysistxt_file:

    analysistxt_file.write('Counties in the Election\n')
    analysistxt_file.write('--------------------------------\n')
    # Write some data to the file.
    analysistxt_file.write("Arapahoe\nDenver\nJefferson")
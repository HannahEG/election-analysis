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
#Created filename variable to direct or indirect path to file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#initialized total vote counter
total_votes = 0
#empty list
candidate_options = []
#empty dictionary
candidate_votes = {}
#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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
        # add accumulator to add to the total vote count
        total_votes = total_votes + 1 # can also be total_votes += 1
        #get candidate name from each row in column 3
        candidate_name = row[2]
    # print total votes
    # print(total_votes)
        #if candidate doesn't match existing candidatess
        if candidate_name not in candidate_options:
            # add to list of candidates
            candidate_options.append(candidate_name)
            #begin tracking each candidate's votes and setting each candidate's vote count to 0
            candidate_votes[candidate_name] = 0
        #incrementing candidate votes by placing it inside for loop
        candidate_votes[candidate_name] += 1
# print(candidate_votes)

#save results to text file i.e. code for writing to a text file
with open(file_to_save, "w") as analysistxt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #save to text file
    analysistxt_file.write(election_results)
    #for loop to go through candidate list
    for candidate in candidate_votes:
        #getting vote counts for each candidate
        votes = candidate_votes[candidate]
        #calculate percentage of candidate votes for each candidate
        vote_percentage = int(votes) / int(total_votes) * 100

        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        analysistxt_file.write(candidate_results)
        #determine winning vote count and winning candidate
        # determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #set winning_candidate equal to candidate's name
            winning_candidate = candidate

    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
    print(winning_candidate_summary)

    analysistxt_file.write(winning_candidate_summary)
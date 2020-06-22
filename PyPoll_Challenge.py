#Voter Turnout by county
import os
import csv

#read/write files
file_to_load = os.path.join('Resources/election_results.csv')
file_to_save = os.path.join("analysis", "election_analysis.txt")
#variables, lists, dictionary
total_votes = 0
county_participation = []
county_votes = {}
candidate_options = []
candidate_votes = {}
#largest county participation
largest_count = 0
largest_percentage = 0
largest_participation = ""
#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    # print(election_data)

    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    # print(headers)
    
    for row in file_reader:
        total_votes = total_votes + 1
        county_name = row[1]
        candidate_name = row[2]
    # print(total_votes)
        #if statement for candidate votes
        if candidate_name not in candidate_options:
            # add to list of candidates
            candidate_options.append(candidate_name)
            #tracking candidate votes
            candidate_votes[candidate_name] = 0
        #incrementing candidate votes 
        candidate_votes[candidate_name] += 1
    
        #if statement for counties
        if county_name not in county_participation:
            #adding participating counties
            county_participation.append(county_name)
            county_votes[county_name] = 0
        #incrementing county votes  
        county_votes[county_name] += 1
# print(county_votes)

#county results to analysis text file
with open(file_to_save, "w") as analysistxt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    analysistxt_file.write(election_results)

    county_title = (f"\nCounty Votes:\n")
    print(county_title)
    analysistxt_file.write(county_title)

    #for loop for counties
    for county in county_votes:
        #vote counts for each county
        votes1 = county_votes[county]
        #percentage of votes for each county
        county_percentage = int(votes1) / int(total_votes) * 100
        # print(county_percentage)

        county_results = (f"{county}: {county_percentage:.1f}% ({votes1:,})\n")
        print(county_results)
        analysistxt_file.write(county_results)

        #if statement for largest county
        if (votes1 > largest_count) and (county_percentage > largest_percentage):
            #if true set winning_count = votes and winning_percent = vote_percentage
            largest_count = votes1
            largest_percentage = county_percentage
            largest_participation = county

    largest_county_turnout = (
        f"\n---------------------------\n"
        f"Largest County Turnout: {largest_participation}\n"
        f"---------------------------\n")
    print(largest_county_turnout)

    analysistxt_file.write(largest_county_turnout)

    #for loop for candidates
    for candidate in candidate_votes:
        #getting vote counts for each candidate
        votes = candidate_votes[candidate]
        #calculate percentage of candidate votes for each candidate
        vote_percentage = int(votes) / int(total_votes) * 100

        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        analysistxt_file.write(candidate_results)    

       
        #if statement for election winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate

    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
    print(winning_candidate_summary)

    analysistxt_file.write(winning_candidate_summary)
#The data we need to retrive.
#The total number of votes cast.
#A complete list of candidates who received votes.
#The percentage of votes  each candidate won.
#The total number of votes each candidate won.
#The winner of the election based on popular vote.
# Create a filename variable to a direct or indirect path to the file.

import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")


# 1. Initialize a total vote counter.
total_votes=0

# candidate options
candidate_options=[]

#declare the empty dictionary
candidate_votes={}

#winning candidate and winning count tracker
winning_candidate=""
winning_count=0
winning_percentage=0

# Open the election results and read the file.
with open(file_to_load) as election_data:
       file_reader = csv.reader(election_data)

       # Read and print the header row.
       headers = next(file_reader)
       #print(headers)


       # Print each row in the CSV file.
       for row in file_reader:

              # 2. Add to the total vote count.
              total_votes +=1
              # 3. Print the total votes.
              #print(total_votes)
              #print the candidate name from each row

              candidate_name = row[2]


              # If the candidate does not match any existing candidate...

              if candidate_name not in candidate_options:
                     #add it to list of candidates
                     #1add the candidate name the candidate list
                candidate_options.append(candidate_name)
              
              #2 begin tracing that candidate's vote count
              candidate_votes[candidate_name]=0
              candidate_votes[candidate_name] +=1


with open(file_to_save,"w") as txt_file:
       # Print the final vote count to the terminal.
       election_results = (
              f"\nElection Results\n"
              f"-------------------------\n"
              f"Total Votes: {total_votes:,}\n"
              f"-------------------------\n")
       print(election_results, end="")
    # Save the final vote count to the text file.
       txt_file.write(election_results)


                     #1 iterate through the candidate list
       for candidate_name in candidate_votes:
              # 2retrive vote count of each candidate
              votes=candidate_votes[candidate_name]
              #3 calculate the percentage of votes
              vote_percentage=float(votes)/float(total_votes)*100


                            #  To do: print out each candidate's name, vote count, and percentage of
              # votes to the terminal.
                     #print(f"{candidate_name}: {vote_percentage:.if}%({votes:,})/n")

              # Determine winning vote count and candidate
              # Determine if the votes is greater than the winning count.
                            #4 print the candidate name and percentage of votes

              if (votes>winning_count) and (vote_percentage>winning_percentage):
                     # If true then set winning_count = votes and winning_percent =
                     # vote_percentage.
                     winning_count=votes
                     winning_candidate=candidate_name
                     winning_percentage=vote_percentage

              # Print the winning candidates' results to the terminal.
       winning_candidate_summary = (
              f"-------------------------/n"
              f"Winner: {winning_candidate}/n"
              f"Winning Vote Count: {winning_count:,}/n"
              f"Winning Percentage: {winning_percentage:.1f}%/n"
              f"-------------------------/n")

              #print(winning_candidate_summary)

              # And, set the winning_candidate equal to the candidate's name.
              #winning_candidate=candidate_name

                     #print(f"{candidate_name}:received{vote_percentage}%of the vote.")


                     #3print the candidate vote dictionary




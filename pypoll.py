#The data we need to retrive.
#The total number of votes cast.
#A complete list of candidates who received votes.
#The percentage of votes  each candidate won.
#The total number of votes each candidate won.
#The winner of the election based on popular vote.
# Create a filename variable to a direct or indirect path to the file.

import csv
import os
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Aerapahoe\nDenver\nJefferson")

# Close the file
outfile.close()


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
       file_reader = csv.reader(election_data)


       # Read and print the header row.
       headers = next(file_reader)
       print(headers)
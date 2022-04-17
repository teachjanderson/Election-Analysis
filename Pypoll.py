#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received the votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

# Import the datetime class from the datetime module
import datetime as dt
# Use the now() attribute on the datetime class to get the present time
now = dt.datetime.now()
# Print the present time
print("The time right now is ", now)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path 
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Print each row in the CSV file
    headers = next(file_reader)
    print(headers)

    #Print the file object
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    #Write some data to the file.
    txt_file.write("Counties in the Election\n----------------------\nArapahoe\nDenver\nJefferson")
    
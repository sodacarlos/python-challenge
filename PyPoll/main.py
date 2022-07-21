# Dependencies
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

# Set parameters
total_votes = 0
candidates = []
candidate_votes = {}
winner_count = 0
winner = ""

# Read the csv
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:

        # Track the total
        total_votes += 1
        candidate = row["Candidate"]
        # Track candidate name
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        
        candidate_votes[candidate] = candidate_votes[candidate] + 1
#We should have a list of unique candidates and a dictionary with candidate names and corresponding votes

# Print the results and export the data to our text file
with open(file_to_output, "w") as txt_file:

    # Print the final vote count
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    #Track percentage of votes count per candidate
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes)/float(total_votes)*100
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
            # Print each candidate's votes count and percentage
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's votes count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate
    winner_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")
    print(winner_summary)

    # Save the winner name to the text file
    txt_file.write(winner_summary)
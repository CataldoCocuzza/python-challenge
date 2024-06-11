import csv
import os


load_file = os.path.join("/Users/ccocu/Desktop/Homework/python-challenge/PyPoll/Resources", "election_data.csv")
output_file = os.path.join("/Users/ccocu/Desktop/Homework/python-challenge/PyPoll/analysis", "results.txt")

# Total Vote
total_votes = 0

# Candidates
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count
winning_candidate = ""
winning_count = 0

# Read the csv
with open(load_file) as election_data:
    reader = csv.reader(election_data)

    
    header = next(reader)

    
    for row in reader:

       
        print(". ", end=""),

        # total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            # list of candidates in the running
            candidate_options.append(candidate_name)

            # tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the results and export the data to our text file
with open(output_file, "w") as txt_file:

    # terminal print
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Get vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print candidate's voter count and percentage
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print winning candidate to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

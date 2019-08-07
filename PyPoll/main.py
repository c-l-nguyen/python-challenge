import csv, os

election_csv = os.path.join("Resources", "election_data.csv")
output_csv = os.path.join("Resources", "output.csv")

fields = "Voter ID,County,Candidate"
fields = fields.split(",")

total_votes = 0
candidate_votes = {}

with open(election_csv, 'r', newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",", fieldnames = fields)
    next(csvreader)
    # tally up the total votes and votes per candidate
    for row in csvreader:
        total_votes +=1
        # if candidate in dict, then add 1. else, create initial entry for candidate
        if candidate_votes.get(row["Candidate"]) != None:
            candidate_votes[row["Candidate"]] += 1
        else:
            candidate_votes[row["Candidate"]] = 1

# calculate percentage of vote for each candidate and then find the winner
candidate_percentages = {}
for key, value in candidate_votes.items():
    candidate_percentages[key] = round(candidate_votes[key]/total_votes * 100)

winner = max(candidate_percentages, key=candidate_percentages.get)

# print out the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidate_votes.keys():
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# output lines above to text file
with open(output_csv, "w", newline="") as writefile:
    writer = csv.writer(writefile)
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------"])
    writer.writerow([f"Total Votes: {total_votes}"])
    writer.writerow(["-------------------------"])
    for candidate in candidate_votes.keys():
        writer.writerow([f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})"])
    writer.writerow(["-------------------------"])
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(["-------------------------"])


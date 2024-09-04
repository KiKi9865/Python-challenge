import csv


csv_file_path = "/Users/kimiri/PythonStuff/Python-challenge/PyPoll/Resources/election_data.csv"

with open(csv_file_path) as csvfile:
    reader = csv.reader(csvfile)

    next(reader)

candidate_votes = {}
total_votes = 0

for row in reader:
    total_votes += 1
    candidate_name = row[2]
    if candidate_name in candidate_votes:
        candidate_votes[candidate_name] += 1
    else:
        candidate_votes[candidate_name] = 1

max_percentage = 0
winner = ""

for candidate, vote in candidate_votes.items():
    percentage = (vote / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({vote})")
    
    if percentage > max_percentage:
        max_percentage = percentage
        winner = candidate

print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")
for candidate, vote in candidate_votes.items():
    percentage = (vote / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({vote})")
print("-------------------------")
print(f"The winner is: {winner}")

#----Export to a text file
with open("pypollresults.txt", "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f'Total Votes: {total_votes}\n')
    file.write("-------------------------\n")
    for candidate, vote in candidate_votes.items():
        percentage = (vote / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({vote})\n")
    file.write("-------------------------\n")
    file.write(f"The winner is: {winner}\n")
    file.write("-------------------------\n")
print("Results exported to pypollresults.txt")
#import module
import os
import csv

#set path for file
csvpath = os.path.join("election_data.csv")

vote_records = []
candidate_list = []
winning_count = 0 
vote_counts = []

#open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header
    next(csvreader)

    #find total number of votes
    for vote in csvreader:
        vote_records.append(vote)
        total_votes = len(vote_records)

    #create candidate list
    for vote in vote_records:
        current_vote = vote[2]
        if current_vote not in candidate_list:
            candidate_list.append(current_vote)
    for candidate in candidate_list:
        vote_counter = 0
        for vote in vote_records:
            if candidate == vote[2]:
                vote_counter += 1
        vote_counts.append(vote_counter)
        
        max_vote_count = max(vote_counts)
        vote_index = vote_counts.index(max_vote_count)
        winning_candidate = candidate_list[vote_index]

print('')
print('Election Results')
print('----------------')
print(f'Total Votes: {total_votes}')
print('----------------')
for i, candidate in enumerate(candidate_list):
    print(f'{candidate}: {((vote_counts[i]/total_votes) * 100):0.3f}% ({vote_counts[i]})')
print('------------------')
print(f'Winner: {winning_candidate}')
print('')

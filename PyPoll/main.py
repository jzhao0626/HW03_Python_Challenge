### Import modules
import os, csv



### Reading through the CSV data
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # Skip through header
    csv_header = next(csvreader)

    # Create variables
    count = 0
    cand = {}
    winner_count = 0

    # Loop through the file and calculate the information needed  
    for row in csvreader:
        
        if not row[2] in cand.keys():
            cand[row[2]] = 0
        
        cand[row[2]] += 1

        count += 1

    print("Election Results")
    print("----------------------------")
    print(f'Total Votes: {count}')
    print("----------------------------")


    ### Write to file

    output_path = os.path.join('Analysis', 'Analysis.txt')
    fh = open(output_path, 'w')

    fh.write("Election Results" + '\n')
    fh.write("----------------------------" + '\n')
    fh.write(f'Total Votes: {count}' + '\n')
    fh.write("----------------------------" + '\n')

    for can in cand.keys():
        
        print(f"{can}: {format(round(cand[can] / count * 100), '.3f')}% ({cand[can]})")
        
        fh.write(f"{can}: {format(round(cand[can] / count * 100), '.3f')}% ({cand[can]})" + '\n')

        if cand[can] > winner_count:
            winner_count = cand[can]
            winner = can

    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")

    fh.write("----------------------------" + '\n')
    fh.write(f"Winner: {winner}" + '\n')
    fh.write("----------------------------")

fh.close()
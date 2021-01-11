### Import modules
import os, csv



### Reading through the CSV data
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # Skip through header
    csv_header = next(csvreader)

    # Create variables
    months = 0
    net = 0
    change = 0
    change_all = 0
    maxi = 0
    mini = 0

    # Loop through the file and calculate the information needed  
    for row in csvreader:
        
        # Increment 'months' for every row
        months += 1

        # Add the new change to 'net'
        net += int(row[1])
        
        # For the first month, record the Profit/Losses(P/L) in 'last'
        if months == 1:
            last = int(row[1])

        # For the rest, find the 'change' by subtracting last from the current (P/L), 
        # and add to the 'change_all' to record change overall
        else:
            change = int(row[1]) - last
            change_all += change
            last = int(row[1])

        # Record the new change if it is greater than 'maxi' or less than 'mini'
        if change > maxi:
            maxi = change
            maxi_month = row[0]

        elif change < mini:
            mini = change
            mini_month = row[0]

    net = '$' + str(net)
    avg_change = round(change_all / (months - 1), 2)
    avg_change = "$" + str(avg_change)
    maxi = "$" + str(maxi)
    mini = "$" + str(mini)



### Print to terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months:", months)
print("Total:", net)
print("Average Change:", avg_change)
print(f"Greatest Increase in Profits: {maxi_month} ({maxi})")
print(f"Greatest Decrease in Profits: {mini_month} ({mini})")



### Write to file

output_path = os.path.join('Analysis', 'Analysis.txt')
fh = open(output_path, 'w')
fh.write("Financial Analysis" + '\n')
fh.write("----------------------------" + '\n')
fh.write("Total Months:" + " " + str(months) + '\n')
fh.write("Total:" + " " + str(net) + '\n')
fh.write("Average Change:" + " " + str(avg_change) + '\n')
fh.write(f"Greatest Increase in Profits: {maxi_month} ({maxi})" + '\n')
fh.write(f"Greatest Decrease in Profits: {mini_month} ({mini})")

fh.close()
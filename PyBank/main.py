# Dependencies
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

# Track various financial parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # Track the total
        total_months += 1
        total_net =total_net+int(row[1])
        net_change=float(row[1])-prev_net
        prev_net=float(row[1])
        net_change_list=net_change_list+[net_change]
        month_of_change=month_of_change+[row[0]]

        #The greatest increase in revenue (date and amount) over the entire period
        if net_change>greatest_increase[1]:
            greatest_increase[1]= net_change
            greatest_increase[0] = row[0]

        #The greatest decrease in revenue (date and amount) over the entire period
        if net_change<greatest_decrease[1]:
            greatest_decrease[1]= net_change
            greatest_decrease[0] = row[0]
    net_average = sum(net_change_list)/len(net_change_list)
   
    #printing the result
    print("\n\nFinancial Analysis")
    print("---------------------")
    print("Total Months: %d" % total_months)
    print("Total Revenue: $%d" % total_net)
    print("Average Revenue Change $%d" % net_average)
    print("Greatest Increase in Revenue: %s ($%s)" % (greatest_increase[0], greatest_increase[1]))
    print("Greatest Decrease in Revenue: %s ($%s)\n\n" % (greatest_decrease[0], greatest_decrease[1]))

#write .txt file
with open(file_to_output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total_net)
    file.write("Average Revenue Change $%d\n" % net_average)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))
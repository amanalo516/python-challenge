import os
import csv


with open("Resources/budget_data.csv", 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter= ',')

    f = open('PyBank_results.txt',"w")
    #Use output to write results to text file
    output="Financial Analysis \n"
    output+="-----------------------  \n"
    # Create variables for needed calculations
    total_months = -1
    greatest_increase = 0
    greatest_decrease = 0
    total_profit_loss = 0
    first = True 
    greatest_increase_month = ""
    greatest_decrease_month = ""
    total_profit_change = 0 
    first_profit = 0
    previous_value = 0
    # Loop through data to capture values for variables and finish calculations
    for row in csvreader:
        if first == False and (int(row[1]) - previous_value) < greatest_decrease:
            greatest_decrease = int(row[1]) - previous_value
            greatest_decrease_month = row[0]

        if first == False and (int(row[1]) - previous_value) > greatest_increase:
            greatest_increase = int(row[1]) - previous_value
            greatest_increase_month = row[0]
            
        total_months += 1
        if first == False: 
            total_profit_loss += int(row[1])
            total_profit_change += int(row[1]) - previous_value
            previous_value = int(row[1])
            if total_months == 1:
                first_profit = int (row[1])
        if first:
            first = False
    
    output+="Total Months: " + str(total_months)
    output+= "\n"
    output+="Total: $" + str(total_profit_loss)
    output+= "\n"
    average = (total_profit_change-first_profit)/(total_months-1)
    output+="Average Change: $" + str(round(average,2))
   
    output+= "\n"
    output+="Greatest Increase in Profits: " + greatest_increase_month + "($" + str(greatest_increase) + ")" 
    output+= "\n"
    output+="Greatest Decrease in Profits: " + greatest_decrease_month + "($" + str(greatest_decrease) + ")"

print(output)
f.write(output)
f.close()
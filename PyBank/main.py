#Import the moduels into python
import os
import csv

#Set path for csv file
budget_csv = os.path.join('Resources', 'budget_data.csv')

#Store data as lists
date = []
profit = []
monthly_changes = []

#Create variables and set them equal to zero
count = 0
change_count = 0
initial_profits = 0
total_profits = 0
change_profits = 0

#read in csv file and declare header
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    
#Begin the for loop
    for row in csv_reader:

#The variable count will be what sums up the total months
        count = count + 1
        
#Declares the date for use later in the code
        date.append(row[0])

#Calulate total profit
        profit.append(row[1])
        total_profits = total_profits + int(row[1])

#If statement is used to calculate average profits. Change count is for January because there is no profits for the previous month in the data
        final_profits = int(row[1])

        if initial_profits != 0:
            
            monthly_change_profits = final_profits - initial_profits
            change_count = change_count + 1
            monthly_changes.append(monthly_change_profits)

            change_profits = change_profits + monthly_change_profits

        initial_profits = final_profits

#Final calculations for average profit
    average_change_profits = (change_profits/change_count)

#Calculating greatest increase and decrease profits using the max and min functions
    greatest_increase = max(monthly_changes)
    greatest_decrease = min(monthly_changes)

#Calculating the date of greatest increase and decrease using index function. Add one to make up for no month before January
    increase_date = date[monthly_changes.index(greatest_increase) + 1]
    decrease_date = date[monthly_changes.index(greatest_decrease) + 1]



print(average_change_profits)


#Outputing data into txt document

Output = f"""
Financial Analysis
----------------------------
Total Months: {count}
Total: {total_profits}
Average Change: ${average_change_profits: .2f}
Greatest Increase in Profits: {increase_date} (${greatest_increase})
Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})
"""
print(Output)



with open("Analysis/analysis.txt", "w") as out_file:
          out_file.write(Output)


        
        
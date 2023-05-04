import os
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')

profit = []
monthly_changes = []
date = []

count = 0
change_count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    
    for row in csv_reader:
        count = count + 1
        
        date.append(row[0])

        profit.append(row[1])
        total_profit = total_profit + int(row[1])

        final_profit = int(row[1])

        if initial_profit != 0:
            
            monthly_change_profits = final_profit - initial_profit
            change_count = change_count + 1
            monthly_changes.append(monthly_change_profits)

            total_change_profits = total_change_profits + monthly_change_profits

        initial_profit = final_profit

    average_change_profits = (total_change_profits/change_count)

    greatest_increase_profits = max(monthly_changes)
    greatest_decrease_profits = min(monthly_changes)

    increase_date = date[monthly_changes.index(greatest_increase_profits) + 1]
    decrease_date = date[monthly_changes.index(greatest_decrease_profits) + 1]



print(average_change_profits)


Output = f"""
Financial Analysis
----------------------------
Total Months: {count}
Total: {total_profit}
Average Change: ${average_change_profits: .2f}
Greatest Increase in Profits: {increase_date} (${greatest_increase_profits})
Greatest Decrease in Profits: {decrease_date} (${greatest_decrease_profits})
"""
print(Output)



with open("Analysis/analysis.txt", "w") as out_file:
          out_file.write(Output)

    #print("Financial Analysis")
    #print("----------------------------")
    
   # months = str(csv_reader[0])
  #  Profit = int(csv_reader[1])
   # total_months = sum(months)
  #  print(total_months)

        
        
import csv
#this calls on a library to use within the python code
csv_file_path = "/Users/kimiri/PythonStuff/Python-challenge/PyBank/Resources/.ipynb_checkpoints/budget_data.csv"
#file path shows anyone looking at the code where the file lives.
with open(csv_file_path) as csvfile:
    reader = csv.reader(csvfile)

    next(reader) 
    #Using this function to skip the header.

    total_months = 0
    total = 0
    previous_value = None
    changes = []


    greatest_increase_profit = 0
    greatest_decrease_profit = 0
    increase_profit_month = None
    decrease_profit_month = None
    
    for row in reader:
        total_months = total_months + 1
        total = total + int(row[1])
        current_value = int(row[1])
        if previous_value != None:
            change = current_value - previous_value
            changes.append(change)

        if previous_value != None and current_value > previous_value:
            increase_sum = current_value - previous_value
            if increase_sum > greatest_increase_profit:
                greatest_increase_profit = increase_sum
                increase__profit_month = row[0]

        if previous_value != None and current_value < previous_value:
            decrease_sum = current_value - previous_value
            if decrease_sum < greatest_decrease_profit:
                greatest_decrease_profit = decrease_sum
                decrease__profit_month = row[0]

        previous_value = current_value

    sum = 0
    for i in range(len(changes)):
        sum = sum + changes[i]
    average = sum/len(changes)

print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: {average:.2f}")
print(f"Great Increase in Profits: ${greatest_increase_profit}")
print(f"Date: {increase_profit_month}")
print(f"Greatest Decrease in Profits: ${greatest_decrease_profit}")
print(f"Date: {decrease__profit_month}")
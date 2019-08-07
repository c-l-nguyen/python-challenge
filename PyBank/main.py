import csv, os

budget_csv = os.path.join("Resources", "budget_data.csv")
output_csv = os.path.join("Resources", "output.csv")

num_month = 0
total_amount = 0
months_list = []
profit_loss_list = []

# open CSV file and iterate to calculate Financial Analysis
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        # count number of months, 
        # add up net total amount of Profits/Losses,
        # append Profit/Losses value to list,
        # append month/year value to list
        num_month +=1
        total_amount += int(row[1])
        profit_loss_list.append(int(row[1]))
        months_list.append(row[0])

# calculate the difference between months and store in difference
difference = []
for i in range(num_month-1):
    difference.append(profit_loss_list[i+1]-profit_loss_list[i])

# calculate average change in Profit/Losses over entire period, subtract one for month difference
average_change = sum(difference) / (num_month-1)
average_change_formatted = round(average_change,2)

# find list index of max & min difference
max_increase_index = difference.index(max(difference))
max_decrease_index = difference.index(min(difference))

# find greatest profit increase/decrease and the month they occured in
greatest_profit_increase = difference[max_increase_index]
greatest_profit_decrease = difference[max_decrease_index]
greatest_profit_increase_month = months_list[max_increase_index+1]
greatest_profit_decrease_month = months_list[max_decrease_index+1]

# output formatted results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {num_month}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${average_change_formatted}")
print(f"Greatest Increase in Profits: {greatest_profit_increase_month} (${greatest_profit_increase})")
print(f"Greatest Decrease in Profits: {greatest_profit_decrease_month} (${greatest_profit_decrease})")

# output lines above to text file
with open(output_csv, "w", newline="") as writefile:
    writer = csv.writer(writefile)

    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Months: {num_month}"])
    writer.writerow([f"Total: ${total_amount}"])
    writer.writerow([f"Average Change: ${average_change_formatted}"])
    writer.writerow([f"Greatest Increase in Profits: {greatest_profit_increase_month} (${greatest_profit_increase})"])
    writer.writerow([f"Greatest Decrease in Profits: {greatest_profit_decrease_month} (${greatest_profit_decrease})"])

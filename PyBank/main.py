#Import Modules
import os
import csv


#Set path for file
csvpath = os.path.join("budget_data.csv")

#Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Create variables
    months = []
    total_months = 0
    total = 0
    month_records = []
    deltas = []

    next(csvreader)

    #Print CSV 
    for record in csvreader:
        month_records.append(record)
        print(record)
        
        #find results
        total_months += 1
        
        total += int(record[1])
        month = record[0]
        months.append(month)

    #create list of deltas
    last_record = None
    for i, record in enumerate(month_records):
        if last_record is not None:
            current_value = int(record[1])
            prev_value = int(last_record[1])
            delta = current_value - prev_value
            deltas.append(delta)
        last_record = record
    
    average_delta = round(sum(deltas)/len(deltas), 2)
    greatest_increase = max(deltas)
    greatest_decrease = min(deltas)
    greatest_increase_month = deltas.index(greatest_increase)
    greatest_decrease_month = deltas.index(greatest_decrease)
    

#final print statements  
print('')
print(f'Financial Analysis')
print(f'------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: {average_delta}')
print(f'Greatest Increase: {months[greatest_increase_month + 1]} (${greatest_increase})')
print(f'Greatest Decrease: {months[greatest_decrease_month + 1]} (${greatest_decrease})')

with open('Analysis.txt', 'w') as outputfile:#writing file
    
    outputfile.write(f'Financial Analysis\n')
    outputfile.write(f'------------------\n')
    outputfile.write(f'Total Months: {total_months}\n')
    outputfile.write(f'Total: ${total}\n')
    outputfile.write(f'Average Change: {average_delta}\n')
    outputfile.write(f'Greatest Increase: {months[greatest_increase_month + 1]} (${greatest_increase})\n')
    outputfile.write(f'Greatest Decrease: {months[greatest_decrease_month + 1]} (${greatest_decrease})\n')   
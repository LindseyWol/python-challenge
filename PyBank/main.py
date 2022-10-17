#import os and csv
import os
import csv

#set path for csv file to be read 
budgetData_csv = os.path.join('Resources', 'budget_data.csv')

#open csv
with open(budgetData_csv) as csv_file:
   
    #read csv
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    #skip header row
    csv_header = next(csv_reader)
    
    #variables
    month_count = 0
    total = 0
    current_row = 0
    previous_row = 0
    month_to_month = 0

    #make empty lists
    month_change = []
    date = []

    #Loop through rows
    for row in csv_reader:
        
        # Objective 1: The total number of months included in the dataset
        month_count += 1
        
        # Objective 2: The net total amount of "Profit/Losses" over the entire period (sum all rows in 2nd column)
        current_row = int(row[1])
        total += int(row[1])
        
        # Objective 3: The changes in "Profit/Losses" over the entire period...
        if (month_count==1):
            previous_row = current_row
            
        else:
            month_to_month = current_row - previous_row
            date.append(row[0])
            month_change.append(month_to_month)
            previous_row = current_row
    #Objective 3 contd: ...and then the average of those changes        
    average = round(sum(month_change)/(month_count - 1), 2)
    
    #Objective 4: The greatest increase in profits (date and amount) over the entire period
    greatInc = max(month_change)
    greatIncDate = date[month_change.index(greatInc)]
    
    #Objective 5: The greatest decrease in profits (date and amount) over the entire period
    greatDec = min(month_change)
    greatDecDate = date[month_change.index(greatDec)]
    
    # print like example
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${total}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {greatIncDate}(${greatInc})")
    print(f"Greatest Decrease in Profits: {greatDecDate}(${greatDec})")
    print(f"----------------------------")

#write 'Financial Analysis' to a txt file in 'Analysis' folder
#set path so analysis file goes to 'Analysis' folder
financial_analysis = "Analysis/Financial Analysis.txt"

with open(financial_analysis, "w") as text:
    text.write(f"Financial Analysis\n")
    text.write(f"----------------------------\n")
    text.write(f"Total Months: {month_count}\n")
    text.write(f"Total: ${total}\n")
    text.write(f"Average Change: ${average}\n")
    text.write(f"Greatest Increase in Profits: {greatIncDate}(${greatInc})\n")
    text.write(f"Greatest Decrease in Profits: {greatDecDate}(${greatDec})\n")
    text.write(f"----------------------------")
'''
The total number of months included in the dataset

The total amount of revenue gained over the entire period

The average change in revenue between months over the entire period

The greatest increase in revenue (date and amount) over the entire period

The greatest decrease in revenue (date and amount) over the entire period

Example:
Financial Analysis
----------------------------
Total Months: 25
Total Revenue: $1241412
Average Revenue Change: $216825
Greatest Increase in Revenue: Sep-16 ($815531)
Greatest Decrease in Revenue: Aug-12 ($-652794)
'''
import os 
import csv

#build path to CSV 1 & 2
PyBank_CSV_1 = os.path.join("raw_data", "budget_data_1.csv")

#Read CSV
with open (PyBank_CSV_1, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #ignore headers
    next(csvreader)
    
    #empty lists for date and revenue
    date = []
    revenue = []

    #Start of Loop
    for row in csvreader:
        #append date & revenue to empty list
        date.append(row[0])
        revenue.append(int(row[1]))
        
        #calculate the total months & total revenue
        total_months = len(date)
        total_revenue = sum(revenue)
        
    
#Calculate the difference between months and store in a list
    total_diff_list = [j-i for i,j in zip(revenue[:-1], revenue[1:])]  
#Find the average of the list
    average_diff = float(sum(total_diff_list))/len(total_diff_list)
#find the max increase
    greatest_increase = max(total_diff_list)
#store the index where max is 
    position_increase_index = total_diff_list.index(greatest_increase)
    
#find the min increase
    greatest_decrease = min(total_diff_list)
#store the index where min is 
    position_decrease_index = total_diff_list.index(greatest_decrease)
    
    #print for days 
    print("Financial Analysis")  
    print("--------------------------")
    print ("Total Months: ", total_months)
    print ("Total Revenue: ", "$",total_revenue)
    print ("Average Revenue Change: ", average_diff)
    print ("Greatest Increase in Revenue: ", date[position_increase_index], "($" , greatest_increase, ")")
    print ("Greatest Decrease in Revenue: ", date[position_decrease_index], "($", greatest_decrease, ")")
 
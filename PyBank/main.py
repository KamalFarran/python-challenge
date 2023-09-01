# Dependencies
import os
import csv

RowCounter = 0
NetAmount = 0
IsFirstRow = True
Changes = []
SumOfChanges = 0
PreviousAmount = 0
MaxAmount = 0
MaxMonth = ""
MinAmount = 0
MinMonth = ""
Output = []

#Specify the file path
csvPath = os.path.join("Resources", "budget_data.csv")

#Open CSV file
with open(csvPath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    next(csvreader)

    #Loop through rows in the file
    for row in csvreader:

        #Count the rows
        RowCounter += 1

        #Count total amount
        Amount = float(row[1])
        NetAmount += Amount

        #Compare to previous row unless it's the first row
        if not IsFirstRow:

            #Calculate change from previous row's amount
            Change = Amount - PreviousAmount
            SumOfChanges += Change
            Changes.append(Change)

            #Check if change is the maximum or mininum so far
            if Change > MaxAmount:
                MaxAmount = Change
                MaxMonth = row[0]
            if Change < MinAmount:
                MinAmount = Change
                MinMonth = row[0]
        else:
            IsFirstRow = False

        #set amount value for next row comparison    
        PreviousAmount = float(row[1])

#Calculate the average change in profit
AverageChange = round(SumOfChanges / len(Changes), 2)

#Prepare output content
Output.append('Financial Analysis')
Output.append("----------------------------")
Output.append(f'Total Months: {RowCounter}')
Output.append(f'Total: ${NetAmount}')
Output.append(f'Average Change: ${AverageChange}')
Output.append(f'Greatest Increase in Profits: {MaxMonth} (${round(MaxAmount)})')
Output.append(f'Greatest Decrease in Profits: {MinMonth} (${round(MinAmount)})')

#Specify output path
OutputPath = os.path.join("analysis", "results.txt")

#Open output file
with open(OutputPath, "w") as OutputFile:

    #Print each line to the terminal and add it to the file
    for row in Output:
        print(row)
        OutputFile.write(row+'\n')
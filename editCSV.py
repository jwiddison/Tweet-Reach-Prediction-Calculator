import csv

def addColumnToCSV(columnName, whatToPutInColumn):
    with open('/Users/Jordan/Desktop/posts.csv','r') as csvinput:
        with open('/Users/Jordan/Desktop/output.csv', 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)

            newColumn = []
            row = next(reader)
            row.append(columnName)
            newColumn.append(row)

            for row in reader:
                # row.append(row[2])
                row.append(whatToPutInColumn)
                newColumn.append(row)

            writer.writerows(newColumn)

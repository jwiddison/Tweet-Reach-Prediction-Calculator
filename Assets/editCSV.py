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
                # row[2] is how you access the stuff in the text column.  So I was just appending the same stuff out of row[2].
                # You can access row[2] and then use that data to call the Google API eventually.
                # row.append(row[2])

                # TODO: Call google text processing API here.

                row.append(whatToPutInColumn)
                newColumn.append(row)

            writer.writerows(newColumn)

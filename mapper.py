import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)

for row in reader:
    try:
        rating = row[8]
        if rating:
            print "%s\t1" % rating
    except:
        pass

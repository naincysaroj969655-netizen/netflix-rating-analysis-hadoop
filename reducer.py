import sys

current_rating = None
count = 0

for line in sys.stdin:
    rating, value = line.strip().split("\t")
    value = int(value)

    if current_rating == rating:
        count += value
    else:
        if current_rating:
            print "%s\t%d" % (current_rating, count)
        current_rating = rating
        count = value

if current_rating:
    print "%s\t%d" % (current_rating, count)

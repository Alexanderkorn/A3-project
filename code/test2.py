__author__ = 'alexander'
import csv
import sys
keywords = {"aasdf", "aasdfs"}
csv.field_size_limit(sys.maxsize)
invalids = 0
valids = 0
for filename in ['database.csv']:
    # The with statement in Python makes sure that your file is properly closed
    # (automatically) when an error occurs. This is a common idiom.
    # In addition, CSV files should be opened only in 'rb' mode.
    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter='|', quotechar='\\')
        for row in reader:
            try:
                print(row)[2]
                valids += 1
            # Don't use bare except clauses. It will catch
            # exceptions you don't want or intend to catch.
            except IndexError:
                invalids += 1
            # The filtering is done here.
            for field in row:
                if field in keywords:
                    print(row)
                    break
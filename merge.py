import csv
import sys
import re

reader = sys.argv[1:]
writer = csv.writer(sys.stdout)

for icsv in reader:
  acsv = open(icsv)
  fcsv = csv.reader(acsv)

  fcsv.next()
  for i, row in enumerate(fcsv):
    row = [(int(x) if re.match(r"[-+]?\d+$", x) is not None else x) for x in row]
    state = row[9].split('/')[4]
    writer.writerow([i, state] + row)
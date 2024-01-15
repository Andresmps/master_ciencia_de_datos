import sys

for line in sys.stdin:
    line = line.strip()
    person, store, spending = line.split(';')
    print(f'{person},{store}\t{spending}')

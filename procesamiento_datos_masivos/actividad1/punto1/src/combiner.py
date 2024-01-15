import sys

current_key = None
current_sum = 0
current_count = 0

for line in sys.stdin:
    line = line.strip()
    key, spending = line.split('\t')
    spending = float(spending)

    if current_key == key:
        current_sum += spending
        current_count += 1
    else:
        if current_key:
            print(f'{current_key}\t{int(current_sum)},{current_count}')
        current_sum = spending
        current_count = 1
        current_key = key

if current_key == key:
    print(f'{current_key}\t{int(current_sum)},{current_count}')

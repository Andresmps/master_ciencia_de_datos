import sys

current_key = None
total_sum = 0
total_count = 0

for line in sys.stdin:
    line = line.strip()
    key, values = line.split('\t')
    sum_values, count_values = map(float, values.split(','))

    if current_key == key:
        total_sum += sum_values
        total_count += count_values
    else:
        if current_key:
            person, store = current_key.split(',')
            average = total_sum / total_count
            print(f'{person};{store};{average}')
        total_sum = sum_values
        total_count = count_values
        current_key = key

if current_key == key:
    person, store = current_key.split(',')
    average = total_sum / total_count
    print(f'{person};{store};{average}')

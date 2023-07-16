import csv
with open('testing.txt', 'r', encoding='utf-8') as input_file:
    reader = csv.reader(input_file, delimiter='\t')
    modified_rows = []
    for row in reader:
        modified_row = row[1:]
        modified_rows.append(modified_row)
with open('modified_testing.txt', 'w', encoding='utf-8', newline='') as output_file:
    writer = csv.writer(output_file, delimiter='\t', lineterminator='\n')
    writer.writerows(modified_rows)
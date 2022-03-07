import csv

with open('practice_csv_dir/parse.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter='\t')
    with open('practice_csv_dir/csv_test_file.csv', 'w') as csv_file:
        fieldnames = ['first_name\tlast_name\temail']
        csv_writer = csv.writer(csv_file, delimiter=',')  # fieldnames=fieldnames
        for line in csv_reader:
            csv_writer.writerow(line)
            print(line)

with open('practice_csv_dir/csv_test_file.csv', 'r') as read_new:
    csv_reader= csv.DictReader(read_new)
    for i in csv_reader:
        print(i['first_name'])
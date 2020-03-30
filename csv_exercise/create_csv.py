# CSV: use csv files; import csv files, manage csv data, basic ETL, transform data and write to new csv file

import csv
# with open('user_details.csv', newline='') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
#     # print(csvreader)
#     iterable_csv = iter(csvreader)
#     next(iterable_csv) # to skip the next line
#     for row in iterable_csv:
#         print(row[-1])

# transform csv data:
def transform_user_details(file):
    new_user_data = []
    with open(file, newline='') as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=',')
        for user in user_details_csv:
            # transformation = []
            # transformation.append(user[0])
            # transformation.append(user[1])
            # transformation.append(user[-1])
            transformation = user[0], user[1], user[-1]
            new_user_data.append(transformation)
    return new_user_data
print(transform_user_details("user_details.csv"))

# create a copy of a csv file in the same directory
def create_user_details_copy(old_file_name, new_file_name = 'user_details_copy.csv'):
    user_details_copy = transform_user_details(old_file_name)
    # new_file = open(new_file_name, 'w')
    with open(new_file_name, 'w+') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(user_details_copy)
create_user_details_copy("user_details.csv")
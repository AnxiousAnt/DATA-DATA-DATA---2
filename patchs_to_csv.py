import os
import csv

#directory containing the .pd files
directory_path = 'renamed_patches'

#output CSV file
output_csv = 'pd_patches_instruction_dataset.csv'

# Function to read the contents of a .pd file
def read_pd_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# List to hold the data for the CSV
data = []

# Traverse the directory and read each .pd file
for file_name in os.listdir(directory_path):
    if file_name.endswith('.pd'):
        file_path = os.path.join(directory_path, file_name)
        source_code = read_pd_file(file_path)
        data.append([file_name, source_code])

# Write the data to a CSV file
with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Filename', 'SourceCode'])
    writer.writerows(data)  

print(f'Successfully written data to {output_csv}')

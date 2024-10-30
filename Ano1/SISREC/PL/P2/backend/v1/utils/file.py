import os
import pandas as pd
import csv

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir,'./movies_with_imdb.csv')
file1_path = os.path.join(script_dir,'./movies_with_url.csv')


merged_df = pd.read_csv(file_path)
#merged_df['title'] = merged_df['title'].astype(str)
merged_df['year'] = pd.to_numeric(merged_df['year'], errors='coerce').astype(pd.Int64Dtype())
#merged_df['genres'] = merged_df['genres'].astype(str)


merged_df.to_csv(file_path, index=False)

#Read the CSV file with comma separator and write it with semicolon separator
#with open(file1_path, 'r', newline='', encoding='utf-8')  as infile:
#    reader = csv.reader(infile)
#    with open(file_path, 'w', newline='', encoding='utf-8') as outfile:
#        writer = csv.writer(outfile, delimiter=',')
#        for row in reader:
#            writer.writerow(row)

#Read the CSV file with semicolon separator and write it with comma separator
            
""" with open(file1_path, 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    with open(file_path, 'w', newline='', encoding='utf-8') as new_csvfile:
        csv_writer = csv.writer(new_csvfile, delimiter=',')
        for row in csv_reader:
            csv_writer.writerow(row) """
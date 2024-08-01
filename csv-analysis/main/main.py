from scripts.scripts import *
import os

# Get the path of the current script
current_dir = os.path.dirname(__file__)

# Construct the path to the CSV file
file_path = os.path.join(current_dir, '../csv-analysis/data.csv')
data = read_csv(file_path)

if data is not None:
    display_head(data)
    display_summary_statistics(data)

from scripts.scripts import *

file_path = ('csv-excel-analisys/Data.csv')
data = read_csv(file_path)

if data is not None:
    display_head(data)
    display_summary_statistics(data)

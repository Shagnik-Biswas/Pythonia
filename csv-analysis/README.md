
# CSV Mini-script 📊

🧑‍💻 This is a small Python3 script that allows you to read a .csv file 
and can filter its headers and displays summary statistics of the csv file.

## Considerations ‼️‼️
First you must install the pandas library using the following command: 
`pip install pandas` 

## Badge
Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## Contributing

Contributions are always welcome!

See `contributing.md` to see how to get started.

## Usage/Examples

```Python
# Use

file_path = 'path/to/your/file.csv'
data = read_csv(file_path)

if data is not None:
    display_head(data)
    display_summary_statistics(data)
    
    # Filter data where age is greater than 21
    
    filtered_data = filter_data(data, 'age', 'age > 21')
    print("\nFiltered data:")
    print(filtered_data)
```


## Autor

- [@AbelolDev](https://github.com/AbelolDev)


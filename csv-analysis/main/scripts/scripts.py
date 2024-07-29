import pandas as pd

def read_csv(path):
    """Reads a CSV file and returns a DataFrame."""
    try:
        data = pd.read_csv(path)
        return data
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return
    
def display_head(data, n=5):
    """Displays the first n rows of the DataFrame."""
    print(f"First {n} rows of the CSV file:")
    print(data.head(n))
    return

def display_summary_statistics(data):
    """Displays summary statistics of the DataFrame."""
    print("\nSummary statistics:")
    print(data.describe())
    return
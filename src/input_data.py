import pandas as pd

def load_reservoir_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print("Error: File not found.")
        return None

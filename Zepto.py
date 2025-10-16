import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import zipfile

print("Starting Step 1: Data Setup & Pre-processing...")

zip_path = r'C:\Users\MY PC\Downloads\Zepto datasets.zip'

try:
    with zipfile.ZipFile(zip_path, 'r') as z:
        # Read Excel file
        with z.open('zepto_v1.xlsx') as f1:
            df_v1 = pd.read_excel(f1)
        # Read CSV file
        with z.open('zepto_v2.csv') as f2:
            df_v2 = pd.read_csv(f2, encoding='latin-1')
except FileNotFoundError as e:
    print(f"Error: {e}. Please ensure the files are in the correct directory.")
    exit()
except KeyError as e:
    print(f"Error: {e}. Please check the file names inside the zip archive.")
    exit()

df = pd.concat([df_v1, df_v2], ignore_index=True)

initial_rows = len(df)
df.drop_duplicates(inplace=True)
print(f"Removed {initial_rows - len(df)} duplicate rows. Total rows now: {len(df)}")

df.columns = [col.replace(' ', '').replace('&', '').lower() for col in df.columns]

for col in ['mrp', 'discountedsellingprice']:
    if col in df.columns:
        df[col] = df[col] / 100

print("\nData Pre-processing complete. Here is a summary of the cleaned data:")
print(df.info())
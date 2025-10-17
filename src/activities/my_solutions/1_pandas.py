from pathlib import Path
import csv
import pandas as pd
import matplotlib.pyplot as plt

project_root = Path(__file__).parent.parent

csv_file = project_root.joinpath('data', 'paralympics_raw.csv')

# Check if the file exists, this will print 'true' if it exists
# print(csv_file.exists())


from importlib import resources
from activities import data



# def describe(df):
    

paralympics_data_file_csv = resources.files(data).joinpath("paralympics_raw.csv")
paralympics_all_data_file_csv = resources.files(data).joinpath("paralympics_all_raw.xlsx")
# print(f"{paralympics_data_file_csv.exists()} y")

variable_name_for_df = pd.read_csv(paralympics_data_file_csv)

sheet_1 = pd.read_excel(paralympics_all_data_file_csv, sheet_name=0)
sheet_2 = pd.read_excel(paralympics_all_data_file_csv, sheet_name=1)

# Create a histogram of the DataFrame
sheet_1.hist()
# Show the plot
plt.show()


print('y')
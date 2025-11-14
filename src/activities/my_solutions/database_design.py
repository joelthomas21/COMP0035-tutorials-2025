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
# sheet_1.hist()
# # Show the plot®
# plt.show()

def describe(df):
    print("\nColumns:")
    print(df.columns)
    print("\nDatatypes:")
    print(df.dtypes)
    print("\nInfo:")
    print(df.info())
    print("\nDescription:")
    print(df.describe())


if __name__ == "__main__":
    # Filepath of the csv data file (you may have used importlib.resources rather than pathlib.Path)
    paralympics_data_file_csv = resources.files(data).joinpath("paralympics_raw.csv")
    paralympics_all_data_file_csv = resources.files(data).joinpath("paralympics_all_raw.xlsx")
    # Read the data from the file into a Pandas dataframe
    events_csv_df = pd.read_csv(paralympics_data_file_csv)
    sheet_1 = pd.read_excel(paralympics_all_data_file_csv, sheet_name=0)
    sheet_2 = pd.read_excel(paralympics_all_data_file_csv, sheet_name=1)

    # Call the function named 'describe_dataframe' - you may have a different name for your function
    # print('**Events CSV')
    # describe(events_csv_df)
    print('**Sheet 1')
    describe(sheet_1)
    print('**Sheet 2')
    describe(sheet_2)


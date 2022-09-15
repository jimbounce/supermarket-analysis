
"""
Created: 14th September 2022
Author: Nigel Cooksley BEng PGCE

Contact: njcooksley@live.co.uk
LinkedIn Profile: www.linkedin.com/in/nigel-cooksley-bristol

"""

import numpy as np
import pandas as pd

def main():
    """

    Supermarket Sales at 3 branches from January 2019 to March 2019.

    6 Product lines.
    Purchase times (10am to 9pm)
    cogs is Cost Of Goods Sold
    Rating scale of 1 to 10

    """
    # Setting workspace
    pd.set_option('display.width', 1200)  # These two lines so all columns are printed in output
    pd.set_option('display.max_columns', 100)

    # Uploading dataset
    df = pd.read_csv("Supermarket Dataset.csv", header=0)

    # Describing the data
    print("\nNumber of rows and columns: ", df.shape, "\n")
    print("df...first and last 5 rows. \n", df)
    print("\n\ndf.describe()\n", df.describe())     # Basic statistical measures of each column
    print("\n")
    #print("Datatypes of each column:\n", df.dtypes)  # data types of each attribute

    # Totals of each column
    print("\n")
    gender_counts = df["Gender"].value_counts();
    #print('gender counts:', gender_counts)  # Ordered no. of occuraences of each value

    # Identifying number of unique values in each column
    for col in df.columns:
        print("Unique values of column", col, "are: ", df[col].nunique())

    # Checking for missing values
    #print("\ndf.count():\n", df.count())   # Counts number of entries in each column

    # Checking for duplicate rows
    # df = df.drop_duplicates()
    # print("counts after duplicate removal")
    # print(df.count())

    # Checking for outliers


    # Features (Xi)
    #print("\n\nColumns as a list: \n", df.columns, '\n')  # column names as a list

   # Do 'tax 5%' and 'gross income' columns have the same values?
    print("equal?", df["Tax 5%"].equals(df["gross income"]))   # Suspecting equal columns

if __name__ == "__main__":
    main()


"""

This is free software: you can redistribute it and/or modify it under the terms
of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version. It is
distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
the code.  If not, see <http://www.gnu.org/licenses/>.

File name: 	delta_clean.py
Created: 11th July 2022
Author: Nigel Cooksley BEng PGCE

Contact: njcooksley@live.co.uk
LinkedIn Profile: www.linkedin.com/in/nigel-cooksley-bristol
github profile: github.com/jimbounce

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
    # print("\nNumber of rows and columns: ", df.shape, "\n")
    print("df...first and last 5 rows. \n", df)
    print("\n\ndf.describe()\n", df.describe())     # Basic statistical measures of each column
    # print("\n")
    #print("Datatypes of each column:\n", df.dtypes)  # data types of each attribute

    # Summing "Total" column for checking later
    sum_cols = df.sum(axis = 0)
    print(sum_cols[9])

    # Totals of each column
    print("\n")
    #gender_counts = df["Gender"].value_counts();
    #print('gender counts:', gender_counts)  # Ordered no. of occuraences of each value

    # Identifying number of unique values in each column
    # for col in df.columns:
    #     print("Unique values of column", col, "are: ", df[col].nunique())

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
    #print("equal?", df["Tax 5%"].equals(df["gross income"]))   # Suspecting equal columns

    # Re-formatting the "Date" column




    # Converting date to number 1-90
    daynum_list = []
    for date in df["Date"]:
        if date[0] != "0":    # not equal to the string zero not the integer zero
            date = "0" + date
        #print(date)
        monthday = date[:5].split("/")
        month = int(monthday[0])
        day = int(monthday[1])

        # Assigning numbers 1 - 90 to the days in Jan - Mar.
        if month == 1:          #Jan
            daynum = day
        elif month == 2:        # Feb
            daynum = 31 + day
        else:                   # Mar
            daynum  = 59 + day  # 2019 is not a leap year so 28 days in Feb
        daynum_list.append(daynum)
        #print(month, day, daynum)

    print("Length of daynum_list", len(daynum_list))

    # Create new (18th) column called "daynum col title" representing date -- still 1000 rows tho
    df["Daynum"] = daynum_list
    # print(df)

    # Sum all totals for each day and display dataframe now only 89 rows / 2 col
    df2 = df.groupby("Daynum", as_index=False)["Total"].sum()
    print("df2\n", df2)
    print("type of df2", type(df2))    # pandas.core.series.Series
    print("type of df ", type(df), "\n")     # whereas df is a :    pandas.core.frame.DataFrame

    print(df2.describe(), "\n")

    # Plotting total sales in each of 89 days (not for presentation)
    # import matplotlib.pyplot as plt
    # plt.figure()
    # plt.scatter(df2["Daynum"], df2["Total"])
    # plt.title("Scatter plot")
    # plt.xlabel("Day number")
    # plt.ylabel("Total Sales")
    # plt.xlim([0, 90])
    # plt.ylim([0, 7600])  ## Highest value of total is 1042.65
    # plt.show()

    # Arranging into days of the week total sales
    # Categorizing day numbers into 7 days of the week (1st Jan 2019 was a Tues)
    dowlist = []
    for daynum in daynum_list:
        if daynum % 7 == 1:
            dow = "Tue"
        elif daynum % 7 == 2:
            dow = "Wed"
        elif daynum % 7 == 3:
            dow = "Thu"
        elif daynum % 7 == 4:
            dow = "Fri"
        elif daynum % 7 == 5:
            dow = "Sat"
        elif daynum % 7 == 6:
            dow = "Sun"
        else:                   # daynum % 7 == 0
            dow = "Mon"
        dowlist.append(dow)
    print(len(dowlist))     # still in 1000 world

    # Creating day of week column dataframe
    df["dow"] = dowlist
    print(df)
    df3 = df.groupby("dow", as_index=False)["Total"].sum()
    print("\ndf3\n", df3)
    import matplotlib.pyplot as plt
    plt.figure()
    plt.bar(df3["dow"], df3["Total"])
    plt.title("Comparing days of the week")
    plt.xlabel("Day of the week")
    plt.ylabel("Total Sales")
    # plt.xlim([0, 7])
    plt.ylim([0, 60000])  ## Highest value of total is 1042.65
    plt.show()

    # Creating a 'week of the season' dataframe
    seasonlist = []
    for daynum in daynum_list:
        if 1 < daynum <= 8:
            season = "aj1"
        elif 8 < daynum <= 16:
            season = "aj2"
        elif 16 < daynum <= 23:
            season = "aj3"
        elif 23 < daynum <= 31:
            season = "aj4"
        elif 32 < daynum <= 38:
            season = "f1"
        elif 38 < daynum <= 45:
            season = "f2"
        elif 45 < daynum <= 52:
            season = "f3"
        elif 52 < daynum <= 59:
            season = "f4"
        elif 59 < daynum <= 67:
            season = "m1"
        elif 67 < daynum <= 75:
            season = "m2"
        elif 74 < daynum <= 82:
            season = "m3"
        elif 82 < daynum <= 90:
            season = "m4"
        seasonlist.append(season)
    print("\nLength of season list", len(seasonlist))

    df["Season"] = seasonlist
    print(df.head())

    df4 = df.groupby(by = "Season", as_index=False)["Total"].sum()

    # Standardizing values so all 7-day (not 8 day) week categories
    df4.iloc[0,1] = df4.iloc[0,1] * (7/8)
    df4.iloc[1, 1] = df4.iloc[1, 1] * (7 / 8)
    df4.iloc[3, 1] = df4.iloc[3, 1] * (7 / 8)
    df4.iloc[8, 1] = df4.iloc[8, 1] * (7 / 8)
    df4.iloc[9, 1] = df4.iloc[9, 1] * (7 / 8)
    df4.iloc[11, 1] = df4.iloc[11, 1] * (7 / 8)

    print("\ndf4\n", df4)

    # Plotting weekly performance throughout the time period of 3 months
    import matplotlib.pyplot as plt
    #plt.figure()
    plt.bar(df4["Season"], df4["Total"])
    plt.title("Comparing Sales in 12 weeks of January - March 2019")
    plt.xlabel("Week of the season")
    plt.ylabel("Total Sales")
    # plt.xlim([0, 7])
    plt.ylim([0, 40000])  ## Highest value of total is .....
    plt.show()





    # Which date were there no sales? 89 unique data values out of 90 days 1 Jan to 31 Mar.








if __name__ == "__main__":
    main()


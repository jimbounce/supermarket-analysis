# supermarket-analysis readme.md 

"""
This project was written as part of my (Nigel Cooksley) Python and Machine Learning training on an Institute Of Coding Skills Bootcamp. This Cloud Analytics and Data Science bootcamp was delivered by Edge Hill University, Liverpool, UK from June to September 2022. 

I chose this project from the 3 available projects as I wanted the challenge of some 'messy' raw data of a straightforward commercial situation. The role of a Data Scientist famously involves 80% data wrangling, which is preceived as the 'boring admin' before the real work begins. It is for me though, a large attraction to the profession! 

The problem, the project solved was to predict the busiest day of an apparently fictitious supermarket in Burma in the first quarter of 2020 given only some sales figures from the first quarter of 2019 (but no figures for the reaminder of that year or previous years. 

This project provided me with essential practice in data wrangling and the chance to apply other skills I had developed on the course (which consisted of 20 hours study per week for 4.5 months, weekly assessment deadlines and larger monthly assesssment deadlines). I also learnt (in the good example here) how 'messy' raw data can be and it really made me think about how and which features I should use to provide useful insight. This was just to enable me to eyeball the data. Further feature engineering was required to convert string fields into dummy integer variables for the application of Machine Learning algorithms. 

From feedback from tutors upon my presentation of my insights what makes my project stand out is that I preformed a significant amount of feature engineering as I focussed on decomposing the date field into days of the week and I also introduced further seasonality fields to represent weeks (which I standardised to classify 31 days of January and March into 28 days (4 weeks).

Original Raw Data Features:
Invoice 
ID
Branch
City
Customer type
Gender
Product line
Unit price
Quantity
Tax 5%
Total
Date
Time
Payment
cogs
gross margin percentage
gross income
Rating

In addition to the original features, I created the following fields for exploratory analysis and machine learning requirements:

dow - day of week - a string variable extracted from original date 
Season - which week in Q1 of 2019 - also a string variable extracted from original date 

Dummy variables for ML:

dowsat, dowsun, dowmon, dowtue, dowwed, dowthu, dowfri
aj1, aj2, aj3, aj4, f1, f2, f3, f4, m1, m2, m3, m4



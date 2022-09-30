"""

This is free software: you can redistribute it and/or modify it under the terms
of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version. It is
distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
the code.  If not, see <http://www.gnu.org/licenses/>.

File name: 	delta_machine_learning.py
Created: 21st September 2022
Author: Nigel Cooksley BEng PGCE

Contact: njcooksley@live.co.uk
LinkedIn Profile: www.linkedin.com/in/nigel-cooksley-bristol
github profile: github.com/jimbounce

"""

def main():
    """
Supervised learning Machine Learning algorithm to predict busiest business day between Jan 1st 2020 and Mar
31st 2020 using training and test data from the same time period in 2019.

    """
    import pandas as pd
    df5 = pd.read_csv("DeltaML.csv", header=0)
    print(df5.info())

    # The ML Model
    feature_cols = ["dowsat", "dowsun", "dowmon", "dowtue", "dowwed", "dowthu", "dowfri", "aj1", "aj2", "aj3", "aj4", \
                    "f1", "f2", "f3", "f4", "m1", "m2", "m3", "m4"]
    X = df5[feature_cols]
    y = df5['Total']

    # Splitting into training and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    # Creating the deploying the model
    model = DecisionTreeClassifier()
    model = model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Accuracy
    accuracy = metrics.accuracy_score(y_test, y_pred) * 100
    print('DT Accuracy is: ', accuracy)

if __name__ == "__main__":
    main()









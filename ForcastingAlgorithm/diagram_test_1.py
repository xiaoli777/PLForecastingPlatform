import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('Advertising.csv')
print(data.head())

#create a python list of feature names
feature_cols = ['TV', 'Radio', 'Newspaper']
# use the list to select a subset of the original DataFrame
X = data[feature_cols]
# equivalent command to do this in one line
X = data[['TV', 'Radio', 'Newspaper']]

sns.pairplot(data, x_vars=['TV','Radio','Newspaper'], y_vars='Sales', size=7, aspect=0.8, kind='reg')
plt.show()

# check the type and shape of X
print(type(X))
print(X.shape)

y = data['Sales']
# equivalent command that works if there are no spaces in the column name
y = data.Sales
# print the first 5 values
print(y.head())

plt.show()#注意必须加上这一句，否则无法显示。
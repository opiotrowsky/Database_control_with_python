import pandas as pd
import statistics as st

data = pd.read_csv('forestfires.csv', delimiter=';')

dictionary = {'month':{'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,
                       'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12},
              'day':{'mon':1,'tue':2,'wed':3,'thu':4,'fri':5,'sat':6,'sun':7}}

for category in dictionary:
    for value in dictionary[category]:
        data[category] = data[category].replace(value, dictionary[category][value])
        
data = data[['month', 'day', 'temp', 'area']]
print(data)

print('\nMaximum temperature in which fire started:')
print(data.nlargest(1, 'temp'))

print('\nMinimum temperature in which fire started:')
print(data.nsmallest(1, 'temp'))

print('\nMean temperature in which fire started:')
print(round(data['temp'].mean(), 2))

print('\nMaximum burnt area:')
print(data.nlargest(1, 'area'))

print('\nMean burnt area:')
print(round(data['area'].mean(), 2))

print('\nQuartiles of months in which fire started:')
print(round(data['month'].quantile([.25, .5, .75])))

print("\nOdchylenie:")
for (column_name, column_data) in data.items():
    print(f"{column_name}:\t{round(st.stdev(column_data), 2)}")

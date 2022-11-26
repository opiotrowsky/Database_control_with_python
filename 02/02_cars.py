import pandas as pd
import statistics as st

data=pd.read_csv('samochody.csv', delimiter=';')

slownik={'Buying':{'vhigh':3, 'high':2, 'med':1, 'low':0},
         'Maint':{'vhigh':3, 'high':2, 'med':1, 'low':0},
         'Doors':{'5more':5, '4':4, '3':3, '2':2},
         'Persons':{'more':5, '4':4, '2':2},
         'Lug  boot':{'small':0, 'med':1, 'big':2},
         'Safety':{'low':0, 'med':1, 'high':2},
         'Class Values':{'unacc':0, 'acc':1, 'vgood':2, 'good':3}}

for kategoria in slownik:
    for value in slownik[kategoria]:
        data[kategoria]=data[kategoria].replace(value, slownik[kategoria][value])

print("Maximum:")
print(data.max())
    
print("\nMinimum:")
print(data.min())

print("\nMean:")
print(round(data.mean(), 2))
    
print("\nFirst quartile [0.25], median [0.5], third quartile [0.75]:")
print(data.quantile([.25, .5, .75]))

print("\nOdchylenie:")
for (column_name, column_data) in data.items():
    print(f"{column_name}:\t{round(st.stdev(column_data), 2)}")
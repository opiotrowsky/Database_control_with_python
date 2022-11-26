import pandas as pd
import statistics as st

data = pd.read_excel(r'breast_cancer.xlsx')
print(data)

print("\nMaximum:")
print(data.max())
    
print("\nMinimum:")
print(data.min())
    
print("\nMean:")
print(round(data.mean(), 2))
    
print("\nFirst quartile, median, third quartile:")
pd.set_option('display.max_columns', None)
print(data.quantile([.25, .5, .75]))
pd.reset_option('display', None)

print("\nMode:")
print(data.mode())

print("\nOdchylenie:")
for (column_name, column_data) in data.items():
    print(f"{column_name}:\t{round(st.stdev(column_data), 2)}")

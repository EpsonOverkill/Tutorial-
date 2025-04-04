import pandas as pd
data = [['Nandhu', 21], ['Gouri', 20]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
df.set_index('Name', inplace=True)
print(df)

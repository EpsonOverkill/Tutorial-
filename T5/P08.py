import pandas as pd
df = pd.read_csv("auto.csv")
df = df.dropna()

most_expensive = df[df["price"] == df["price"].max()]
print("Most expensive car company:")
print(most_expensive["company"].values[0])

print("\nToyota car details:")
print(df[df["company"] == "toyota"])

print("\nTotal cars by each company:")
print(df["company"].value_counts())

print("\nHighest priced car of each company:")
print(df.loc[df.groupby("company")["price"].idxmax()])

print("\nAverage mileage by company:")
print(df.groupby("company")["average-mileage"].mean())

print("\nCars sorted by price:")
print(df.sort_values("price", ascending=False))

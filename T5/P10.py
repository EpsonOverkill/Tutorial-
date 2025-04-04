import pandas as pd
import matplotlib.pyplot as plt

data = {
    "rollno": [50, 60, 70, 80, 90],
    "name": ["Nandhu", "Gouri", "Roshan", "Gigi", "Aravind"],
    "place": ["Trichur", "Kochi", "Kozhikode", "Ernakulam", "Malappuram"],
    "mark": [98, 85, 91, 67, 74]
}
df = pd.DataFrame(data)
df.to_csv("stud.csv", index=False)

df = pd.read_csv("stud.csv")
print("All data:\n", df)

df_indexed = df.set_index("rollno")
print("\nWith rollno as index:\n", df_indexed)

print("\nOnly name and mark:\n", df[["name", "mark"]])

sorted_by_name = df.sort_values("name")
print("\nSorted by name:\n", sorted_by_name[["rollno", "name", "mark"]])

sorted_by_mark = df.sort_values("mark", ascending=False)
print("\nSorted by mark descending:\n", sorted_by_mark[["rollno", "name", "mark"]])
print("\nAverage mark:", df["mark"].mean())
print("Median mark:", df["mark"].median())
print("Mode of marks:\n", df["mark"].mode())

print("\nMinimum mark:", df["mark"].min())
print("Maximum mark:", df["mark"].max())

print("\nVariance:", df["mark"].var())
print("Standard Deviation:", df["mark"].std())

plt.hist(df["mark"], bins=5, color='skyblue', edgecolor='black')
plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.grid(True)
plt.show()

df_removed = df.drop(columns=["place"])
print("\nData after removing 'place' column:\n", df_removed)

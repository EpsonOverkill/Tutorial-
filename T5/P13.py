import pandas as pd

data = {
    "name": ["Nandhu", "Gouri", "Roshan", "Gigi", "Aravind", "Pavithra"],
    "gender": ["Male", "Female", "Male", "Male", "Male", "Female"],
    "start_date": ["2020-01-10", "2019-07-15", "2021-03-05", "2018-11-20", "2022-06-18", "2017-04-22"],
    "salary": [98000, 52000, 47000, 60000, 45000, 75000],
    "team": ["Design", "Sales", "Design", "Engineering", "HR", "Engineering"]
}
df = pd.DataFrame(data)
df.to_csv("employee.csv", index=False)
df = pd.read_csv("employee.csv")
print("First 7 records:\n", df.head(7))
print("\nEmployees in alphabetical order:\n", df["name"].sort_values())
highest_paid = df[df["salary"] == df["salary"].max()]
print("\nEmployee with highest salary:\n", highest_paid["name"].values[0])
print("\nMale employees:\n", df[df["gender"] == "Male"]["name"])
print("\nTeams in the company:\n", df["team"].unique())

import pandas as pd

df = pd.read_csv("student.csv")

avg_cgpa = df["CGPA"].mean()
print("Average CGPA of all students:", avg_cgpa)
print("\nStudents with CGPA > 9:")
print(df[df["CGPA"] > 9])
print("\nCSE students with CGPA > 9:")
print(df[(df["Branch"] == "CSE") & (df["CGPA"] > 9)])

max_cgpa_student = df[df["CGPA"] == df["CGPA"].max()]
print("\nStudent with maximum CGPA:")
print(max_cgpa_student)

print("\nAverage CGPA of each branch:")
print(df.groupby("Branch")["CGPA"].mean())

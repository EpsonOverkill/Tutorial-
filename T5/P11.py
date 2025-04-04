import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

plt.figure(figsize=(8, 4))
plt.scatter(df["month_number"], df["toothpaste"], color='blue')
plt.title("Toothpaste Sales Per Month")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.grid(True)
plt.xticks(df["month_number"])
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
bar_width = 0.4
months = df["month_number"]
x1 = [m - bar_width/2 for m in months]
x2 = [m + bar_width/2 for m in months]
plt.bar(x1, df["facecream"], width=bar_width, label="Face Cream")
plt.bar(x2, df["facewash"], width=bar_width, label="Face Wash")
plt.title("Face Cream and Face Wash Sales")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.xticks(months)
plt.legend()
plt.tight_layout()
plt.show()

total_sales = {
    "Face Cream": df["facecream"].sum(),
    "Face Wash": df["facewash"].sum(),
    "Toothpaste": df["toothpaste"].sum(),
    "Bathing Soap": df["bathingsoap"].sum(),
    "Shampoo": df["shampoo"].sum(),
    "Moisturizer": df["moisturizer"].sum()
}

plt.figure(figsize=(6, 6))
plt.pie(total_sales.values(), labels=total_sales.keys(), autopct='%1.1f%%', startangle=140)
plt.title("Total Sales Share by Product (Yearly)")
plt.tight_layout()
plt.show()

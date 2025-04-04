import pandas as pd
data = {"Bike": ["BMW", "Ducati"], "Price": [500000, 450000]}
df = pd.DataFrame(data)
df.to_excel("bikes.xlsx", index=False)

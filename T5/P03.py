import pandas as pd
data = {"College": ["CEK", "CET"], "District": ["Kollam", "Thiruvananthapuram"]}
df = pd.DataFrame(data)
df.to_excel("colleges.xlsx", index=False)

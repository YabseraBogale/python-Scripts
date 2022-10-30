import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("passedwd.xlsx")
highest_letter=df.sort_values(by=["Number"]).drop(["Unnamed: 0"],axis=1).reset_index().drop(["index"],axis=1)

print(highest_letter["Number"].plot.bar())
print(highest_letter["Number"].tail().plot.bar())
plt.show()

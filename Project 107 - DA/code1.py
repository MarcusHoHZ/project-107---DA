import pandas as pd
import plotly.express as pe

df = pd.read_csv("data_2.csv")
newDataFrame = df.groupby("level")["attempt"].mean()
fig = (pe.scatter(df,x = newDataFrame, y = ["level 1", 'level 2',  "level 3", "level 4"]))
fig.show()
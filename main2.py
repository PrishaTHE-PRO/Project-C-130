import pandas as pd
import csv

df=pd.read_csv("totalstars.csv")
print(df.shape)
del df["Star_name1"]
del df["Distance1"]
del df["Mass1"]
del df["Radius1"]
del df["Luminosity"]

print(df.shape)

print(list(df))
df.to_csv('main1.csv')


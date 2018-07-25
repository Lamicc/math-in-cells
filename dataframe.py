#python 2 script
import pandas as pd

y01 = pd.read_excel("Population_doublings_edited.xlsx",sheet_name=0)
y02 = pd.read_excel("Population_doublings_edited.xlsx",sheet_name=1)
y03 = pd.read_excel("Population_doublings_edited.xlsx",sheet_name=2)
y04 = pd.read_excel("Population_doublings_edited.xlsx",sheet_name=3)
y05 = pd.read_excel("Population_doublings_edited.xlsx",sheet_name=4)
y06 = pd.read_excel("Population_doublings_edited.xlsx",sheet_name=5)

y = [y01,y02,y03,y04,y05,y06]

for i in range(len(y)):
    y[i] = y[i].dropna(axis=0, how='all')
    y[i] = y[i].dropna(axis=1, how='all')
    y[i].to_csv("Y0"+str(i+1)+".csv")

import pandas as pd
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn import preprocessing,cross_validation
from sklearn.linear_model import LinearRegression
g=pd.read_csv('feeds.csv')
g.rename(columns={'created_at':'DateTime'},inplace=True)
g.rename(columns={'entry_id':'Input Number'},inplace=True)
g.rename(columns={'field1':'Pollution'},inplace=True)
print(g)
print("Mean value:")
print(g['Pollution'].mean())
print("Maximum Value:")
print(g['Pollution'].max())
print(g.query("['829'] in Pollution"))
print("Minimum Value:")
print(g['Pollution'].min())
print(g.query("['10'] in Pollution"))
print(g['Pollution'].value_counts())
print("Maximum pollution intensity list:")
print(g.query("['734'] in Pollution"))
print(g.query("['740'] in Pollution"))
print(g.query("['758'] in Pollution"))
print(g.query("['738'] in Pollution"))
print(g.query("['725'] in Pollution"))
print(g.query("['735'] in Pollution"))
print("Minimum pollution intensity list:")
print(g.query("['492'] in Pollution"))
print(g.query("['491'] in Pollution"))
print(g.query("['489'] in Pollution"))
print(g.query("['391'] in Pollution"))
print(g.query("['369'] in Pollution"))
print(g.query("['351'] in Pollution"))

g['Pollution'].fillna((g['Pollution'].mean()), inplace=True)   

g['DateTime']=g['DateTime'].replace('UTC','')
t=g.DateTime.str.slice(10,13).astype(int)
t.values.reshape(-1,1)
t=np.array(t)

q=g['Pollution']
q.values.reshape(-1,1)
q=np.array(q)
    

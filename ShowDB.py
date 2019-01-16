import pandas as pd
import pickle

data = [['Alex',10],['Bob',12],['Clarke',13]]


Data=pickle.load(open("DataAnalysed.pkl", 'rb'))
print(len(Data))
AllData=[]
for data in Data:
	print(len(data))
	AllData=AllData+data
print(len(AllData))
df = pd.DataFrame(AllData,columns=['Description', 'CompanyName', 'Count', 'Type', 'Complexity'],dtype=float)
print (df.head())
df.to_csv("ComplicatedStatements.csv", sep='|')

from bs4 import BeautifulSoup
import requests as req
class StorageUnit:
    def __init__(self, Description, CompanyName, Count, Type, Complexity):
        self.Description=Description
        self.CompanyName=CompanyName
        self.Count=Count
        self.Type=Type
        self.Complexity=Complexity
    def Serialized(self):
        return [self.Description, self.CompanyName, self.Count, self.Type, self.Complexity]

# help(BeautifulSoup)
AllInformation=[]
for i in range(1,13):
    url="https://www.sih.gov.in/sih2019ProblemStatements/QWxs/U29mdHdhcmU=/Q29tcGxleA==/QWxs/QWxs?page="+str(i)
    webpage=req.get(url)
    # print(webpage.text)
    soup = BeautifulSoup(webpage.content, "html.parser")


    # In[170]:


    allRows=soup.tbody
    Rows=allRows.find_all("tr")


    # In[171]:





    # In[172]:


    len(Rows)


    # In[173]:


    AllData=[]
    for rows in range(len(Rows)):
        td=Rows[rows].find_all("td")
    #     foo=("none","none","none","none","none")
        Info=StorageUnit("none","none","none","none","none")
        for i in [1,3,9,10,11]:
            try:
                data=BeautifulSoup(str(td[i]), "html.parser")
                if(data.div!=None):
                    if(data.div.string!=None and data.div.string!=" "):
    #                     print(data.div.string,"bbb")
                        Info.Description=data.div.string
                        continue
                if(data.td.string!=None and data.td.string!=" "):
    #                 print(data.td.string.strip(),"aaa")
                    if(i ==1):
                        Info.CompanyName=data.td.string.strip()
                    elif(i ==9):
                        Info.Count=data.td.string.strip()
                    elif(i ==10):
                        Info.Type=data.td.string.strip()
                    elif(i ==11):
                        Info.Complexity=data.td.string.strip()
                        
            except:
                pass
        print("\n")
        print(Info.Description)
        AllData.append(Info.Serialized())


    # In[174]:


    while(['none', 'none', 'none', 'none', 'none'] in AllData):
        AllData.remove(['none', 'none', 'none', 'none', 'none'])


    # In[176]:


    for i in AllData:
        print(i[1])
    AllInformation.append(AllData)
import pickle
pickle.dump(AllInformation,open("DataAnalysed.pkl", 'wb'))   




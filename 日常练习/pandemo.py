import pandas as pd 
import json
data = pd.read_excel('data.xlsx')
# print(data["状态码预期"][0])
print(json.loads(data["参数"][0])["username"])
data1 = pd.read_excel('data.xlsx',sheet_name="Sheet1")
data1["id"] = range(1,101)
data1.to_excel('data.xlsx',"Sheet1")

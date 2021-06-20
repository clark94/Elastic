import pandas as pd
import json




with open('shakespeare1.json','r') as arq:
    data = json.load(arq)


columns = [dct['name'] for dct in data['columns']]

#print(columns)
df = pd.DataFrame(data['rows'], columns=columns)

print(df)

#df.to_csv('shake.csv')


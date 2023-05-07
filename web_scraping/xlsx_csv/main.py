import pandas as pd

# Đọc file xlsx 
df = pd.read_excel('data.xlsx')

df.to_csv('student_score_vnua/data.csv' , index=False)

import ast
import numpy as np
import pandas as pd

# Đọc dữ liệu từ tệp CSV
with open('C:/Users/ramma/Desktop/app_web_scraping/web_scraping/student_score_vnua/data_diem_vnua.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Chuyển đổi chuỗi thành danh sách và mảng
data = []
for line in lines:
    msv, hoc_ki, dtb = line.strip().split(',')
    hoc_ki = ast.literal_eval(hoc_ki)
    dtb = np.array(ast.literal_eval(dtb))
    data.append([msv, hoc_ki, dtb])

# Tạo DataFrame và chuyển đổi thành tệp Excel
df = pd.DataFrame(data, columns=['msv', 'hoc ki', 'dtb'])
df.to_excel('C:/Users/ramma/Desktop/app_web_scraping/web_scraping/student_score_vnua/data_diem_vnua.xlsx', index=False)

import requests
from bs4 import BeautifulSoup as Soup
import csv

with open('data.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    file_name ="data_diem_vnua.csv"
    with open(file_name, 'w', encoding='utf-8') as f:
        header = '"msv"," hoc ki", "dtb"\n'
        f.write(header)
        
        for row in reader:
            msv = row[1]
            url = f"https://daotao.vnua.edu.vn/Default.aspx?page=xemdiemthi&id={msv}"
            response = requests.get(url)
            content = response.content

            # print(url)
            page_html = Soup(content, 'html.parser')
            try:
                name_titles = page_html.find_all('tr', {'class': 'title-hk-diem'})
                data_name_titles = []
                for name_title in name_titles:
                    td_name_titles = name_title.find_all('td')
                    for td_name_title in td_name_titles:
                        span_name_titles = td_name_title.find_all('span')
                    for span_name_title in span_name_titles:
                        hk_title = span_name_title.text
                        data_name_titles.append(hk_title)
                        print('hk_title', data_name_titles)
            except:
                print("Error")
            try:
                diem_trung_binhs=[]
                dtbs = page_html.find_all('span', string='Điểm trung bình học kỳ hệ 4:')
                data_dtb = []
                for dtb in dtbs:
                    diem_trung_binh = dtb.find_next_sibling('span')
                    for diem_trung_binh_end in diem_trung_binh:
                        diemtrungbinh= diem_trung_binh_end.text
                        diem_trung_binhs.append(float(diemtrungbinh))
            except AttributeError:
               diemtrungbinh = 'N/A'
            print('name :',msv)
            print('diem_trung_binhs :' , diem_trung_binhs)
            # Viết thông tin về sinh viên và điểm số vào tệp CSV mới
            data_row = [msv, ','.join(data_name_titles), ','.join(map(str, diem_trung_binhs))]
            data_row = [f'"{x}"' for x in data_row]
            f.write(','.join(data_row) + '\n')
        f.close()
       


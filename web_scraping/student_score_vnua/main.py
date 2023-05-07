import requests
from bs4 import BeautifulSoup as Soup
import csv

with open('data.csv') as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        msv = row[1]

        url = f"https://daotao.vnua.edu.vn/Default.aspx?page=xemdiemthi&id={msv}"
        response = requests.get(url)
        content = response.content

        # print(url)
        page_html = Soup(content, 'html.parser')

    

        try:
            name_titles = page_html.find_all('tr', {'class': 'title-hk-diem'})
            for name_title in name_titles:
                td_name_titles = name_title.find_all('td')
                for td_name_title in td_name_titles:
                    span_name_titles = td_name_title.find_all('span')
                    for span_name_title in span_name_titles:
                        print(span_name_title.text)
        except:
            print("Error")


    
   


        try:
            dtbs = page_html.find_all('span', text='Điểm trung bình học kỳ hệ 4:')
            diem_trung_binhs =[]
            for dtb in dtbs:
                #append them mot phan tu vao cuoi danh sach 
                diem_trung_binhs.append(dtb.find_next_sibling('span').text)
            if not diem_trung_binhs:
                diem_trung_binh = "N/A"
            else:
                diem_trung_binh = ','.join(diem_trung_binhs)
        except AttributeError:
            dtb = 'N/A'
        print('name :',msv)
        print('hk_title', span_name_title)
        print('dtb :', diem_trung_binh)


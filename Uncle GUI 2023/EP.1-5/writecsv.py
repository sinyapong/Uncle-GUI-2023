import csv

def wirtecsv(data):
    # data = ['ค่ารถเมล์ BTS',10,'2023-01-11 9:00:05']  # fomat เป็น list
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)  
        
        
wirtecsv(['apple',20,'2023-01-11 10:00:05'])
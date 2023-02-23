from tkinter import *
from tkinter import ttk
import csv
from datetime import datetime  # strftime.org


# ========== CSV =====================================
def wirtecsv(data):
    # data = ['ค่ารถเมล์ BTS',10,'2023-01-11 9:00:05']  # fomat เป็น list
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)
# ===================================================== 

GUI = Tk()
GUI.title("โปรแกรมบันทึกค่าใช้จ่าย")
GUI.geometry("600x600")

FONT1 = ('Angsana New', 25)

# Image
# icon1 = r"C:\Users\ying4\OneDrive\Desktop\Uncle GUI 2023\images\expense.png"
icon = "C:\\Users\\ying4\\OneDrive\\Desktop\\Uncle GUI 2023\\images\\expense.png"
iconimage = PhotoImage(file=icon)
L = Label(GUI, image=iconimage)
L.pack(pady=10)

# Label
L = Label(GUI, text="รายการค่าใช้จ่าย", font=(None, 20))
L.pack(pady=5)

# Entry
v_expense = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_expense,font=FONT1)
E1.pack(pady=5)

L = Label(GUI, text="จำนวนเงิน (บาท)", font=(None, 20))
L.pack(pady=5)

v_amount = StringVar()
E2 = ttk.Entry(GUI, textvariable=v_amount,font=FONT1)
E2.pack(pady=5)

def SaveData(event=None):
    expence = v_expense.get()
    amount = float(v_amount.get())
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = [expence, amount, timestamp]
    wirtecsv(data)
    v_expense.set('')
    v_amount.set('')
    E1.focus()
    
E2.bind('<Return>', SaveData)
E1.bind('<Return>', lambda x:E2.focus())

def Fav1(event=None):
    v_expense.set('น้ำเต้าหู้')
    v_amount.set('15')
    
GUI.bind('<F1>', Fav1)
    
iconEnter = "C:\\Users\\ying4\\OneDrive\\Desktop\\Uncle GUI 2023\\images\\iconEnter.png"
iconimage2 = PhotoImage(file=iconEnter)
B1 = ttk.Button(GUI, text="บันทึก",command=SaveData, image=iconimage2, compound='top')
B1.pack(ipadx=20,ipady=10,pady=20)





GUI.mainloop()
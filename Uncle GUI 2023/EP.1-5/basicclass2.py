class Product:
    # Attribute
    # name = 'Water'
    # quantity = 3
    # price = 8.50
    
    # Consturctor
    def __init__(self, name='Water', quantity=3, price=8.5):
        self.name = name
        self.quantity = quantity
        self.price = price 
    
    # Method
    def hello(self):
        print('สวัสดีคุณลูกค้าร้าน Uncle Shop')
        
# ===================================================================================================

class Customer(Product):
    def __init__(self, fullname, money, name, quantity, price):
        super().__init__(name, quantity, price)
        self.fullname = fullname
        self.money = money
        
    def calculate(self):
        self.total = self.quantity * self.price
        self.money -= self.total
        print(f'เหลือเงิน {self.money} บาท')
        
    
     
# Instance

# product1 = Product()
# product1 = Product('Coffee', 2, 15)
# print(product1.name)  
# print(product1.quantity)
# print(product1.price)
# product1.hello()  # การเรียกใช้ method
# print("="*30)

# product2 = Product('Juice', 5, 20)
# print(product2.name)  
# print(product2.quantity)
# print(product2.price)
# # print(type(product1))  #<class '__main__.Product'>
# # print(type(product2))
# print("="*30)
# customer1 = Customer('Somchai sabuydee', 500 )
# print(customer1.fullname)
# print(customer1.money)

if __name__=='__main__':
    customer2 = Customer('Somying jingjai', 1000, 'Juice', 5, 20)
    print(customer2.fullname)
    print(customer2.money)
    customer2.calculate()
    print("="*30)
    customer3 = Customer('Somchai sabuydee', 500,'Tea', 2, 17)
    print(f'{customer3.fullname} มีเงิน {customer3.money} ซ์้อ {customer3.name} จำนวน {customer3.quantity} ราคา {customer3.price} บาท' ) 
    customer3.calculate()
    print("="*30)


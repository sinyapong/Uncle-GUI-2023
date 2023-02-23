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
        
        
# Instance

# product1 = Product()
product1 = Product('Coffee', 2, 15)
print(product1.name)  
print(product1.quantity)
print(product1.price)
product1.hello()  # การเรียกใช้ method
print("="*30)

product2 = Product('Juice', 5, 20)
print(product2.name)  
print(product2.quantity)
print(product2.price)

# print(type(product1))  #<class '__main__.Product'>
# print(type(product2))
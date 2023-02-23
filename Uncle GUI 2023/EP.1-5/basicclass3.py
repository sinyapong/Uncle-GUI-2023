from basicclass2 import Product, Customer

class StaticClass:
    def run():
        print('This is Method StaticClass')

if __name__=='__main__':
    product = Product('Coke', 10, 10)
    print(product.name)
    print(product.quantity)
    print(product.price)
    
    customer = Customer('fullname', 500, 'name', 10, 1)
    print(customer.calculate())
    
    StaticClass.run()
    
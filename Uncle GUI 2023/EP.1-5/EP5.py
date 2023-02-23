class Person:
    def __init__(self, fname, lname, ages, department):
        self.fname = fname
        self.lname = lname
        self.ages = ages
        self.department = department
    
    def hello(self):
        print(f'สวัสดีคุณ {self.fname} {self.lname}')
        
    def age(self):
        print(f'คุณ {self.fname} อายุ {self.ages} ปี')
        
    def depart(self):
        print(f'คุณทำงานตำแหน่ง {self.department} นะ')
        
# ===================================================================================================

if __name__=='__main__':

    person1 = Person("Konon","Kung",9,"Detective")
    person1.hello()
    person1.age()
    person1.depart()

class Student:
    def __init__(self,phys,chem,math):
        self.phys=phys
        self.chem=chem
        self.math=math

    @property
    def percentage(self):
        return str((self.phys+self.chem+self.math)/3) + "%"




stud1=Student(100,100,100)
print(stud1.percentage)

stud1.phys=99
print(stud1.percentage)


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def get_avg(self):
        sum=0
        count=0
        for val in self.marks:
            count+=1
            sum+=val
        print("The average marks of the students",sum/count)


s1=Student("Tony Stark",[98,89,78,47])
s1.get_avg()

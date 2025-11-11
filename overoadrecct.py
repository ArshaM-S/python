class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def __lt__(self,other):
        return self.area()<other.area()
length1=int(input("Enter the length of first rectangle:"))
width1=int(input("Enter the width of first rectangle:"))
length2=int(input("Enter the length of second rectangle:"))
width2=int(input("Enter the width of second rectangle:"))
r1=Rectangle(length1,width1)
r2=Rectangle(length2,width2)
print("Area of fisrt Rectangle:",r1.area())
print("Area of second Rectangle:",r2.area())

if r1<r2:
    print("first Rectangle has smaller area")
else:
    print("second Rectangle has smaller area")

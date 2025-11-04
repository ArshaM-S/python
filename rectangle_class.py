class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)

length1=int(input("Enter the length of the first rectangle: "))
breadth1=int(input("Enter the breadth of the first rectangle: "))
length2=int(input("Enter the length of the second rectangle: "))
breadth2=int(input("Enter the breadth of the second rectangle: "))
r1=Rectangle(length1,breadth1)
r2=Rectangle(length2,breadth2)

print("Area of first rectangle: ",r1.area())
print("Perimeter of first rectangle: ",r1.perimeter())
print("Area of second rectangle: ",r2.area())
print("Perimeter of second rectangle: ",r2.perimeter())

if r1.area() > r2.area():
    print("Area of first rectangle is greater.")
else:
    print("Area of second rectangle is greater.")

    

names=[]
account=0
n=int(input("Enter the number of first names: "))
print("Enter the names: ")
for i in range(1,n+1):
    name = input()
    names.append(name)
for name in names:
    account+=name.lower().count('a')
print("Number of a : ",account)

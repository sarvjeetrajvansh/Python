lst = []

for i in range(5) :
    inp = input("Enter a string: ")
    lst.append(inp)
print(lst)
result=""    
for j in range(3) :
    inpt = int(input("Enter a number: "))
    result+=lst[inpt]
print(result)
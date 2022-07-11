# for loops

for i in range(10) :
    print(i,end=",")
# 0 1 2 3 4 5 6 7 8 9 

print() # for new line

for i in range(1,11) :
    print(i,end=",")
    
# 1 2 3 4 5 6 7 8 9 10

print()
# range(start,stop,step)
for i in range (1,11,2) :
    print(i,end=",")
# 13579

# pritn char to ascii
print()
inp_char = input("Enter a char : ")
print(ord(inp_char))

# pritn ascii to char
print()
inp_num= int(input("Enter a num : "))
print(chr(inp_num))

"""
NOT > AND > OR
/ , * , + , - , % , // , **
"""

print(2**2)
print(2*2)

print(2/2)
print(2//2)

print(2%2)
print(2+2,2-2)

if 2+2 >=4 and 2*2 >= 4 :
    print("passed")

if 2%2 == 1 or 2/2 ==1 :
    print("pass by margin")
if not 2/2 == 1 :
    print("passed")
else :
    print("failed")
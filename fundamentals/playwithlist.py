lst = [1,2,3,4,5]

# index iteration
for i in range(len(lst)) :
    print(lst[i],end=" ")
    print(i)
    
# element iteration
print()

for i in lst :
    print(i)
    
# index and element iteration
print()

for i,e in enumerate(lst):
    print(i,end=" ")
    print(e)
print()

for i in range(3):
    pass  # pass the cursor


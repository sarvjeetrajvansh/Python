# find max length subarray sum = 0 

from audioop import reverse


lst = [3,6,10,5,3,5,6,3,6,5,10,6,5] # PF sum of array



# ----

chars = set()

while True:
    char = input("Enter a character: ")

    if len(char) > 1 : 
        break
    if char in chars : 
        break
    chars.add(char)
print(f"Number of unique characters entered: {len(chars)}")



x = set()
x = {(1,2),(2,3)}
print((1,2) in x) # return true in python
frequency = {}

word = input("Enter your name :")

for char in word:
    frequency[char]=frequency.get(char,0) + 1
    
print(frequency)
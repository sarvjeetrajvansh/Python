x = "global"

def foo():
    global x
    print(x, end=",")
    x = "local"
    print(x, end=",")

foo()
print(x, end="")
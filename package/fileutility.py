
def appender(filename : str , str :str):
    with open(filename,"r+") as file:
        file.write(str)
        print("Response Recieved !!")

def reader(file):
    with open(file,"r" )as lines:
        for line in lines:
            print(line)
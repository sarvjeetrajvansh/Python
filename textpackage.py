# import package

# url = "https://jsonplaceholder.typicode.com/todos/1"

# result = str(package.requester(url))
# package.appender("result.txt",result )
# package.reader("result.txt")

from package import requester , appender ,reader

url = "https://jsonplaceholder.typicode.com/todos/1"

result = str(requester(url))
appender("result.txt",result )
reader("result.txt")
from package import requester , appender ,reader

url = "https://jsonplaceholder.typicode.com/todos/1"

result = str(requester(url))
appender("result.txt",result )
reader("result.txt")
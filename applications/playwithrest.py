from package import requester
from package import appender , reader

url = "https://jsonplaceholder.typicode.com/todos/1"

result = str(requester(url))
appender("result.txt",result )
reader("result.txt")
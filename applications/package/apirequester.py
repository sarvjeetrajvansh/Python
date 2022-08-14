from urllib import response
import requests

def requester(url):
    response = requests.get(url)
    return response.json()
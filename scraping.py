from bs4 import BeautifulSoup
import requests

url = "https://www.wavsource.com/people/people.htm&quot"

result = requests.get(url)
print(result.text)
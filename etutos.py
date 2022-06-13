from bs4 import BeautifulSoup
import requests

def pull_tos():
    url = input("Please enter url: ")
    content = requests.get(url).content
    
    paragraphs = BeautifulSoup(content, 'html.parser').find_all('p')
    for p in paragraphs:
        print(p.get_text("\n",strip = True))


pull_tos()
from bs4 import BeautifulSoup
import requests

def intro_message():
    message = "Welcome to ETOTUS (Easy to Understand Terms of Service)! This tool is in active development, so please submit all issues or comments to the github repository at https://github.com/micsport13/etutos/issues. \n"
    print(message)
def pull_tos():
    url = input("Please enter url: ")
    content = requests.get(url).content
    try:
        test = requests.get(url)
        test.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("A connection error occurred, please check your internet")
        return 1
    except requests.exceptions.ConnectTimeout:
        print("The request timed out.")
        return 1
    except requests.exceptions.HTTPError:
        print("An HTTP Error occurred.  Please check the url.")
    
    headers = BeautifulSoup(content, 'html.parser').find_all('div', role = "article")
    paragraphs = BeautifulSoup(content, 'html.parser').find_all('p')
    tos = ""
    for p in paragraphs:
        tos += p.get_text("\n",strip = True)
    return tos

def tos_parser(tos):
    tos = str(tos)
    if tos.find("legal guardian")>= 0 or tos.find("parent")>=0:
        print("FIXME: Add what requirements for parental or guardian consent")

def test():
    url = input("Please enter url: ")
    content = requests.get(url).content
    
    headers = BeautifulSoup(content, 'html.parser').find_all('div', id != "license", role = "article")
    paragraphs = BeautifulSoup(content, 'html.parser').find_all('p')
    bullet_points = BeautifulSoup(content, 'html.parser').find_all('li')
    for p in headers:
        print(p.get_text("\n", strip = True))
    

intro_message()
tos_parser(pull_tos())


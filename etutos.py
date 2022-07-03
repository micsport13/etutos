from bs4 import BeautifulSoup
import requests
import re


def intro_message():
    message = '''\
    Welcome to ETOTUS! (Easy to Understand Terms of Service) 
    This tool is in active development, so please submit all issues or comments to the github repository at 
    https://github.com/micsport13/etutos/issues.'''
    print(message)


def pull_tos(url):
    title = re.search("[a-z]*(?=.com)", url).group(0).upper()
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

    headers = BeautifulSoup(content, 'html.parser').find_all(
        'div', role="article")
    paragraphs = BeautifulSoup(content, 'html.parser').find_all('p')
    tos = title + "\n" + ""
    for p in paragraphs:
        tos += p.get_text("\n", strip=True)
    return tos


def tos_parser(tos: str):
    if tos.find("legal guardian") >= 0 or tos.find("parent") >= 0:
        print("FIXME: Add what requirements for parental or guardian consent")


def input_url():
    url = input("Please enter url: ")
    if url.find("https://") == -1 and url.find("https://") == -1:
        print("Please input a valid URL.")
        input_url()
    if url.find("terms") == -1:
        print("Are you sure this is the address of the terms of service?")
        response = input("Y or N: ")
        if response.upper() == "Y":
            return url
        elif response.upper() == "N":
            print("Please input a valid terms of service page: ")
            input_url()
    else:
        return url


intro_message()
print(pull_tos(input_url()))

from bs4 import BeautifulSoup
from requests import get
from termcolor import colored

def get_link(link):
    #link = sys.argv[1]

    res = get(str(link)).text
    soup = BeautifulSoup(res, features="html.parser")

    ryan = []

    for linkk in soup.find_all('a', href=True):
        if(linkk['href'].find('http://ps4.downloadha.com/') != -1 or linkk['href'].find('_www.Downloadha.com_') != -1):
            ryan.append(linkk['href'])
    
    return ryan

search_word = input("What do you want> ")

search_url = 'https://www.downloadha.com/?s='
full_search_url = search_url + search_word.replace(' ', '+')

urls = {}

soup = BeautifulSoup(get(full_search_url).text, features='html.parser')

for link in soup.find_all('a', href=True):
    if(link['href'].find('https://www.downloadha.com/game') != -1 and link['href'].find(search_word.split()[0]) != -1 and link['href'].find("#respond") == -1):
        urls[link['href'].replace('https://www.downloadha.com/game','').replace('/','')] = link['href']

for i in urls.keys():
    print(i)

chosen_game = input("Enter the exact name of game> ")

try:
    download_urls = get_link(urls[chosen_game])
    for i in download_urls:
        print(colored('\t{}'.format(i), 'red'))
except:
    print("Error!")
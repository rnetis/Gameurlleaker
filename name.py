from requests import get
from bs4 import BeautifulSoup
import main
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

download_game_urls = {}

link = "https://www.downloadha.com/category/%D8%A8%D8%A7%D8%B2%DB%8C-%DA%A9%D9%86%D8%B3%D9%88%D9%84-console-game/%D8%A8%D8%A7%D8%B2%DB%8C-ps4/page/"

should_exist = "https://www.downloadha.com/game/" 

try:
    for i in range(1,20):
        #Leaking Game Page Url
        res = get(str(link) + str(i)).text
        soup = BeautifulSoup(res, features="html.parser")

        for linkk in soup.find_all('a', href=True):
            if(linkk['href'].find(should_exist) != -1 and linkk['href'].find('ps4') != -1 and linkk['href'].find('#respond') == -1):
                #print(linkk['href'])
                download_game_urls[linkk['href'].replace(should_exist,'').replace('/','')] = linkk['href']

    for i in urls.keys():
        print(colored("\t***{}***".format(i), 'red'))
        #Print Download Game Urls
        for links_of_url in get_link(urls[i]):
            print(links_of_url)
except:
    print(colored("Somthing Happend!\nGoodbye", 'red'))
import requests
import functions as fn
from urllib.parse import urlparse
from bs4 import BeautifulSoup

URL = "https://community.o2.co.uk/t5/Discussions-Feedback/bd-p/4"
domain = urlparse(URL).netloc #community.o2.co.uk

#On va récupérer toutes les pages des articles (environ 930 pages)
for all_pages in range(1):
    page = requests.get(URL+'/page/'+str(all_pages)+'/')
    soup = BeautifulSoup(page.content, "html.parser") #récupère le contenu de la page et parser

    articles = [] #récupère tous les titres et url des articles
    
    # Récupère tous les articles
    results = soup.find_all("article", class_="custom-message-tile")
    print(results)
    # Récupère tous les titres et urls des articles
    for thread_title in results:
        first_element = thread_title.find("div") # get first children - the div
        lien = first_element.find("a")
        
        titre = lien["title"] # get the title and save it 
        url = lien["href"] # get the link towards the post of the thread 
        articles.append((titre, url)) 

    chemin = r"C:\Users\devia.e16\Documents\GitHub\forum_scrapper\liste titre d'article.txt"
    with open(chemin, 'a') as f:
        f.write(f"{articles}")

print(f'Number of post extracted for the thread "{articles[0]}": {len(thread_posts)}')

reponsesDeLarticle = soup.find_all_next(class_='lia-message-body-content')
pageArticle = URL + url
page = requests.get(pageArticle)
soup = BeautifulSoup(page.content, 'html.parser')

for reponse in reponsesDeLarticle:
    reponse = reponsesDeLarticle.findNext('p')
    #contenuReponse = reponsesDeLarticle.find('p')
    print(reponse.text)
    
    


"""
import requests
import functions as fn
from urllib.parse import urlparse
from bs4 import BeautifulSoup

URL = "https://community.o2.co.uk/t5/Discussions-Feedback/bd-p/4"
domain = urlparse(URL).netloc #community.o2.co.uk

#On va récupérer toutes les pages des articles (environ 930 pages)
for all_pages in range(1,10):
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
        
        threadContent = fn.getSoupObject(domain,url)
        #Récupérer toutes les réponses des articles
        for 
        
        posts_Content = fn.getPostsFromPage(threadContent,posts_Content)
        print(posts_Content)

    chemin = r"C:\Users\devia.e16\Documents\GitHub\forum_scrapper\liste titre d'article.txt"
    with open(chemin, 'a') as f:
        f.write(f"{articles}")

"""

""" FRIGO qui fonctionne récupère toutes les pages mais pas la celle de la première page
    URL = "https://community.o2.co.uk/t5/Discussions-Feedback/bd-p/4"
    domain = urlparse(URL).netloc #community.o2.co.uk

    #On va récupérer toutes les pages des threads (environ 930 pages)
    for all_pages in range(1,3):
        page = requests.get(URL+'/page/'+str(all_pages)+'/')
        soup = BeautifulSoup(page.content, "html.parser") #récupère le contenu de la page et parser

        threads = [] #récupère tous les titres et url des articles
        
        # get all articles
        results = soup.find_all("article", class_="custom-message-tile")

        # get all threads titles and urls
        for thread_title in results:
            first_element = thread_title.find("div") # get first children - the div
            link = first_element.find("a")
            
            title = link["title"] # get the title and save it 
            url = link["href"] # get the link towards the post of the thread 
            threads.append((title, url)) #titre et url des articles
        #print(threads)

        chemin = r"C:\Users\devia.e16\Documents\GitHub\forum_scrapper\liste titre d'article.txt"
        with open(chemin, 'w') as f:
            f.write(f"{threads}")


    # get all post content for each thread
    all_thread_posts = [] #toutes les réponses posté sous les articles
    for thread in threads: #Pour chaque article dans les articles
        thread_posts = [] #réponses posté sous un article
        thread_url_path = thread[1] #récupère le chemin de l'url du fil d'article

        soupObject = fn.getSoupObject(domain, thread_url_path) #Laurent: je reconstitue l'url de l'article, j'y vais dans l'article et je soup tout le contenu de l'article + reponses

        thread_posts = fn.getPostsFromPage(soupObject, thread_posts) #Depuis la soup, je filtre sur les Div lia-message-body-content et je récupère les réponses
        next_page_url = fn.getNextPageUrl(soupObject) #depuis la soup, je récupère l'url de la page suivante des reponses
        while next_page_url:
            # get all posts for given a page
            #print(next_page_url)
            next_page_url_path = urlparse(next_page_url).path
            soupObject = fn.getSoupObject(domain, next_page_url_path)
            thread_posts = fn.getPostsFromPage(soupObject, thread_posts)
            next_page_url = fn.getNextPageUrl(soupObject)
        
        #all_thread_posts.append(thread_posts)

        chemin = r"C:\Users\devia.e16\Documents\GitHub\forum_scrapper\Toutes les réponses.txt"
        with open(chemin, 'w') as f:
            f.write(f"{all_thread_posts}")   

        print(f'Number of post extracted for the thread "{thread[0]}": {len(thread_posts)}')
        all_thread_posts.append((thread[0], thread_posts)) # adding tuples with the title of a thread and the array containing all the posts content of a thread
        print("Number of threads scrapped:", len(all_thread_posts))
        #print(threads)
        
    print("the scrapping task is finished")
    # TODO store data into a CSV or relational database
"""

""" FRIGO Création fichier fxt 
chemin = r"C:\Users\devia.e16\Documents\GitHub\forum_scrapper\Toutes les réponses.txt"
with open(chemin, 'a') as f:
f.write(f"{all_thread_posts}")
"""

""" FRIGO Création fichier txt
        chemin = r"C:\Users\devia.e16\Documents\GitHub\forum_scrapper\liste titre d'article.txt"
        with open(chemin, 'a') as f:
            f.write(f"{threads}")
"""            
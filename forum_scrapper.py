
import requests
import functions as fn
from urllib.parse import urlparse
from bs4 import BeautifulSoup

URL = "https://community.o2.co.uk/t5/Discussions-Feedback/bd-p/4"
domain = urlparse(URL).netloc #community.o2.co.uk

#threads = [] #récupère tous les titres et url des articles de la page traitée en cours (13 par pages)

allThreads = [] #récupère les titres et url des articles de chaque page (13 x 931 pages)

#get all post content for each thread
all_thread_posts = [] #toutes les réponses posté sous les articles

#On va récupérer toutes les pages des threads (environ 930 pages)
for all_pages in range(1,3):
    page = requests.get(URL+'/page/'+str(all_pages)+'/')
    soup = BeautifulSoup(page.content, "html.parser") #récupère le contenu de la page et parser

    threads = [] #récupère tous les titres et url des articles de la page traitée en cours (13 par pages)
    
    #get all post content for each thread
    #all_thread_posts = [] #toutes les réponses posté sous les articles
    
    # get all articles
    results = soup.find_all("article", class_="custom-message-tile")

    # get all threads titles and urls
    for thread_title in results:
        first_element = thread_title.find("div") # get first children - the div
        link = first_element.find("a")
        
        title = link["title"] # get the title and save it 
        url = link["href"] # get the link towards the post of the thread 
        
        threads.append((title, url)) #titre et url des articles de la page en cours
        allThreads.append((title,url)) #titre et url des articles qui va s'accumuler au fil des pages

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

        all_thread_posts.append((thread[0], thread_posts)) # adding tuples with the title of a thread and the array containing all the posts content of a thread        
    
        print(f'Number of post extracted for the thread "{thread[0]}": {len(thread_posts)}')
        print("Number of threads scrapped:", str(len(all_thread_posts)) + str("/") + str(len(allThreads)))
        #print("Number of threads to be scrapped:", len(allThreads))

print("the scrapping task is finished")
# TODO store data into a CSV or relational database
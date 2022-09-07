import requests
import functions as fn
from urllib.parse import urlparse
from bs4 import BeautifulSoup

URL = "https://community.o2.co.uk/t5/Discussions-Feedback/bd-p/4"
domain = urlparse(URL).netloc #community.o2.co.uk

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

threads = []


# get all articles
results = soup.find_all("article", class_="custom-message-tile")


# get all threads titles and urls
for thread_title in results:
    first_element = thread_title.find("div") # get first children - the div
    link = first_element.find("a")
    
    title = link["title"] # get the title and save it 
    url = link["href"] # get the link towards the post of the thread 
    threads.append((title, url)) 
    
    chemin = r"/Users/laurentvergoz/Documents/GitHub/forum_scrapper/liste titre d'article.txt"
    with open(chemin, 'a') as f:
        f.write(f"{threads}")

    
     # TODO navigate through all the pages showing threads
        


# get all post content for each thread
all_thread_posts = []
for thread in threads:
    thread_posts = []
    thread_url_path = thread[1]
    soupObject = fn.getSoupObject(domain, thread_url_path)

    thread_posts = fn.getPostsFromPage(soupObject, thread_posts)
    next_page_url = fn.getNextPageUrl(soupObject) 
    while next_page_url:
        # get all posts for given a page
        #print(next_page_url)
        next_page_url_path = urlparse(next_page_url).path
        soupObject = fn.getSoupObject(domain, next_page_url_path)
        thread_posts = fn.getPostsFromPage(soupObject, thread_posts)
        next_page_url = fn.getNextPageUrl(soupObject)
        
    print(f'Number of post extracted for the thread "{thread[0]}": {len(thread_posts)}')
    all_thread_posts.append((thread[0], thread_posts)) # adding tuples with the title of a thread and the array containing all the posts content of a thread
    print("Number of threads scrapped:", len(all_thread_posts))
    
print("the scrapping task is finished")
# TODO store data into a CSV or relational database


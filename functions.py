import requests
from bs4 import BeautifulSoup
from urllib.parse import urlunparse


def getSoupObject(domain, url_path):
    thread_url = urlunparse(('https', domain, url_path, "", "", "")) # construct the url to access the posts for each thread
    page = requests.get(thread_url)
    soup = BeautifulSoup(page.content, "html.parser")

    return soup

def getPostsFromPage(soup, posts_content):
    thread_results = soup.find_all("div", class_="lia-message-body-content") #piege ici

    #print(thread_results)
    for page_posts_content in thread_results:
        body_content = page_posts_content.get_text()   
        posts_content.append(body_content)
    return posts_content


def getNextPageUrl(soup):
    # get to next page 
    all_next_page_link_components = soup.find_all("li", class_="lia-paging-page-next")
    
    if len(all_next_page_link_components) < 2: # case where the thread just have one page to navigate
        return None
    
    next_page_link_component = all_next_page_link_components[1] # second child makes reference to the url we need
    
    if not next_page_link_component: #case where there is just one navigation page
        return None
    
    link = next_page_link_component.find("a")
    if not link: #case were we checked all the navigation pages
        return None
    else:
        next_page_url = link["href"] # get the url for the next page 
    return next_page_url


""" FRIGO
def getSoupObject(domain, url_path):
    thread_url = urlunparse(('https', domain, url_path, "", "", "")) # construct the url to access the posts for each thread
    page = requests.get(thread_url)
    soup = BeautifulSoup(page.content, "html.parser")

    return soup

def getPostsFromPage(soup, posts_content):
    thread_results = soup.find_all("div", class_="lia-message-body-content") #piege ici

    #print(thread_results)
    for page_posts_content in thread_results:
        body_content = page_posts_content.get_text()   
        posts_content.append(body_content)
    return posts_content


def getNextPageUrl(soup):
    # get to next page 
    all_next_page_link_components = soup.find_all("li", class_="lia-paging-page-next")
    
    if len(all_next_page_link_components) < 2: # case where the thread just have one page to navigate
        return None
    
    next_page_link_component = all_next_page_link_components[1] # second child makes reference to the url we need
    
    if not next_page_link_component: #case where there is just one navigation page
        return None
    
    link = next_page_link_component.find("a")
    if not link: #case were we checked all the navigation pages
        return None
    else:
        next_page_url = link["href"] # get the url for the next page 
    return next_page_url

"""    
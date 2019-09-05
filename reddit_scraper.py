import requests
import lxml
import re
from bs4 import BeautifulSoup

def get_page(url):
    return requests.get(url=url, headers={'User-agent': 'Bingo 0.1'})

def get_content():
    return get_page('https://www.reddit.com/').content

def get_soup():
    return BeautifulSoup(get_content(), 'html.parser')

def get_users(soup):
    user_list=[]
    anchor=soup.findAll('a')
    for data in anchor:
        if re.match(r"r/\w*", data.get_text()) is not None:
            user_list.append(data.get_text())
    return user_list

def get_latest_posts(soup):
    post_list=[]
    posts=soup.findAll('h3')
    for post in posts:
        post_list.append(post.get_text())
    return post_list

soup = get_soup()
print(get_latest_posts(soup))

import json
import hashlib
import sys
from multiprocessing import Process
#from PostgreSQL.database import database

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# progressbar
from tqdm import tqdm



def thread_article_crawl(url, profile):
    '''
    A helper thread function for article crawl
    :param profile: a profile of publisher website that this article belongs to
    :param conn_string: a psycopg2 connection setup string
    '''
    process = CrawlerProcess(get_project_settings())
    process.crawl('articles', url=url, profile=profile)
    process.start()


    '''
    output the article information from article database by article id
    '''
def output_article_to_txt(article_id):
    
    with open("test_article.txt", "w", encoding="utf-8") as output:
        output.write("Article Title: " + article[0]+"\n")
        output.write(article[1])

def scrape_articles(urls):
    '''

    scraping articles from given URLs. ALl results store in articles Table
    :param urls: a list of article URLs
    '''

    article_profiles = json.load(open("website_profiles/profiles.json"))

    for i in tqdm(range(len(urls))):
        url = urls[i]
        url_domain = url.split("/")[2].strip()
        print("Working")
        if url.split("/")[2].strip() in article_profiles:
            print("Working")
            profile = article_profiles[url_domain]
            # crawl article information
            p = Process(target=thread_article_crawl, args=(url, profile))
            p.start()
            p.join()
            

if __name__ == '__main__':
    urls = [""] 
    scrape_articles(urls)






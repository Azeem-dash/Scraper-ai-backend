from fastapi import APIRouter
import os
from app.models.index_request import IndexRequest

from app.services.article_scrapping import scrape_articles

websitesData = [
    {
        'base_url': 'https://www.3pillarglobal.com/',
        'search_url': 'search/?query=',
        'query': 'AI',  # You can change this to any query you like
        'article_selector': '.row.search-results .card',  # CSS selector for each article card
        'title_selector': '.card-title',  # CSS selector for the article title
        'output_file': 'articles.md',  # File to store the results
        'article_content_selector': '.paper'  # CSS selector for the paper (entire article) content
    },
    {
        'base_url': 'https://www.mendix.com/',
        'search_url': 'search-results/?search=',
        'query': 'Javascript', 
        'article_selector': '.grid-x.align-center.mv1 a',
        'title_selector': '.search-card__heading.heading5',
        'output_file': 'mendix_articles.md', 
        'article_content_selector': '#blog__content' 
    }
]

# File to store the scraped data

# Create the router
router = APIRouter()


# Endpoint to trigger scraping
@router.post("/scrape/")
def scrape(request: IndexRequest):
    index = request.index
    SCRAPED_DATA_FILE = websitesData[index]['output_file']

    # If data exists, do not scrape again.
    if os.path.exists(SCRAPED_DATA_FILE):
        return {"success": False, "message": "Data already scraped. Fetch it using /fetch."}

    scrape_articles(websiteMap=websitesData[index])  # Scrape the data and store it in the file
    return {"success": True, "message": "Scraping completed and data saved."}


# Endpoint to fetch the scraped data
@router.post("/fetch/")
def fetch(request: IndexRequest):
    index = request.index
    SCRAPED_DATA_FILE = websitesData[index]['output_file']

    # Check if the scraped data file exists
    if not os.path.exists(SCRAPED_DATA_FILE):
        return {"success": False, "message": "No scraped data available. Please scrape first."}

    # Read and return the scraped data
    with open(SCRAPED_DATA_FILE, 'r', encoding='utf-8') as file:
        data = file.read()
    
    articlesList = data.split('# ARTICLE ')
    articlesList = articlesList[1:]

    return {"success": True, "scraped_data": articlesList}

@router.get("/get_websites/")
def get_websites():
    base_urls = [website['base_url'] for website in websitesData]
    return {"success": True, "websites": base_urls}
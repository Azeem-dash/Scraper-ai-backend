from fastapi import APIRouter
import os

from app.services.article_scrapping import scrape_articles

websiteData = {
    'base_url': 'https://www.3pillarglobal.com/',
    'search_url': 'search/?query=',
    'query': 'AI',  # You can change this to any query you like
    'article_selector': '.row.search-results .card',  # CSS selector for each article card
    'title_selector': '.card-title',  # CSS selector for the article title
    'output_file': 'articles.md',  # File to store the results
    'article_content_selector': '.paper'  # CSS selector for the paper (entire article) content
}

# File to store the scraped data
SCRAPED_DATA_FILE = websiteData['output_file']

# Create the router
router = APIRouter()

# Endpoint to trigger scraping
@router.post("/scrape/")
def scrape():
    # If data exists, do not scrape again.
    if os.path.exists(SCRAPED_DATA_FILE):
        return {"success": False, "message": "Data already scraped. Fetch it using /fetch."}

    scrape_articles(websiteMap=websiteData)  # Scrape the data and store it in the file
    return {"success": True, "message": "Scraping completed and data saved."}


# Endpoint to fetch the scraped data
@router.get("/fetch/")
def fetch():
    # Check if the scraped data file exists
    if not os.path.exists(SCRAPED_DATA_FILE):
        return {"success": False, "message": "No scraped data available. Please scrape first."}

    # Read and return the scraped data
    with open(SCRAPED_DATA_FILE, 'r', encoding='utf-8') as file:
        data = file.read()
    
    articlesList = data.split('# ARTICLE ')
    articlesList = articlesList[1:]

    return {"success": True, "scraped_data": articlesList}

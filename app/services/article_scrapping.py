from typing import List
from playwright.sync_api import sync_playwright
from markdownify import markdownify as md

# Website map with the required selectors and configurations
# websiteMap = {
#     'base_url': 'https://www.3pillarglobal.com/',
#     'search_url': 'search/?query=',
#     'query': 'AI',  # You can change this to any query you like
#     'article_selector': '.row.search-results .card',  # CSS selector for each article card
#     'title_selector': '.card-title',  # CSS selector for the article title
#     'output_file': 'articles.md',  # File to store the results
#     'article_content_selector': '.paper'  # CSS selector for the paper (entire article) content
# }

# websiteMap = {
#     'base_url': 'https://www.mendix.com/',
#     'search_url': 'search-results/?search=',
#     'query': 'Javascript', 
#     'article_selector': '.grid-x.align-center.mv1 a',
#     'title_selector': '.search-card__heading.heading5',
#     'output_file': 'mendix_articles.md', 
#     'article_content_selector': '#blog__content' 
# }


# Scrape function
def scrape_articles(websiteMap):

    SCRAPED_DATA_FILE = websiteMap['output_file']
    articles_md = []  # This will store all articles in Markdown format

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        search_url = f"{websiteMap['base_url']}{websiteMap['search_url']}{websiteMap['query']}"
        page.goto(search_url)

        page.wait_for_selector(websiteMap['article_selector'], timeout=10000)

        # Get all article cards
        articles = page.query_selector_all(websiteMap['article_selector'])
        
        numOfArticles = 0
        for idx, article in enumerate(articles):
            if numOfArticles > 4:  # Limit to 5 articles
                break

            try:
                title_element = article.query_selector(websiteMap['title_selector'])
                title = title_element.inner_text() if title_element else "No title found"
                url = article.get_attribute('href')  # Get the article URL

                # Create the Markdown for the article header
                article_md = f"# ARTICLE {idx + 1}: {title}\n"
                article_md += f"[Read More]({url})\n"
                article_md += "-" * 50 + "\n\n"

                # Now go to the article page and get the content
                article_page = browser.new_page()
                article_page.goto(url)
                article_page.wait_for_selector(websiteMap['article_content_selector'], timeout=10000)

                article_content_html = article_page.query_selector(websiteMap['article_content_selector']).inner_html()
                article_content_md = md(article_content_html)

                article_md += f"{article_content_md}\n"
                article_md += "\n" + "=" * 50 + "\n\n"

                articles_md.append(article_md)  # Add to the list of articles
                numOfArticles += 1
                article_page.close()  # Close the article page after scraping

            except Exception as e:
                print(f"Error processing article {idx + 1}: {e}")
                continue  # Skip to the next article on error

        browser.close()

    # Save the scraped articles to a file
    with open(SCRAPED_DATA_FILE, 'w', encoding='utf-8') as file:
        file.writelines(articles_md)



# Scrape function
def scrape_3pillar(websiteMap) -> List[str]:
    articles_md = []  # This will store all articles in Markdown format

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        search_url = f"{websiteMap['base_url']}{websiteMap['search_url']}{websiteMap['query']}"
        page.goto(search_url)

        page.wait_for_selector(websiteMap['article_selector'], timeout=10000)

        # Get all article cards
        articles = page.query_selector_all(websiteMap['article_selector'])
        
        numOfArticles = 0
        for idx, article in enumerate(articles):
            if numOfArticles > 4:  # Limit to 5 articles
                break

            try:
                title_element = article.query_selector(websiteMap['title_selector'])
                title = title_element.inner_text() if title_element else "No title found"
                url = article.get_attribute('href')  # Get the article URL

                # Create the Markdown for the article header
                article_md = f"# Article {idx + 1}: {title}\n"
                article_md += f"[Read More]({url})\n"
                article_md += "-" * 50 + "\n\n"

                # Now go to the article page and get the content
                article_page = browser.new_page()
                article_page.goto(url)
                article_page.wait_for_selector(websiteMap['article_content_selector'], timeout=10000)

                article_content_html = article_page.query_selector(websiteMap['article_content_selector']).inner_html()
                article_content_md = md(article_content_html)

                article_md += f"{article_content_md}\n"
                article_md += "\n" + "=" * 50 + "\n\n"

                articles_md.append(article_md)  # Add to the list of articles
                numOfArticles += 1
                article_page.close()  # Close the article page after scraping

            except Exception as e:
                print(f"Error processing article {idx + 1}: {e}")
                continue  # Skip to the next article on error

        browser.close()

    return articles_md  # Return the list of articles in Markdown format

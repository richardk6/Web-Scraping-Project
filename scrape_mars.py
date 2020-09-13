from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import time

    
def init_browser():
        executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
        return Browser("chrome", **executable_path, headless=False)

def scrape_all():
    browser = init_browser()
    mars_dict = {}
    news_info = mars_news()
    mars_dict["mars_title"] = news_info[0]
    mars_dict["mars_paragraph"] = news_info[1]
    mars_dict["mars_image"] = mars_image()
    mars_dict["mars_facts"] = mars_facts()
    mars_dict["mars_hemisphere"] = hemispheres()

    return mars_dict

# Mars News

def mars_news():
    browser = init_browser()
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(10)

    html = browser.html
    soup = bs(html, "html.parser")

    title = soup.find("ul", class_="item_list")
    news_title = title.find("div", class_="content_title")

    news_p = soup.find("div", class_="article_teaser_body")

    news_info = [news_title, news_p]
    return news_info

# Mars Featured Image
def mars_image():
    browser = init_browser()
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(10)

    browser.click_link_by_partial_text('more info')
    time.sleep(10)

    html = browser.html
    soup = bs(html, "html.parser")

    space_image = soup.find('figure', class_="lede")

    featured_image_url = space_image.a["href"]

    featured_url = "https://www.jpl.nasa.gov" + featured_image_url

    return featured_url


# Mars Facts Table
def mars_facts():
    # Add try/except for error handling
    try:
        # use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]
    except BaseException:
        return None
    # assign columns and set index of dataframe
    df.columns = ['Description', 'Mars']
    df.set_index('Description', inplace=True)
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

# Mars Hemispheres 
def hemispheres():
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    time.sleep(10)

    hemisphere_image_urls = []
    
    for i in range(4):
        browser.find_by_css("a.product-item h3")[i].click()
        hemi_data = scrape_all_hemisphere(browser.html)
        hemisphere_image_urls.append(hemi_data)
        browser.back()
    
    return hemisphere_image_urls

# Close the browser after scraping
    browser.quit()
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

# Mars News

# def mars_news():
    #browser = init_browser()
    # url = "https://mars.nasa.gov/news/"
    # browser.visit(url)

    # time.sleep(10)

    #html = browser.html
    #soup = bs(html, "html.parser")

    #try:
        # title = soup.find("ul", class_="item_list")
        # news_title = title.find("div", class_="content_title")
    
        # news_p = soup.find("div", class_="article_teaser_body")
    
    # except AttributeError:
        # return None, None

    # mars_dict["mars_title"] = news_title
    # mars_dict["mars_p"] = news_p

# Mars Featured Image
# def mars_image():
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

    mars_dict["mars_image"] = featured_url


# Mars Facts Table
# def mars_facts():
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
    mars_table = df.to_html(classes="table table-striped")

    mars_dict["mars_facts"] = mars_table

# Mars Hemispheres 
# def hemispheres():
    browser = init_browser()

    # Visit website
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    hemisphere_image_urls = []
    hemi_data = browser.find_by_css("a.product-item h3")[1].click()
    hemisphere_image_urls.append(hemi_data)
    
    mars_dict["hemisphere_image_urls"] = hemisphere_image_urls

    return mars_dict

    # Close the browser after scraping
    browser.quit()
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import time

    
def init_browser():
        executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
        return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()
    mars_dict = {}

    # Mars News
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(10)

    html = browser.html
    soup = bs(html, "html.parser")

    title = soup.find("ul", class_="item_list")
    news_title = title.find("div", class_="content_title")

    news_p = soup.find("div", class_="article_teaser_body")

    mars_dict["news title"] = news_title
    mars_dict["news paragraph"] = news_p

    # Mars Featured Image
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

    mars_dict["featured url"] = featured_url


    # Mars Facts Table
    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)

    df = tables[0]
    df.columns = ["Planet Attributes", "Mars"]
    df.set_index("Planet Attributes", inplace=True)

    html_table = df.to_html()

    html_table.replace('\n', '')

    df.to_html('table.html')

    mars_dict['table.html'] = table.html

    # Mars Hemispheres 
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    time.sleep(10)

    response = requests.get(url)
    soup = bs(response.text, 'html.parser').find_all("a",class_ = "itemLink product-item")
    hemi_titles = []
    for i in soup:
        title = i.find("h3").text
        hemi_titles.append(title)

    hemi_imglist = []
    for x in range(len(hemi_titles)):
        try:
            browser.click_link_by_partial_text(hemi_titles[x])
        except:
            browser.find_link_by_text('2').first.click()
            browser.click_link_by_partial_text(hemi_titles[x])
    html = browser.html
    soup2 = bs(html, 'html.parser')
    hemi_soup = soup2.find('div', 'downloads')
    hemi_url = hemi_soup.a['href']
    
    hemi_dict={"title": hemi_titles[x], 'img_url': hemi_url}
    hemi_imglist.append(hemi_dict)

    hemisphere_image_urls = [
        {'title': 'Cerberus Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},
        {'title': 'Schiaparelli Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},
        {'title': 'Syrtis Major Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},
        {'title': 'Valles Marineris Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}
    ]
    
    mars_dict['hemisphere_images'] = hemisphere_image_urls

    # Close the browser after scraping
    browser.quit()
    
    return mars_dict


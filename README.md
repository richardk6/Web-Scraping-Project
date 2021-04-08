# web-scraping-project
Web-Scraping-Project.

Scraped a number of Mars websites to put together an html index of many Mars news, facts & images. For the first scrapping, set it up in a jupyter notebook.


NASA Mars News

Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 


JPL Mars Space Images - Featured Image


Visit the url for JPL Featured Space Image  and used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.



Mars Facts


Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts to create an html table.



Mars Hemispheres


Visit the USGS Astrogeology site here to obtain high resolution images for each of Mars's hemispheres.


MongoDB and Flask Application
Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.


Converted Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

Create an index route / that will query your Mongo database and pass the Mars data into an HTML template to be displayed.


Create a template HTML file called index.html that will take the dictionary of Mars data and display its values in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

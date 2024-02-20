import os

from FileUtils_class import FileUtils
from WebScraper_class import WebScraper

# Create an instance of the FileUtils class
fileUtils = FileUtils()

# Check if the directory exists
if not os.path.exists("data_playwright_niels"):
    # If not, create it
    os.makedirs("data_playwright_niels")

# Load the data from the file
data = FileUtils.read_json_file(r"data_playwright_niels\scrapy_output.json")

# Create a list of the urls that is 100 long
urls = [d["href"] for d in data[:10]]

for url in urls:
    # Create an instance of the WebScraper class with a URL
    scraper = WebScraper(url)
    scraper.scrape()
    street_name = scraper.street_name
    print(street_name)

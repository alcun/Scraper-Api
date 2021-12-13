from requests_html import HTMLSession



# Here we create the class, method and use session obkect to scrape data #

class Scraper():
  def scrapedata(self, tag):
    url = f'https://quotes.toscrape.com/tag/life/'
    s = HTMLSession()
    r = s.get(url)
    print(r.status_code)


quotes = Scraper()

quotes .scrapedata('life')

#At the point the program returns '200' which means it's working #

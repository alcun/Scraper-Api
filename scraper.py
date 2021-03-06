from requests_html import HTMLSession



# Here we create the class, method and use session obkect to scrape data #

class Scraper():

  def scrapedata(self, tag):
    url = f'https://quotes.toscrape.com/tag/life/'
    s = HTMLSession()
    r = s.get(url)
    print(r.status_code)
    qlist = []
    quotes = r.html.find('div.quote')

#Created dictionary
#Author found in 'small' tag

    for q in quotes:
        item = {
            'text': q.find('span.text', first=True).text.strip(),
            'Author': q.find('small.author', first=True).text.strip()
            }
        print(item)
        qlist.append(item)

    return qlist

#qlist is now stored as a variable 

quotes = Scraper()

quotes.scrapedata('life')


# Here is an example of a quote via HTML inspect, we will be using it to point the scraper in the right place


'''
<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
        <span class="text" itemprop="text">“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”</span>
        <span>by <small class="author" itemprop="author">Albert Einstein</small>
        <a href="/author/Albert-Einstein">(about)</a>
        </span>
        <div class="tags">
            Tags:
            <meta class="keywords" itemprop="keywords" content="inspirational,life,live,miracle,miracles">

            <a class="tag" href="/tag/inspirational/page/1/">inspirational</a>

            <a class="tag" href="/tag/life/page/1/">life</a>

            <a class="tag" href="/tag/live/page/1/">live</a>

            <a class="tag" href="/tag/miracle/page/1/">miracle</a>

            <a class="tag" href="/tag/miracles/page/1/">miracles</a>

        </div>
    </div>
'''

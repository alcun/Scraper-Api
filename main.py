from fastapi import fastAPI
from Api-Scraper import Scraper

app = FastAPI()
quotes = Scraper()


root = @app.get('/{cat}')
async def read_tem(cat):
    return quotes.scrapedata('cat')

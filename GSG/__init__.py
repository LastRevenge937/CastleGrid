from .gsg_core import GlobalShadowGrid
from gsg.news_feed import NewsFeed
self.news = NewsFeed()

def add_news(self, message: str):
    self.news.post(message)

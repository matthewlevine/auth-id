from google.appengine.api import urlfetch
from libraries.BeautifulSoup import BeautifulSoup

class Page:
  
  url = ''
  html = ''
  soup = None
  hcards = []
  me_links = []
  
  def __init__(self, url):
    self.url = url
    self.html = urlfetch.fetch(url).content
    self.soup = BeautifulSoup(self.html)

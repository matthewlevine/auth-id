from google.appengine.api import urlfetch
from google.appengine.api import urlfetch_errors
from libraries.BeautifulSoup import BeautifulSoup

import logging
import urlparse

class Page:
  
  url = ''
  html = ''
  soup = None
  hcards = []
  me_links = []
  
  def __init__(self, url):
    self.url = url
    
    try:
      self.html = urlfetch.fetch(url).content
    except urlfetch_errors.InvalidURLError:
      return
      
    self.soup = BeautifulSoup(self.html)
    self.populate_me_links()

  def populate_me_links(self):
    self.me_links = [urlparse.urljoin(self.url, tag['href']) for tag in self.soup.findAll(attrs={'rel': 'me'}) if tag.get('href')]
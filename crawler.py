from google.appengine.api import urlfetch

import logging
import page

SIMILARITY_THRESHOLD = .9

class Crawler(object):
  
  url_visited = []
  url_queue = []
  start_url = None
  
  def crawl(self, start_url, max_pages=10):
    self.url_queue.append(start_url)
    
    while self.url_queue and len(self.url_visited) < max_pages:
      p = page.Page(self.url_queue.pop(0))
      self.url_visited.append(p.url)
      
      logging.debug("Visiting url: %s\n" % p.url)
      
      for new_url in p.me_links:
        if new_url not in self.url_visited and new_url not in self.url_queue:
          self.url_queue.append(new_url)

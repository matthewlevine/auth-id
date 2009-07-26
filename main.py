from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch
import page

class HomeController(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Home page')
  
class APIController(webapp.RequestHandler):
  def get(self, url):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(url)
    p = page.Page('http://' + url)
    self.response.out.write([tag['href'] for tag in p.soup.findAll(attrs={'rel': 'me'})])

application = webapp.WSGIApplication([
    ('/', HomeController),
    ('/(.+)', APIController)], debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
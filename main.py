import webapp2
from views.front_page import FrontPage
from views.login_page import LoginPage
from views.protected_page import ProtectedPage

app = webapp2.WSGIApplication([
  ('/login', LoginPage),
  ('/protected', ProtectedPage),
  ('.*', FrontPage),
  ],debug=False)

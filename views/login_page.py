from google.appengine.api import users
from view_handler import ViewHandler

class LoginPage(ViewHandler):
  '''
  view class for the login page
  '''
  def get(self):
    '''
    render the login page template
    '''
    self.render('login.html', users = users)
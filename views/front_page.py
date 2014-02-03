from view_handler import ViewHandler

class FrontPage(ViewHandler):
  '''
  view class for the front page of the app
  '''
  def get(self):
    '''
    render the front page template
    '''
    self.render('front.html')
from view_handler import ViewHandler

class ProtectedPage(ViewHandler):
  '''
  view class for the protected page, only authenticated users should recieved a 200 response
  from the get request below
  '''
  def get(self):
    '''
    render the protected page template if the user is logged in
    '''
    self.user_required()
    self.render('protected.html')
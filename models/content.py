from google.appengine.ext import ndb

class Content(ndb.Model):
  '''
  this is an example model class
  '''
  title = ndb.StringProperty()
  count = ndb.IntegerProperty()
  body = ndb.TextProperty()



import unittest
import webtest

from google.appengine.ext import ndb
from google.appengine.ext import testbed

import main
from models.content import Content

class TestHandler(unittest.TestCase):
  '''
  a useful class that other tests can inherit
  '''

  def setUp(self):
    self.testbed = testbed.Testbed()
    self.testbed.activate()
    self.testbed.init_datastore_v3_stub()
    self.testbed.init_user_stub()
    self.testbed.init_datastore_v3_stub()  
    self.testapp = webtest.TestApp(main.app)
    self.Content = Content

  def tearDown(self):
    self.testbed.deactivate()

  def createUser(self, email_address, admin=False):
    self.testbed.setup_env(
      USER_EMAIL = email_address,
      USER_ID = '123',
      USER_IS_ADMIN = '1' if admin else '0',
      overwrite = True
    )


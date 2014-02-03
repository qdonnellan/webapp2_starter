from testHandler import TestHandler

class ProtectedPageTest(TestHandler):
  '''
  test the implementaiton of a protected page
  '''

  def test_authorized_get_request(self):
    '''
    any user logged into the their google app should make it to the protected page
    '''
    self.createUser('test@example.com')
    response = self.testapp.get('/protected')
    self.assertEqual(response.status_int, 200)

  def test_unauthorized_get_request(self):
    '''
    any user not logged into the their google account should recieve a 401 error
    '''
    response = self.testapp.get('/protected', status = 401)
    self.assertEqual(response.status_int, 401)
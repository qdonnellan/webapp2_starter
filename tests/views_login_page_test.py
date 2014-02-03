from testHandler import TestHandler 

class LoginPageTest(TestHandler):
  '''
  test the login page
  '''

  def test_front_page_response(self):
    '''
    test that the login page is up and running
    '''
    response = self.testapp.get('/')
    self.assertEqual(response.status_int, 200)
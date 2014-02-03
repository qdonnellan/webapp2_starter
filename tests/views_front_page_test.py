from testHandler import TestHandler 

class FrontPageTest(TestHandler):
  '''
  test the public front page
  '''

  def test_front_page_response(self):
    '''
    test that the public front page is working
    '''
    response = self.testapp.get('/')
    self.assertEqual(response.status_int, 200)
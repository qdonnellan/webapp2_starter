from testHandler import TestHandler 

class TestContentModel(TestHandler):
  '''
  test the implementation of the modify functions
  '''

  def test_that_put_method_on_test_model_is_working(self):
    '''
    test that a put() method call is working correctly on the test Model
    '''
    m = self.Content()
    m.title = 'Foo'
    m.body = 'bar bar bar'
    m.count = 1
    self.assertEqual(self.Content.query().count(), 0)
    key = m.put()
    self.assertEqual(self.Content.query().count(), 1)
    m.key.delete()
    self.assertEqual(self.Content.query().count(), 0)


    


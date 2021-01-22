from app import app
from unittest import TestCase

class colorViews(TestCase):
  
  def test_color_form(self):
    with app.test_client() as client:
      import pdb
      pdb.set_trace()
      res = client.get('/')
      html = res.get_data(as_text=True)
      self.assertEqual(res.status_code, 200)
      self.assertIn('<h1>Color form</h1>', html)



  def test_color_submit(self):
    #test client going
    # make a post request to hit the route we've defined
    #check the response data==True
    with app.test_client() as client:
      res = client.post('/favcolor', data={'color': 'red'})
      html = res.get_data(as_text=True)
      
      self.assertEqual(res.status_code, 200)
      self.assertIn('<h2> Really?? red is a beautiful color! And I like it too! </h2>', html)



  def test_redirectme(self):
    with app.test_client() as client:
      res = client.get('/redirectme')

      self.assertEqual(res.status_code, 302)
      self.assertEqual(res.location, 'http://localhost/')
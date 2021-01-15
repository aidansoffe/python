from app import app
from unittest import TestCase

class colorViews(TestCase):
  def test_color_form(self):
    with app.test_client() as client:
      import pdb
      pdb.set_trace()
      result = client.get("/")
      html = result.get.data(as_text=True)
      self.assertEqual(result.status_code, 400)
      self.assertIn('<h1>Color form</h1>', html)
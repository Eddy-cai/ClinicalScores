import unittest
import os
from flask import json

from app import app




class BasicTestCase(unittest.TestCase):

    def test_index(self):
        """initial test. ensure flask was set up correctly"""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_404(self):
        """initial test. ensure that the 404 error exists"""
        tester = app.test_client(self)
        response = tester.get('/no_existant_page', content_type='html/text')
        self.assertEqual(response.status_code, 404)
        #self.assertIn( 'Not Found', response.)



if __name__ == '__main__':
    unittest.main()
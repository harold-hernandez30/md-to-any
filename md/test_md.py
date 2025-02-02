import unittest

from md import MD
from md import Heading

class MDTest(unittest.TestCase):
    def test_single_heading_no_content(self):
        test = """
### this is a title
"""
        md_result =  MD(test)
        
        self.assertEqual(1, len(md_result.headings))
    
        
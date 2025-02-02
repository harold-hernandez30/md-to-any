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

    def test_single_heading_with_single_line_content(self):
        test = """
### this is a title
This is the content
"""
        
        md_result =  MD(test)
        
        self.assertEqual(1, len(md_result.headings))
        self.assertEqual("This is the content", md_result.content_lines[0])

    def test_single_heading_multi_line_content(self):
        test = """
### this is a title
This is the content
Another content
"""
        
        md_result =  MD(test)
        
        self.assertEqual(1, len(md_result.headings))
        self.assertEqual("This is the content", md_result.content_lines[0])
        self.assertEqual("Another content", md_result.content_lines[1])
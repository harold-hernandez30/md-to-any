import unittest
from md import Heading

class TestHeading(unittest.TestCase):
    def test_base_case(self):
        heading = Heading("This is the title", "###")
        self.assertEqual("This is the title", heading.text)
        self.assertEqual("###", heading.level)
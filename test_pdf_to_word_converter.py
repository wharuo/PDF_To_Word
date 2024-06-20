import unittest
from unittest.mock import patch, MagicMock
import sys

# Import the functions you want to test
from pdf_to_word_converter import convert_pdf_to_word_cli

# Mock the Converter class from pdf2docx
class MockConverter:
    def __init__(self, pdf_file):
        self.pdf_file = pdf_file
    
    def convert(self, word_file, start, end):
        print(f"Mock converting {self.pdf_file} to {word_file}")
    
    def close(self):
        print("MockConverter closed")

class TestPDFToWordConverter(unittest.TestCase):

    @patch('pdf_to_word_converter.Converter', new=MockConverter)
    def test_convert_pdf_to_word_cli(self):
        test_pdf_file = "test.pdf"
        test_word_file = "test.docx"
        
        with patch('sys.stdout', new_callable=MagicMock()) as mock_stdout:
            convert_pdf_to_word_cli(test_pdf_file, test_word_file)
            output = mock_stdout.getvalue()
            self.assertIn("MockConverter initialized with test.pdf", output)
            self.assertIn("Mock converting test.pdf to test.docx", output)
            self.assertIn("MockConverter closed", output)
            self.assertIn("Conversion complete: test.docx", output)

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk

# Assuming convert_pdf_to_word_gui, select_pdf_file, select_word_file are part of the same module

class TestPDFToWordConverterGUI(unittest.TestCase):

    @patch('pdf_to_word_converter.Converter', new=MockConverter)
    def test_convert_pdf_to_word_gui(self):
        root = tk.Tk()
        pdf_entry = tk.Entry(root)
        word_entry = tk.Entry(root)
        
        pdf_entry.insert(0, "test.pdf")
        word_entry.insert(0, "test.docx")
        
        with patch('tkinter.messagebox.showinfo') as mock_showinfo, \
             patch('tkinter.messagebox.showerror') as mock_showerror:
            
            convert_pdf_to_word_gui()
            mock_showinfo.assert_called_once_with("Success", "Conversion complete: test.docx")
            mock_showerror.assert_not_called()

if __name__ == '__main__':
    unittest.main()

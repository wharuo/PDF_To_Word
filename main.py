from pdf2docx import Converter
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_pdf_to_word_cli(pdf_file, word_file):
    try:
        # Initialize the converter
        cv = Converter(pdf_file)
        
        # Convert PDF to Word
        cv.convert(word_file, start=0, end=None)
        
        # Close the converter
        cv.close()
        print(f"Conversion complete: {word_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_entry.delete(0, tk.END)
        pdf_entry.insert(0, file_path)

def select_word_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word files", "*.docx")])
    if file_path:
        word_entry.delete(0, tk.END)
        word_entry.insert(0, file_path)

def convert_pdf_to_word_gui():
    pdf_file = pdf_entry.get()
    word_file = word_entry.get()
    if not pdf_file or not word_file:
        messagebox.showerror("Error", "Please select both PDF and Word file paths")
        return

    try:
        cv = Converter(pdf_file)
        cv.convert(word_file, start=0, end=None)
        cv.close()
        messagebox.showinfo("Success", f"Conversion complete: {word_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    if len(sys.argv) == 3:
        pdf_file = sys.argv[1]
        word_file = sys.argv[2]
        convert_pdf_to_word_cli(pdf_file, word_file)
    else:
        # Create the main window
        root = tk.Tk()
        root.title("PDF to Word Converter")

        # Create and place the widgets
        tk.Label(root, text="PDF File:").grid(row=0, column=0, padx=10, pady=10)
        pdf_entry = tk.Entry(root, width=50)
        pdf_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Button(root, text="Browse", command=select_pdf_file).grid(row=0, column=2, padx=10, pady=10)

        tk.Label(root, text="Word File:").grid(row=1, column=0, padx=10, pady=10)
        word_entry = tk.Entry(root, width=50)
        word_entry.grid(row=1, column=1, padx=10, pady=10)
        tk.Button(root, text="Browse", command=select_word_file).grid(row=1, column=2, padx=10, pady=10)

        tk.Button(root, text="Convert", command=convert_pdf_to_word_gui).grid(row=2, column=0, columnspan=3, pady=20)

        # Start the GUI event loop
        root.mainloop()

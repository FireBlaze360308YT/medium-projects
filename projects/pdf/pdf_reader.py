import re
from collections import Counter
from PyPDF2 import PdfReader
import customtkinter as ctk
from tkinter import filedialog


class PdfReaderClass:
    def __init__(self):
        # Window Object
        print("Window creation...")
        self.window = ctk.CTk()
        self.window.title("Pdf Reader")
        self.window.geometry("280x60")
        self.window.resizable(False, False)
        print("Window created!")

        # Padding setup
        print("Window initialization...")
        self.padding: dict = {"padx": 20, "pady": 10}
        print("Window initialized!")

        ############################

        # Pdf file label
        self.pdf_file_path_label = ctk.CTkLabel(self.window, text="File Path: ")
        self.pdf_file_path_label.grid(row=0, column=0, **self.padding)

        # Pdf file button
        self.pdf_file_button = ctk.CTkButton(self.window, text="Select file", command=self.select_file)
        self.pdf_file_button.grid(row=0, column=1, **self.padding)

        # Initialize the file path variable (instance variable)
        self.pdf_file_path_str: str = ""

    def run(self):
        self.window.mainloop()

    def select_file(self):
        folder_path = filedialog.askopenfilename(title="Select a pdf", filetypes=[("PDF files", "*.pdf")])

        if folder_path:
            self.pdf_file_path_str = folder_path.rsplit("/")[-1]  # Get just the file name, not the full path

            # Display the file name on the window
            if hasattr(self, 'pdf_path_label'):  # Check if the label already exists
                self.pdf_path_label.configure(text=self.pdf_file_path_str)  # Update existing label
            else:
                self.pdf_path_label = ctk.CTkLabel(self.window, text=self.pdf_file_path_str)
                self.pdf_path_label.grid(row=0, column=2, **self.padding)

            # Update window size after the file is selected
            self.window.geometry("390x110")

            # Change button text and disable it
            self.pdf_file_button.configure(text="File selected", command=None)

            # Add Submit button to proceed with PDF text extraction
            self.submit_button = ctk.CTkButton(self.window, text="Submit", command=self.main)
            self.submit_button.grid(row=1, column=1, **self.padding)

        else:
            print("Pdf not selected")
            self.window.destroy()  # Close the window if no file is selected

    def extract_text_from_pdf(self, pdf_file: str) -> list[str]:
        """Extract text from the given PDF file."""
        with open(pdf_file, "rb") as pdf:
            reader = PdfReader(pdf, strict=False)
            print("Pages:", len(reader.pages))
            print("-" * 10)  # Divider

            pdf_text: list[str] = [page.extract_text() for page in reader.pages]
            return pdf_text

    def count_words(self, text_list: list[str]) -> tuple[Counter, int, ...]:
        """Count words and characters in the given text."""
        all_words: list[str] = []
        num_of_chars: int = 0
        for text in text_list:
            split_text: list[str] = re.split(r"\s+|[,;?!.-]\s*", text.lower())
            all_words += [i for i in split_text if i]  # Only add non-empty strings

        for item in all_words:
            num_of_chars += len(item)  # Count total characters in all words

        return Counter(all_words), len(all_words), num_of_chars

    def main(self):
        self.window.destroy()
        """Process the PDF file and count words."""
        if not self.pdf_file_path_str:
            print("No PDF file selected!")
            return

        extracted_text: list[str] = self.extract_text_from_pdf(self.pdf_file_path_str)
        counter, num_words, num_chars = self.count_words(text_list=extracted_text)

        for page in extracted_text:
            print(page)  # Display extracted text for each page

        print("-" * 10)
        for word, mention in counter.most_common(5):
            print(f"{word:10}: {mention} times")
        print(f"Number of words: {num_words}\nNumber of chars: {num_chars}")


if __name__ == '__main__':
    pdf_reader = PdfReaderClass()
    pdf_reader.run()

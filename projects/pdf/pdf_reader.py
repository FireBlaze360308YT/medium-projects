import re
from collections import Counter
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_file: str) -> list[str]:
    with open(pdf_file, "rb") as pdf:
        reader = PdfReader(pdf, strict=False)

        print("Pages:", len(reader.pages))
        print("-" * 10)  # Divider

        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        return pdf_text


def count_words(text_list: list[str]) -> tuple[Counter, int, ...]:
    all_words: list[str] = list()
    num_of_chars: int = int()
    for text in text_list:
        split_text: list[str] = re.split(r"\s+|[,;?!.-]\s*", text.lower())
        all_words += [word for word in split_text if word]

    for item in all_words:
        for char in item:
            num_of_chars += 1

    return Counter(all_words), len(all_words), num_of_chars


def main():
    extracted_text: list[str] = extract_text_from_pdf("sample.pdf")
    counter, num_words, num_chars = count_words(text_list=extracted_text)

    for page in extracted_text:
        print(page)

    for word, mention in counter.most_common(5):
        print(f"{word:10}: {mention} times")
    print(f"Number of words: {num_words}\nNumber of chars: {num_chars}")


if __name__ == '__main__':
    main()

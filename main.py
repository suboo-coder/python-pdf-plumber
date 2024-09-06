import pdfplumber

# Open the PDF file
with pdfplumber.open("background-checks.pdf") as pdf:
    first_page = pdf.pages[0]
    print(first_page.extract_text())
    print(first_page.chars[1])
    # print(first_page.extract_tables())

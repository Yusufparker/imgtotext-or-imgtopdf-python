
import pytesseract 


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
PATH = 'projek/img to teks/jokowi.png' 


pdf = pytesseract.image_to_pdf_or_hocr(PATH, extension='pdf')
with open('projek/img to teks/test.pdf', 'w+b') as f:
    f.write(pdf) # pdf type is bytes by default

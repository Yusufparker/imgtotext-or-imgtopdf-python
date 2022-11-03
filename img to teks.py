import pytesseract 
from googletrans import Translator
import pywhatkit
import os
import time
from datetime import datetime
os.system('cls')

date = datetime.now().strftime('%d/%m/%y')

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def get_text(line):
    output = [date]
    print('Please enter the text :')
    for i in range(line):
        text = str(input())
        output.append(text)
    output = '\n'.join(output)
    return output

def get_fileName():
    fileName = str(input('input the file name: '))
    return fileName

def get_image():
    file = os.listdir('projek/img to teks/input')
    imageName = str(input('input the image name: '))
    eks = str(input('input file extension (png/jpg/jpeg) : '))
    while eks not in ['png','jpg','jpeg']:
        eks = str(input('input file extension (png/jpg/jpeg) : '))
    fileName = imageName+'.'+eks
    while fileName not in file:
        print('file not availabel..\n')
        imageName = str(input('input the image name: '))
        eks = str(input('input file extension (png/jpg/jpeg) : '))
        while eks not in ['png','jpg','jpeg']:
            eks = str(input('input file extension (png/jpg/jpeg) : '))
        fileName = imageName+'.'+eks       

    return fileName

def translate(teks, lang):
    return str(Translator().translate(teks, lang).text)


while True:
    print('Welcome....')
    select = str(input('''Main Menu :
1. Text to handwriting image
2. Image to text
3. Image to pdf
4. translate text
5. close
=> '''))

    if select == '1':
        try:
            line = int(input('Enter the number of rows you want : '))    
            output = get_text(line)
            fileName = get_fileName()
            pywhatkit.text_to_handwriting(output,f'projek/img to teks/output/{fileName}.png')
            print('\nwait please...')
            print('saving the file...')
            time.sleep(0.5)
            print('\nfile saved successfully....\n')
        except ValueError:
            print('Value Error..\n')
            pass

    elif select == '2':
        teks = get_image()
        print('wait please...')
        time.sleep(1)
        print('--------------output---------------')
        print(pytesseract.image_to_string(f'projek/img to teks/input/{teks}'))
        print('-----------------------------------\n')


    elif select == '3':
        image = get_image()
        pdf = pytesseract.image_to_pdf_or_hocr(f'projek/img to teks/input/{image}', extension='pdf')
        print('wait please...')
        time.sleep(1.2)
        fileName = str(input('input the file name: '))
        print('saving file....')
        time.sleep(1.3)
        with open(f'projek/img to teks/output/{fileName}.pdf', 'w+b') as f:
            f.write(pdf)
        print('file saved successfully....\n')

    elif select =='4':
        text = str(input('Enter the text : \n'))
        lang = str(input('language (id/en): '))
        while lang not in ['id','en']:
            lang = str(input('language (id/en): '))     
        translated = translate(text, lang)
        print('Translating....')
        time.sleep(1.5)
        print('\nTranslate-------------')
        print(translated)
        print('\n--------------------------')


    elif select == '5':
        print('Thank You...😊')
        break

    else:
        print('not available!\n')
        





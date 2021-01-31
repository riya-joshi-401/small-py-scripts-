import filetype
import docx2pdf
from docx2pdf import convert

kind = filetype.guess('testing_conversion_to_pdf.docx')

if kind==None:
    print(":(")
elif kind.extension=='pdf' or kind.extension=='doc':
    print('yay')
    if kind.extension=='doc':
        convert("testing_conversion_to_pdf.docx", "output.pdf")
        convert("temp/")
    
    
#print('File extension: %s' % kind.extension)
#print('File MIME type: %s' % kind.mime)

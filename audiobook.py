import pyttsx3  # text-to-speech conversion library
import PyPDF2  # library built as a PDF toolkit
book = open('name_of_the_document.pdf', 'rb') # opening a fle  for reading in binary mode
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages # total no of pages

speaker = pyttsx3.init() # initializing 
for num in range(pages): # looping through all the pages of the document file / book
    page = pdfReader.getPage(num) 
    text = page.extractText()
    speaker.say(text) # speaks 
    speaker.runAndWait()

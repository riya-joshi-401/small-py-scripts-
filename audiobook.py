import pyttsx3 # text-to-speech conversion library
import PyPDF2  # library built as a PDF toolkit

book = open('the exorcist.pdf', 'rb') # opening a fle  for reading in binary mode

pdfReader = PyPDF2.PdfFileReader(book)

pages = pdfReader.numPages # total no of pages

speaker = pyttsx3.init()  # initializing / creating an object

voices = speaker.getProperty('voices')       #getting details of current voice
#speaker.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

rate = speaker.getProperty('rate')   # getting details of current speaking rate
print(rate)                        #printing current voice rate
speaker.setProperty('rate', 125)     # setting up new voice rate


for num in range(4,5): # looping through all the pages of the document file / book
    
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.save_to_file(text, 'test.mp3')
    speaker.runAndWait()

speaker.stop()
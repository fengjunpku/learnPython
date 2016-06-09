from urllib import urlopen
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from io import open

def readPDF(pdfFile):
  rsrcmgr = PDFResourceManager()
  retstr = StringIO()
  laparams = LAParams()
  device = TextConverter(rsrcmgr, retstr, laparams=laparams)
  interpreter = PDFPageInterpreter(rsrcmgr, device)
  password = ""
  maxpages = 0
  caching = True
  pagenos=set()
  for page in PDFPage.get_pages(pdfFile, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
  device.close()
  content = retstr.getvalue()
  retstr.close()
  return content

pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf");
#outputString = readPDF(pdfFile)
print(pdfFile)
pdfFile.close()
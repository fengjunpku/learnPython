from urllib2 import Request
from urllib2 import urlopen
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

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

#pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf");
#outputString = readPDF(pdfFile)
# print(pdfFile)
# pdfFile.close()

if __name__ == "__main__":
  url = 'http://pythonscraping.com/pages/warandpeace/chapter1.pdf'
  open = urlopen(Request(url)).read()
  memoryFile = StringIO(open)
  #print memoryFile
  rsrcmgr = PDFResourceManager()
  retstr = StringIO()
  codec = 'utf-8'
  laparams = LAParams()
  device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
  fp = file('chapter1.pdf', 'rb')
  print fp
  interpreter = PDFPageInterpreter(rsrcmgr, device)
  password = ""
  maxpages = 0
  caching = True
  pagenos=set()
  for page in PDFPage.get_pages(memoryFile, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
    interpreter.process_page(page)
  fp.close()
  device.close()
  str = retstr.getvalue()
  retstr.close()
  print str
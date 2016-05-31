#coding:utf8
import urllib2

class CD_Conn(object):
    def __init__(self):
        self._url=None
        self._response=None
        
    def visit(self,url):
        if url is None:
            print "Please give a url!"
            return None
        ######
        self._url=url
        ############
        request = urllib2.Request(self._url)
        request.add_header("user-agent", "Mozilla/5.0")
        self._response = urllib2.urlopen(request)
        return self._response.getcode()
    
    def getpage(self):       
        #
        if self._url is None:
            print "Please call visit() first!"
            return None
        #
        webcode = self._response.info().getparam('charset')
        rawdata = self._response.read()
        self._response.close()
        #print webcode
        if webcode == "GBK":
            return rawdata.decode("gbk").encode("utf-8")
        elif webcode == "None":
            return rawdata
        else:
            return rawdata
    
    





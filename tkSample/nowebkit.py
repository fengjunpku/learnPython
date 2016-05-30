import urllib
address = 'http://miaomiaoxiong.net/md/#OpenMP_note'
data =  urllib.urlopen(address)
print data.read()
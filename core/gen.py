#-*- coding: utf-8 -*-

import requests, re, socket, sys
try:
   cek = requests.session()
   count = 0
   page = cek.get("https://free-proxy-list.net").text
   proxy = re.findall(r"\d+\.\d+\.\d+\.\d+",page)
   port = re.findall(r"\**<td>\d+</td>", page)
   country = re.findall(r'td>(\w{2})</', page)
except requests.exceptions.ConnectionError:
   print color.red__+symbol.C+' No Internet Connection '+symbol.C+color.WHITE
   sys.exit()

class color:
      red__ = '\033[91m'
      green__ = '\033[92m'
      yellow__ = '\033[93m'
      blue__ = '\033[94m'
      WHITE = '\033[0m'
class symbol:
      A = '[!]'
      B = '[+]'
      C = '[x]'
      D = '[*]'


class G_Tools:

      def __init__(self, proxy, port, host, method):
          self.proxy = proxy
          self.port = port
          self.host = host
          self.method = method
          proxies = self.proxy+':'+str(port)
          sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          sock.settimeout(int(5))
          try:
             sock.connect((self.proxy,self.port))
             print '[Method]  : '+color.green__+self.method+color.WHITE
             print '[Proxy]   : '+color.blue__+self.proxy+':'+color.WHITE+str((port))
             data  = "{} {} HTTP/1.0\r\nConnection: keep-alive\r\n\r\n".format(self.method,self.host)
             sock.sendall(data)
             abc = sock.recv(9000).split("\r\n")[0]
             if abc in ['HTTP/1.0 200 OK','HTTP/1.1 200 OK', 'HTTP/1.1 200 Connection established', 'HTTP/1.0 200 Connection established' ]:
                print "[Host]    : "+color.red__+self.host+color.WHITE
                print "[Status]  : "+color.green__+abc+color.WHITE
                print "[Save-To] : "+color.yellow__+'results.txt'+color.WHITE
                save = open('results.txt', "a+")
                save.write("%s:%s\n" % (self.proxy,str(self.port)))
                save.close()
             else:
                print '[Status]  : '+color.yellow__+abc+color.WHITE
          except socket.timeout:
              print color.red__+symbol.A+" Connection Time Out "+symbol.A+color.WHITE
          except socket.error:
              print color.red__+symbol.A+' Proxy  Error '+symbol.A+color.WHITE
          except IOError:
              print color.red__+symbol.C+" Invalid Proxy "+symbol.C+color.WHITE
          except KeyboardInterrupt:
              print 'Exit'
              sys.exit()
          sock.close()





def single_proxy(url):
    ress = requests.get(url).json()
    for i in list(ress):
        print color.blue__+symbol.B+color.WHITE,' - ',i+' : '+color.green__,ress[i]
        print color.WHITE



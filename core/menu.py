#-*- coding: utf-8 -*-
from gen import color
import sys, time

codename = 'JaxBCD'
contact = 'fb.me/jaka.lesmana.794628'
TM = '407 Authentic Exploit'
version = '2.7 unv'

logo = '''%s
       0000000         8888888888           00
      00                  00               00
     00                  00               00
    00   0000   000     00 00000  00000  00
   00      00   000    00 00  00 00  00 00
  00      00          00 00  00 00  00 00
  000000000          00 000000 000000 000000000%s
                                        [v]ersion : %s%s%s
                                        %s
  Codename : %s
  Contact  : %s
''' % (color.blue__,color.WHITE,color.yellow__,version,color.WHITE,TM,codename,contact)



help = '''
               [ Command ]     [ Descriptions ]
                 help            show command and description
                 use <module>    use <modules>
                 show modules    show all module available
                 show options    show options in modules
                 set <command>   use <set> after use modules
                 run             use <run> after use modules and set options
                 exit or quit    for logout from This Tool
'''
show_modules = color.green__+'''

Modules                               Description
-------                               ------------

G_Tool/mass_proxy_hunter              Generate Proxy from www.proxylist.net
                                      And check all proxy

G_Tool/random_generate_proxy_hunter   Random generate Proxy from proxylist.com

G_Tool/dnsdumpster                    Search Host from Domain
'''+color.WHITE
options_1 = '''

Command    required   description
------     --------   -----------
METHOD     yes        set check method POST,GET,CONNECT,TRACE
                      HEAD,PUT,OPTIONS,MOVE recomendation:CONNECT

HOST       yes        Direct To HOST for check Proxy

'''
options_2 = '''

Command    required   description
------     --------   -----------
  -          -        exec <run> only
'''
options_3 = '''

Command    required   description
------     --------   -----------
DOMAIN     yes        set DOMAIN e.g example.com

'''
# <Loading> Coded By @Ciku370
# Github : https://github.com/ciku370
def loading(text):
    num = 0
    while num < 1:
        for i,char in enumerate(text):
            if i == 0:
                print "\r%s%s" %(char.upper(),text[1:]),
                sys.stdout.flush()
            elif i == 1:
                old_text = text[0].lower()
                print "\r%s%s%s" %(old_text,char.upper(),text[2:]),
                sys.stdout.flush()
            elif i == i:
                old_text = text[-0:i].lower()
                print "\r%s%s%s" %(old_text,char.upper(),text[i+1:]),
                sys.stdout.flush()
            time.sleep(0.1)
        num += 1

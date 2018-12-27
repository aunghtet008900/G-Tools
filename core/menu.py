#-*- coding: utf-8 -*-
from gen import color
import sys, time

codename = 'JaxBCD'
version = '3.2 unv'
logo = '''%s        
       ++++++       +++++++          ++
      ++             ++             ++ 
     ++ +++   +++   ++ ++++  ++++  ++ 
    ++   ++        ++ ++ ++ ++ ++ ++
    +++++++       ++ +++++ +++++ +++++++%s
                            [v]ersion  : %s%s%s
                            [c]odename :%s%s%s
''' % (color.blue__,color.WHITE,color.green__,version,color.WHITE,color.yellow__,codename,color.WHITE)


menu = '''
      {1} Hunter Proxy
      {2} Search Host
      {3} Generate Proxy
      {0} Exit
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

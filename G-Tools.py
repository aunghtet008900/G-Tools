#!/bin/python2.7
#Codename : JaxBCD
import os
import sys
from time import sleep as turu
sys.path.insert(0,'/data/data/com.termux/files/home/G-Tools/dat')
from bannermenu import *
from _proxy_ import *
from _Host_H_ import *
os.system('clear')
turu(2)

def quit():
    con = raw_input('Lanjutkan? (Y/n)~> ')
    if con[0].upper() == 'N':
        exit()
    else:
        logo()
        pilih()

def pilih():
    bersih = os.system('clear')
    logo()
    Menu0()
    A = input('Pilih : ')
    if A == 1:
       turu(2)
       Menu1()
       A1 = input('Pilih : ')
       if A1 == 1:
          bersih
          list()
          quit()
       elif A1 == 2:
            bersih
            scan_crot()
            quit()
       elif A1 == 3:
            bersih
            fpl_crot()
            quit()
       elif A1 == 4:
            bersih
            daily(kentod)
            quit()
       elif A1 == 0:
            pilih()
       else:
           print 'Masukan Pilihan dengan Benar'

    elif A == 2:
         turu(2)
         Menu2()
         A2 = input('Pilih : ')
         if A2 == 1:
            bersih
            host()
            quit()
         elif A2 == 2:
            bersih
            nmap()
            quit()
         elif A2 == 0:
            pilih()
         else:
             print 'Masukan Pilihan dengan benar'
    elif A == 3:
         turu(2)
         Menu3()
         A3 = input('Pilih : ')
         if A3 == 1:
            bersih
            single()
            quit()
         elif A3 == 2:
              bersih
              singel_socket()
              quit()
         elif A3 == 3:
              bersih
              print '\033[91mMasukan File yang berextensi .txt Contoh :\033[0m Anu.txt'
              tx = raw_input('Masukan file ! : ')
              manual_text(tx)
              quit()
         elif A3 == 0:
              pilih()
         else:
             print 'Masukan Pilihan dengan benar'
    elif A == 4:
         turu(2)
         menu4()
         A4 = input('Pilih : ')
         if A4 == 1:
           bersih()
           single_check_host()
           quit()
         elif A4 == 2:
           bersih
           os.system('python2 $HOME/G-Tools/_mass_cek.pyc')
           quit()
         elif A4 == 0:
           pilih()
         else:
             print 'Masukan Pilihan dengan benar'
    elif A == 5:
         print """
         Author : JaxBCD
         Contact my Facebook : fb.me/jack.lesmen.5
         Special Thanks To : QiubyZukhi , Khoirul amsori , Hard Ghost dan 407 AEx
         facebook : https://www.facebook.com/khoirul.amsori
                    https://www.facebook.com/qiuby.zhukhi
                    https://www.facebook.com/HardGhost.Aore
         udah Tinggal Pake aja """
         quit()
    elif A == 00:
         print '^_^ bye'



def mulai():
   pilih()
   try:
      print""
      print""
   except KeyboardInterrupt:
       print '\033[91mError'
   except ValueError:
       print 'Error'
   except:
        print 'Ulangi\033[0m'

mulai()

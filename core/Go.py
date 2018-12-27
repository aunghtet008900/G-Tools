#-*- coding: utf-8 -*-
import sys, os, menu, dns, gen

proxy = gen.proxy
port = gen.port
method = '''
         CONNECT
         GET
         POST
         PUT
         HEAD
         OPTIONS
         TRACE
         PATCH
         PROPATCH
         DELETE
         MOVE
'''
print menu.logo
print menu.menu
def g_tool():
    while True:
          try:
             G = raw_input(gen.color.blue__+'[G-T]>>>  '+gen.color.WHITE)
             if str(1) in G:
                print ""
                print 'example : '+gen.color.green__+'www.google.com'+gen.color.WHITE
                print ""
                H = raw_input(gen.color.blue__+'[Host]>>>  '+gen.color.WHITE)
                print gen.color.green__+method+gen.color.WHITE
                M = raw_input(gen.color.blue__+'[Method]>>>  '+gen.color.WHITE).upper()
                for i in range(5):
                    menu.loading(gen.color.yellow__+'[*]Starting....'+gen.color.WHITE)
                for i in range(len(proxy)):
                    ports = port[i].replace("<td>", "").replace("</td>","")
                    prx = proxy[i]
                    print '\n'
                    gen.G_Tools(prx, int(ports), H, M)
             elif str(2) in G:
                  print ""
                  print 'example : '+gen.color.green__+'google.com'+gen.color.WHITE
                  print ""
                  dom = raw_input(gen.color.red__+'Domain>>>  '+gen.color.WHITE)
                  for i in range(5):
                      menu.loading(gen.color.yellow__+'[*]Starting....'+gen.color.WHITE)
                  print "\n"
                  dns.dns(dom).dump_()
             elif str(3) in G:
                  for i in range(3):
                      menu.loading(gen.color.yellow__+'[*]Generating....'+gen.color.WHITE)
                  gen.single_proxy('https://api.getproxylist.com/proxy')
             elif str(0) in G:
                  print '\n'
                  print 'EXIT'
                  sys.exit()
             else:
                  print '\n'
                  print gen.color.red__+gen.symbol.A+' No Number Available '+gen.color.WHITE
          except KeyboardInterrupt:
              sys.exit()
          except EOFError:
              sys.exit()



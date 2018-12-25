#-*- coding: utf-8 -*-

import sys, menu, time, gen, dns, requests


domain = ""
method = ""
host = ""
print menu.logo

def opt_2():
    while True:
          P_1 = raw_input('[G_T]'+gen.color.red__+'/G_Tool/mass_proxy_hunter/'+gen.color.WHITE+'>  ').upper()
          try:
              if 'SHOW OPTIONS' in P_1:
                  print menu.options_1
              elif 'SET METHOD' in P_1:
                  method=P_1.split()[2]
                  print 'METHOD ~> ',method
              elif 'BACK' in P_1 or 'EXIT' in P_1:
                  opt_1()
              elif 'SET HOST' in P_1:
                  host=P_1.split()[2]
                  print 'HOST ~> ',host
              elif 'HELP' in P_1:
                  print menu.help
              elif 'RUN' in P_1:
                   for load in range(5):
                       menu.loading(gen.color.green__+'[*]Starting.....'+gen.color.WHITE)
                   print '\n'
                   for i in range(len(gen.proxy)):
                       ports = gen.port[i].replace("<td>", "").replace("</td>", "")
                       print '\n'
                       gen.G_Tools(gen.proxy[i], int(ports), host.upper(), method)
              else:
                   print gen.color.red__+gen.symbol.C+' No Command '+gen.color.WHITE, P_1
          except UnboundLocalError:
              print gen.color.red__+gen.symbol.C+' No options Setted '+gen.color.WHITE
          except IndexError:
              print gen.color.WHITE+gen.symbol.C+' No Options Setted '+gen.color.WHITE
          except EOFError:
              sys.exit()
          except KeyboardInterrupt:
              sys.exit()
def opt_3():
    while True:
          try:
              P_3 = raw_input('[G_T]'+gen.color.red__+'/G_Tools/random_generate_proxy_hunter/'+gen.color.WHITE+'>  ').upper()
              if 'SHOW OPTIONS' in P_3:
                  print menu.options_2
              elif 'HELP' in P_3:
                  print menu.help
              elif 'RUN' in P_3:
                  menu.loading(gen.color.yellow__+gen.symbol.D+' Generating'+gen.color.WHITE)
                  print "\n"
                  gen.single_proxy('https://api.getproxylist.com/proxy')
              elif 'EXIT' in P_3 or 'BACK' in P_3:
                  opt_1()
              else:
                  print gen.color.red__+gen.symbol.C+' No Command '+gen.color.WHITE, P_3
          except EOFError:
              sys.exit()
          except KeyboardInterrupt:
              sys.exit()

def opt_4():
    while True:
          try:
             P_4 = raw_input('[G_T]'+gen.color.red__+'/G_Tool/dnsdumpster/'+gen.color.WHITE+'>  ').upper()
             if 'SET DOMAIN' in P_4:
                 domain=P_4.split()[2]
                 print gen.color.red__+'DOMAIN ~> '+gen.color.WHITE, domain
             elif 'BACK' in P_4 or 'EXIT' in P_4:
                 opt_1()
             elif 'RUN' in P_4:
                 for load in range(5):
                     menu.loading(gen.color.blue__+'[*]Starting.....'+gen.color.WHITE)
                 print "\n"
                 dns.dns(domain).dump_()
             elif 'SHOW OPTIONS' in P_4:
                 print menu.options_3
             elif 'HELP' in P_4:
                 print menu.help
             else:
                 print gen.color.red__+gen.symbol.C+' No Command '+gen.color.WHITE, P_4
          except UnboundLocalError:
             print gen.color.red__+gen.symbol.C+' No options Setted\n'+gen.color.WHITE
          except EOFError:
            sys.exit()
          except KeyboardInterrupt:
            sys.exit()

def opt_1():
    while True:
          try:
              P = raw_input('[G_T]/> ').lower()
              if 'help' in P:
                 print menu.help
              elif 'show modules' in P:
                 print menu.show_modules
              elif 'use g_tool/mass_proxy_hunter' in P:
                 opt_2()
              elif "use g_tool/dnsdumpster" in P:
                  opt_4()
              elif 'exit' in P or 'quit' in P:
                 print 'Exit [!]\n'
                 sys.exit()
              elif 'use g_tool/random_generate_proxy_hunter' in P:
                 opt_3()
              elif 'back' in P:
                 print 'Exit [!]\n'
                 sys.exit()
              elif 'run' in P:
                 print gen.color.red__+gen.symbol.A+' type <run> in modules after set options'+gen.color.WHITE
              else:
                 print ""
                 print gen.color.red__+gen.symbol.C+' No Command '+gen.color.WHITE,P
                 print ""
          except EOFError:
              sys.exit()
          except KeyboardInterrupt:
              sys.exit()





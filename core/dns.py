import requests, re
from bs4 import BeautifulSoup as bs
from gen import color

class dns:

      url__ = 'https://dnsdumpster.com/'
      count = 0

      def __init__(self, domain):
          self.domain = domain


      def dump_(self):
          res = requests.get(dns.url__)
          dat = bs(res.text, 'html.parser').find_all('input')
          tok = re.findall(r'value="(.*?)"', str(dat))[0]
          cookie = {'csrftoken': tok}
          headers = {'Referer': dns.url__}
          data = {'csrfmiddlewaretoken': tok, 'targetip': self.domain}
          resp = requests.post(dns.url__, cookies=cookie, data=data, headers=headers)
          Host = re.findall('http://(.*?)"', str(resp.text))
          for list_host in Host:
              dns.count += 1
              print dns.count,'.'+color.blue__+list_host+color.WHITE









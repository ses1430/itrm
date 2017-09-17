#-*- coding: utf-8 -*-
'''
Created on 2016. 9. 30.

@author: P005271
'''
from bs4 import BeautifulSoup
from urllib import request, parse
import re

url = "http://nharvest.sktelecom.com:9080/sdms/login/login.jsp"
parms = {
        'userName':'OPS02578', 
        'userPasswd':'1q2w3e4r!!'
        }

querystring = parse.urlencode(parms)

req = request.Request(url, querystring.encode('ascii'))
res = request.urlopen(req)

cookie = res.headers.get('Set-Cookie')

url2 = "http://nharvest.sktelecom.com:9080/sdms/delta/deploy_list.jsp"
parms2 = {
          'PROC_TYPE':'',
          'currentPage':'1',
          'countPerPage':'10',
          'deploySeq':'',
          'chgPlanId':'',
          'instance':'5',
          'deployerName':'',
          'module':'',
          'deployStatus':'',
          'startDate':'2016-09-26',
          'endDate':'2016-09-29',
          'buildResult':''
          }

querystring2 = parse.urlencode(parms2)

req2 = request.Request(url2, querystring2.encode('ascii'))
req2.add_header('cookie', cookie)
res2 = request.urlopen(req2)

soup = BeautifulSoup(res2, "lxml")
table = soup.find('table', {'class':'table1'})

for row in [item for item in table.findAll('tr') if item.has_attr('class')]:
    cells = [item.get_text().strip() for item in row.findAll('td')]
    print(cells)
    
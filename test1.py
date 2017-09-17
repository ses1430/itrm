#-*- coding: utf-8 -*-
'''
Created on 2017. 1. 5.

@author: P005271
'''
from urllib import request
from bs4 import BeautifulSoup

url1 = "http://172.31.32.51:8080/araws/loginSvc/Login"
url2 = "http://172.31.32.51:8080/araws/objectSvc/Search/ListNm?dmnCd=SKT&prjCd=UKEY&oprCd=NGMS&objId=ZORDSBB1000&posStart=0&posEnd=49"
url3 = "http://172.31.32.51:8080/araws/objectSvc/Search/ListNm?dmnCd=SKT&prjCd=UKEY&oprCd=NGMS&objId=zordmb010001&posStart=0&posEnd=49"

parms1 = 'userId=arausr&userPwd=skt!0823'
parms2 = ''

req = request.Request(url1, parms1.encode('ascii'))
req.add_header('Content-Type','application/x-www-form-urlencoded')
req.add_header('Content-Length','30')
req.add_header('Expect','100-continue')
req.add_header('Host','172.31.32.51:8080')

res1 = request.urlopen(req)

soup = BeautifulSoup(res1, "lxml")
print(soup)

cookie = res1.headers.get('Set-Cookie')
print('cookie :', cookie)

req2 = request.Request(url2)
req2.add_header('cookie', cookie)
req2.add_header('Connection', 'Keep-Alive')
res2 = request.urlopen(req2)

soup = BeautifulSoup(res2, "lxml")
print(soup)

req2 = request.Request(url3)
req2.add_header('cookie', cookie)
req2.add_header('Connection', 'Keep-Alive')
res2 = request.urlopen(req2)

soup = BeautifulSoup(res2, "lxml")
print(soup)


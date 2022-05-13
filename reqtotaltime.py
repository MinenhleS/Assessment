import requests 
from bs4 import BeautifulSoup 
import datetime
import os

def getsitename(i):
    req = requests.get(url)
    pq = BeautifulSoup(req.text, 'html.parser')
    print(pq.title.text)
    return

if __name__ == '__main__' :
    begin = datetime.datetime.now()
    url = os.environ.get('site')
    iternum = int(os.environ.get('times'))
    counter = 0
    for i in range (0,iternum):
        counter +=1
        getsitename(i)
    finish = datetime.datetime.now() - begin
    print(finish)
    print(counter)


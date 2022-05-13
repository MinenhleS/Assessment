import requests 
from bs4 import BeautifulSoup 
import datetime

def getsitename(i):
    url = 'https://slate.com/technology/2012/10/website-pagination-stories-should-load-into-a-single-page-every-time.html'
    req = requests.get(url)
    pq = BeautifulSoup(req.text, 'html.parser')
    print(pq.title.text)
    return

if __name__ == '__main__' :
    begin = datetime.datetime.now()

    counter = 0
    for i in range (1,10):
        counter +=1
        getsitename(i)
    finish = datetime.datetime.now() - begin
    print(finish)
    print(counter)


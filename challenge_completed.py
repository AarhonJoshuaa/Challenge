import requests
from bs4 import BeautifulSoup
from tamil import utf8
from itertools import count 
import winsound
URL = 'https://venmurasu.in/2014/01/01/%e0%ae%b5%e0%af%86%e0%ae%a3%e0%af%8d%e0%ae%ae%e0%af%81%e0%ae%b0%e0%ae%9a%e0%af%81-%e0%ae%a8%e0%af%82%e0%ae%b2%e0%af%8d-%e0%ae%92%e0%ae%a9%e0%af%8d%e0%ae%b1%e0%af%81/'
final=[]
new=[]
c=1
while True:
    f = open("output.txt", "w",encoding="utf-8")
    fil = open("output/file"+str(c)+".txt", "w",encoding="utf-8")
    fil2 = open("scrap/file"+str(c)+".txt", "w",encoding="utf-8")
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    job_elems = soup.find('div', class_='entry-content')
    try:
        href=soup.find('a',rel="next").attrs
    except:
        print('completed')
        break
    #print(href)
    fil2.write(job_elems.text)
    result=utf8.get_words(job_elems.text)
    for fb in final:
        result.append(fb)
    for a in result:
        a=a.replace('”','')
        a=a.replace('“','')
        a=a.replace('!','',10000000000)
        a=a.replace('.','',10000000000)
        a=a.replace(',','',10000000000) 
        a=a.replace('?','',10000000000)
        a=a.replace('ஏற்றப்படுகின்றது','',10000000000)
        if(utf8.all_tamil(a) ):
            if a not in new:
                new.append(a)
                fil.write(a)
                fil.write('\n')
            #f.write(a)
            #f.write("\n")
            
        else:
            a=''
        
    cnt=count()
    final=sorted(new, key = lambda w : (len(utf8.get_letters(w)), next(cnt)),reverse = True)[:10]
    print(final)
    URL=href['href']
    for fa in final:
        f.write(fa)
        f.write('\t\t')
        f.write(str(len(utf8.get_letters(fa))))
        f.write('\n')
    fil2.write('\n')
    fil2.write(href['href'])
    f.write('\n')
    c=c+1
f.close()
winsound.Beep(2000, 1000)
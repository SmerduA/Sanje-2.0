import urllib.parse
import urllib.request
import http.cookiejar
import re


cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent:', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')]
urllib.request.install_opener(opener)
url = 'http://www.plezanje.net/climbing/db/countryIntro.asp?otype=C'
values = {}


data  = urllib.parse.urlencode(values)
data = data.encode('utf-8')

req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
the_page = response.read().decode('utf-8')



with open('tujina.html', 'w') as f:
    print(str(the_page), file=f)


###Tukaj program poišče naslove, države,... in zbrise tiste elemente, kjer na spletni strani ni navedenih vseh podatkov.

idd = r'cc=(.*?)&amp;type=C&amp;ord=n">'
ids = re.findall(idd, str(the_page))

d = r'&amp;type=C&amp;ord=n">(.*?)</a></td>'
dr =  re.findall(d, str(the_page))   

s = r'<td class="center">(.*?)</td>'
st =  re.findall(s, str(the_page))
print(len(ids), len(dr), len(st), st)


with open('tuja.txt', 'w') as g:
    for i in range(len(ids)):
        g.write('INSERT INTO tujina (id, drzava, stevilo) VALUES (\'' + ids [i] + '\', \'' + dr[i] +'\', ' + st[i]+ ');\n')
        
  

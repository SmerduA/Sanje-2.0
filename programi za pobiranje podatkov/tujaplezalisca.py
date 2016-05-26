dr = ['AT', 'BA', 'CZ', 'ME', 'GR', 'HR', 'ZA', 'MA', 'DE', 'PL', 'SK', 'SI', 'ES', 'RS', 'SE', 'CH', 'TH', 'TR', 'US']
#dr = ['FR']
import urllib.parse
import urllib.request
import http.cookiejar
import re

dic = {}
st = []
ole = []
for i in dr:
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent:', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')]
    urllib.request.install_opener(opener)
    url = 'http://www.plezanje.net/climbing/db/cragIntro.asp?cc=' +i +'&type=C&ord=n'
    values = {}


    data  = urllib.parse.urlencode(values)
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(req)
    the_page = response.read().decode('utf-8')



    with open('plezalisca.html', 'w') as f:
        print(str(the_page), file=f)


    ###Tukaj program poišče naslove, države,... in zbrise tiste elemente, kjer na spletni strani ni navedenih vseh podatkov.

    #<td style="padding-left: 0em;"><a href="showCrag.asp?crag=1840&amp;p_ctx=long">Arnoldstein - Kindergarten</a></td>
#<td style="text-align: center">25</td>
#<td style="text-align: center">4a do 7a+</td>
    
    idd = r'showCrag.asp(.*?)&amp;p_ctx=long">'
    ids = re.findall(idd, str(the_page))
    aa = []
    for k in ids:
        aa += [k[6:]]
    #print(aa)
    st += aa   


    s = r'&amp;p_ctx=long">(.*?)</a></td>' 
    pl = re.findall(s, str(the_page))

    #print(pl)
    ole += pl
print(st, ole)    
##    ss = r'<td style="text-align: center">(.*?)</td>'
##    st = re.findall(ss, str(the_page))
##    a = []
##    b = []
##    for l in range(len(st)):
##        if l%2 == 1:
##            a += [st[l]]
##        else: b += [st[l]]
##
##    with open('tujaplezalisca.txt', 'a') as g:
##        for j in range(len(aa)):
##            try: g.write('INSERT INTO ' + i +' (id, ime, tezavnost, stevilo) VALUES (' + aa [j] + ', \'' + pl[j] +'\', \'' + a[j]+ '\', '+ b[j] + ');\n')
##            except IndexError: g.write(i + ' BRIŠI IMENA! \n')
##      
##

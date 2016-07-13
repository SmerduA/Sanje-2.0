import auth


import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki


import urllib.parse
import urllib.request
import http.cookiejar
import re





#cur.execute("""CREATE TABLE drzave (drzava TEXT NOT NULL PRIMARY KEY)""")
#cur.execute("""CREATE TABLE plezalisca (plezalisce TEXT NOT NULL PRIMARY KEY, drzava TEXT NOT NULL, FOREIGN KEY (drzava) REFERENCES drzave(drzava))""")
#cur.execute("""CREATE TABLE smeri (ime TEXT NOT NULL, tezavnost TEXT, dolzina INTEGER, plezalisce TEXT, PRIMARY KEY (ime, plezalisce), FOREIGN KEY (plezalisce) REFERENCES plezalisca(plezalisce))""")



#cj = http.cookiejar.CookieJar()
#opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#opener.addheaders = [('User-agent:', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')]
#urllib.request.install_opener(opener)
url = 'http://www.plezanje.net/climbing/db/countryIntro.asp?otype=C'
values = {}


data  = urllib.parse.urlencode(values)
data = data.encode('utf-8')

req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
the_page = response.read().decode('utf-8')


###Tukaj program poišče naslove, države,... in zbrise tiste elemente, kjer na spletni strani ni navedenih vseh podatkov.

idd = r'cc=(.*?)&amp;type=C&amp;ord=n">'
ids = re.findall(idd, str(the_page))

d = r'&amp;type=C&amp;ord=n">(.*?)</a></td>'
dr =  re.findall(d, str(the_page))   

print(len(ids), len(dr))


conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

for i in dr:
              if i =='Italija' or i == 'Francija':
                            pass
              else: cur.execute("INSERT INTO drzave VALUES ( \'" + str(i) + '\');' )
              

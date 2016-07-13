import auth


import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) 


#skopirano iz baza_drzave
dr = ['AT', 'BA', 'CZ', 'ME', 'GR', 'HR', 'ZA', 'MA', 'DE', 'PL', 'SK', 'SI', 'ES', 'RS', 'SE', 'CH', 'TH', 'TR', 'US']
drz = ['Avstrija', 'Bosna in Hercegovina', 'Češka', 'Črna gora', 'Grčija', 'Hrvaška', 'Juzna Afrika', 'Maroko', 'Nemčija', 'Poljska', 'Slovaška', 'Slovenija', 'Španija', 'Srbija', 'Švedska', 'Švica', 'Tajska', 'Turčija', 'Združene države Amerike']
import urllib.parse
import urllib.request
import http.cookiejar
import re
t = 0
dic = {}
st = []
ole = []
for i in dr:
    url = 'http://www.plezanje.net/climbing/db/cragIntro.asp?cc=' +i +'&type=C&ord=n'
    values = {}


    data  = urllib.parse.urlencode(values)
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(req)
    the_page = response.read().decode('utf-8')



    with open('plezalisca.html', 'w') as f:
        print(str(the_page), file=f)

    
    idd = r'showCrag.asp(.*?)&amp;p_ctx=long">'
    ids = re.findall(idd, str(the_page))
    aa = []
    for k in ids:
        aa += [k[6:]]
    st += aa   


    s = r'&amp;p_ctx=long">(.*?)</a></td>' 
    pl = re.findall(s, str(the_page))

    ole += pl



    conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    for j in range(len(aa)):
            try: cur.execute('INSERT INTO plezalisca (plezalisce, drzava) VALUES (\'' + pl[j] +'\', \'' + drz[t]+'\');')
            except (IndexError, psycopg2.ProgrammingError, psycopg2.IntegrityError) as e: pass
            
              
              
    t += 1

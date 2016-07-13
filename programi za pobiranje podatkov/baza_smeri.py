import auth


import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) 


import urllib.parse
import urllib.request
import http.cookiejar
import re


pl = {'751': 'Joshua Tree', '1784': 'Chulilla', '1715': 'Tenerife - El Hoyo', '1519': 'Montsant', '1031': 'Rodellar', '1912': 'Perun', '1019': 'Korošica', '1111': 'Hvar - Podstine', '1743': 'Krkuž', '752': 'Košutnikov turn', '612': 'Pisano čelo', '635': 'Šoder graben', '1860': 'Paklenica - Vaganac', '1562': 'Okrešelj', '628': 'Slap ob Idrijci', '1498': 'Terradets - Paret de les Bruixes', '1109': 'Göltschach / Golšovo', '607': 'Mlinarjeva peč', '1553': 'Bast', '1720': 'Monteseel', '1762': 'Calico Hills, The Gallery', '978': 'Chiang Mai - Crazy Horse Buttress', '1087': 'Kochel', '601': 'Lutne Skale', '1157': 'Nugla', '1731': 'Catalunya - Tartareu', '608': 'Močilnik', '594': 'Kotečnik', '698': 'Plitvice - Gajina pećina', '969': 'Krabi - Ton Sai Wall and Roof', '1797': 'Voulismeno ALONI', '1564': 'Nomenj', '579': 'Čolnišče', '1704': 'Ewige Jagdgründe', '1492': 'Grazer Bergland', '687': 'Krk - Portafortuna', '570': 'Bitnje', '1746': 'Kanjon Rječine', '637': 'Pri Plajerju (Trenta)', '1825': 'Kameni most', '1566': 'Dov', '1898': 'Roč', '808': 'Križevska vas', '586': 'Gromberg', '1131': 'Krk - Bunculuka', '577': 'Burjakove peči', '750': 'Kot (nad Prevaljami)', '626': 'Rudnica', '705': 'Ugljan', '1599': 'alaro', '1679': 'Simmering', '614': 'Pod Reško planino', '605': 'Matvoz', '646': 'Završnica', '1559': 'Kanin', '1867': 'Pod Golico', '694': 'Pag - Stogaj', '634': 'Šnitov rob', '690': 'Marjan', '1211': 'Čreta', '1725': 'Catalunya - Cubelles', '1729': 'Catalunya - Santa Linya', '1728': 'Catalunya - Santa Ana', '1750': 'Krvavica', '689': 'Malačka', '1345': 'Tenerife - Arico', '649': 'Renke', '588': 'Iški Vintgar', '1796': 'Skoteino Cave', '1598': 'Gorg Blau', '1065': 'Lavamünd / Labot', '633': 'Šeginov potok', '1726': 'Catalunya - La Pauta', '1560': 'Škratova skala', '1348': 'Tenerife - El Rio', '1721': 'Boneyard (Kloof Gorge)', '970': "Krabi - Wee's Present Wall", '578': 'Čerjan', '736': 'Hunerkogel', '889': 'Petit gorge', '691': 'Markezina greda', '1012': 'Bad Eisenkappel / Železna Kapla', '1303': 'Telendos', '1638': 'Oberdörf-Bubichopf', '1845': 'Jelašnička klisura', '1113': 'Hvar - Velika Stiniva', '763': 'Peč (pri Bohinju)', '678': 'Dabarski kukovi', '973': 'Krabi - Eagle Wall', '1841': 'Woelfnitz - Eibischwandl', '624': 'Retovje', '704': 'Trogir - Sveti Vid', '673': 'Brač - Ložišća', '1835': 'Töllsjo', '1174': 'Konavle', '591': 'Kamniška bistrica', '710': 'Vela Draga', '1711': 'Engelberg', '1173': 'Žarkovica - Gornji Brgat', '621': 'Radlje', '1766': 'Arboli', '1678': 'Tumpen (Engelswand)', '1016': 'Cres - Babina', '1779': 'Šumberk', '700': 'Rabac', '1651': 'Krakow - Labajowa', '1580': 'Taghia', '1798': 'Tartareu', '714': 'Ljubelj', '1823': 'Bielsa', '1347': 'Tenerife - Las Bovedas', '1143': 'Geyikbayiri', '598': 'Lipje', '963': 'Tijuana (Santanyi)', '1673': 'Zrmanja Džebinovac', '606': 'Mišja peč', '580': 'Črni Kal', '630': 'Socka', '681': 'Dvigrad', '1579': 'Piljitor', '1495': 'Oliana', '596': 'Krvavec', '753': 'Calico Basin', '595': 'Kovačevec', '683': 'Istarske toplice', '620': 'Pri Žvikarju', '632': 'Strug', '1286': 'Margalef', '1834': 'Kršlenica', '572': 'Boč', '1563': 'Prepihova dolina', '1602': 'Cala Marganer', '1810': 'Predloka', '712': 'Zir', '703': 'Terihaj', '625': 'Risnik', '589': 'Kal-Koritnica', '1096': 'Frankenjura', '699': 'Ponte porton', '643': 'Vršič', '599': 'Logarska dolina', '1730': 'Catalunya - Sant Llorenç de Montgai', '618': 'Pri Čiginju', '583': 'Gore', '1176': 'Radetina greda', '890': 'Dalle holandes', '1162': 'Rotelstein', '1727': 'Catalunya - Os de Balaguer', '1399': 'Kalymnos - južni del (South)', '717': 'Pokojec', '1565': 'Šavnica', '1447': 'Belove stene', '604': 'Matjaževe kamre', '641': 'Vranja peč', '640': 'Vipavska Bela', '582': 'Dovžanova soteska', '1744': 'Bobanova greda', '1600': 'Les perxes', '1467': 'Sollius', '658': 'Rovinj', '569': 'Bitenj potok', '1852': 'Hvar - Pokrivenik', '1759': 'Vilanova de Prades', '616': 'Porezen', '1596': 'Grdoba', '1826': 'Suturlija', '1795': 'Foz de la canal', '587': 'Igla', '693': 'Okić', '679': 'Dolina Raše - Zub', '615': 'Pod Sušo', '1626': 'spyderman wall', '1894': 'Brač - Smrka', '1694': 'Bergstation', '585': 'Gornji Ig', '619': 'Pri Pavru', '1548': 'Töschling', '971': 'Krabi - Diamond Cave', '1893': 'Čikola kanjon', '657': 'Ravna gora', '672': 'Božin kuk', '837': 'Theopetra', '976': 'Krabi - One Two Three', '1655': 'Pod Škalo', '1707': 'Liebethal', '711': 'Zia', '629': 'Slomnik', '1913': 'Mallorca - Valldemossa', '1710': 'Karin', '584': 'Gorje', '1140': 'Marof', '1431': "Mallorca - S'estret", '766': 'Rabenstein', '696': 'Papuk - Sokoline stijene', '1603': 'cala barques', '1442': 'Drnulk', '1288': 'Sapotniza / Sopotnica', '600': 'Luknja', '590': 'Kamnik', '756': 'Kupljenik', '702': 'Strogir', '610': 'Nadiža', '639': 'Vipava', '1484': 'Kanzianiberg / Škocjanska gora', '697': 'Pazin', '609': 'Nad Savo', '1630': 'St. Llorenc de Montgai', '622': 'Radovna', '692': 'Mošćenićka Draga', '631': 'Sopota', '638': 'Turnc', '685': 'Klek', '680': 'Konavle - Pićete', '1824': 'Pecka', '1152': 'Krabi - Melting Wall', '1629': 'Klobuk', '574': 'Bohinj', '713': 'Omiš', '962': 'Sa Gubia', '975': 'Krabi - Muay Thai', '836': 'Agria', '974': "Krabi - Dum's Kitchen", '611': 'Osp', '688': 'Limski kanal', '1701': 'Obli kuk - Prezid', '701': 'Raspadalica', '1461': 'Prtovč', '952': 'Jammerwadl', '1785': 'Capçanes', '676': 'Cres - Lubenice', '1723': 'Catalunya - Alos de Balaguer', '1175': 'Pod Ključicom', '1601': 'eremita de betlem', '1597': 'port de solrer', '636': 'Štenge', '1558': 'Žvanov rob', '1316': 'Snovik', '576': 'Buncove skale', '1749': 'Drašnice', '1583': 'Oberried', '642': 'Vransko', '708': 'Vis - Crnjene stijene', '1745': 'Brseč', '682': 'Hvar - Šuplja stina', '1582': 'Wiesensee', '568': 'Armeško', '1030': 'Pod Kopitcem', '764': 'Senica', '1561': 'Kegl', '1690': 'Plakias', '1840': 'Arnoldstein - Kindergarten', '1650': 'Kamena vrata', '1910': 'Mallorca - La Creveta', '1191': 'Rosenbach / Podrožca', '1074': 'El Chorro', '647': 'Zelenc pri Izlakah', '1621': 'Port de Soller', '1891': 'Brač - Nerežišća', '757': 'Rupotine (Klis)', '715': 'Golubinjak', '1110': 'Hvar - Milna', '1772': 'Scharnitz Sonnenplatten', '573': 'Bodešče', '707': 'Vinkuran', '677': 'Čepić', '1438': 'Sopot', '706': 'Veli vrh', '835': 'Kalogria', '1454': 'Mixnitz', '1195': 'Urbasova skala', '977': 'Krabi - Thaiwand Wall', '709': 'Vranja peč', '792': 'Alkazar', '675': 'Buzetski kanjon', '623': 'Rakitnica', '684': 'Kamenjak', '571': 'Blažčeva skala', '845': 'Raunjak', '613': 'Lavorček', '686': 'Kozjak', '972': 'Krabi - The Nest/Wild Kingdom', '627': 'Sele', '648': 'Pri Skalarju - Zminec', '1112': 'Hvar - Straćine', '617': 'Preddvor', '695': 'Paklenica', '592': 'Kamnitnik', '1718': 'LLaberia/tivisa', '956': 'Thalhofergrat', '1822': 'Scharnitz Am Sportplatz', '1497': 'Collegats - La Pedrera', '1161': 'Kompanj', '869': 'Kalymnos - osrednji del (Central)', '575': 'Bohinjska Bela', '1285': 'Siurana', '674': 'Brela', '1892': 'Brač - Selca/Povlja', '1827': 'Smith Rock', '581': 'Dolge njive', '597': 'Lijak', '1748': 'Zadvarje', '875': 'Kalymnos - severni del (North)', '1499': 'Tres Ponts', '1747': 'Lošinj - Osoršćica', '1692': 'Pelješac - Orebić', '716': 'Kalnik', '1724': 'Catalunya - Camarasa', '1895': 'Leonidio', '1584': 'Agiofarago'}

print(len(pl))
for i in pl:
    print(i)
    url = 'http://www.plezanje.net/climbing/db/showCrag.asp?crag=' + i + '&p_ctx=long'
    values = {}


    data  = urllib.parse.urlencode(values)
    data = data.encode('utf-8')


    req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(req)
    the_page = response.read().decode('utf-8')



    with open('plezalisca.html', 'w') as f:
        try: print(str(the_page), file=f)
        except UnicodeEncodeError:pass


    s = r'<a href="showRoute.asp(.*?)</a></td>' 
    smer = re.findall(s, str(the_page))
    

    ss = r'<p>(.*?)</p>'
    tezavnost= re.findall(ss, str(the_page))
   

    sss = r'<td class="right">(.*?)</td>'
    visina = re.findall(sss, str(the_page))
    
    S = []
    T = []
    V = visina
    for k in range(len(smer)):
        S += [smer[k].split('>')[1]]
        try:
            a = [(tezavnost[k].split('>')[1]).split('<')[0][0]]
            if a == 'P' or a == 'V' or a == 'I':
                          pass
            else: T += [(tezavnost[k].split('>')[1]).split('<')[0][0]]
        except IndexError:
            b = [tezavnost[k][0]]
            if b == 'P' or b == 'V' or b == 'I':
                          pass
            else: T += [tezavnost[k][0]]
      

    conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    for j in range(len(smer)):
            try:cur.execute('INSERT INTO ' + 'smeri' + ' (ime, tezavnost, dolzina, plezalisce) VALUES (\'' + S[j] +'\', \'' + T[j]+ '\', '+ V[j][:-2] + ', '+ '\'' + pl[i]+ '\'' +');\n')
            except (IndexError, psycopg2.ProgrammingError, psycopg2.IntegrityError, UnicodeEncodeError) as e: pass
            
              


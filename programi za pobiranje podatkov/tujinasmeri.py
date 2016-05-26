#pl = ['1840', '1012', '1694', '1704', '1109', '1492', '736', '952', '1484', '752', '1065', '1454', '1583', '766', '845', '1191', '1162', '1288', '1822', '1772', '1679', '956', '1548', '1678', '1582', '1841','1825', '1824', '1826','792','1579','1584', '836', '835', '1399', '869', '1895', '1690', '1796', '1303', '837', '1797', '1553', '1447', '1744', '672', '673', '1891', '1892', '1894', '674', '1745', '675', '677', '1893', '1016', '676', '678', '679', '1749', '681', '715', '1110', '1111', '1852', '1112', '682', '1113', '683', '716', '1650', '684', '1746', '1710', '685', '1629', '1161', '1174', '680', '686', '1131', '687', '1743', '1750', '688', '714', '1747', '689', '690', '691', '692', '1157', '1701', '693', '713', '694', '695', '1860', '696', '697', '1692', '698', '1175', '717', '699', '700', '1176', '701', '657', '1898', '658', '757', '1438', '702', '703', '704', '705', '710', '706', '707', '708', '709', '1748', '1173', '711', '712', '1673', '1721', '1720', '890', '889', '1580', '1096', '1087', '1707', '1651', '1834', '568', '569', '570', '571', '572', '573', '574', '575', '576', '577', '578', '579', '1211', '580', '581', '1566', '582', '1442', '583', '584', '585', '586', '587', '588', '589', '590', '591', '592', '1559', '1561', '1019', '750', '594', '595', '808', '596', '756', '613', '597', '598', '599', '600', '601', '1140', '604', '605', '606', '607', '608', '609', '610', '1564', '1562', '611', '763', '612', '1867', '1030', '614', '1655', '615', '616', '617', '1810', '1563', '618', '619', '637', '648', '620', '1461', '621', '622', '623', '649', '624', '625', '626', '1565', '633', '627', '764', '1560', '628', '629', '634', '1316', '630', '635', '631', '636', '632', '1779', '638', '1195', '639', '640', '641', '642', '643', '646', '647', '1558', '1599', '1766', '1823', '1603', '1602', '1785', '1723', '1724', '1725', '1726', '1727', '1730', '1728', '1729', '1731', '1784', '1497', '1074', '1601', '1795', '1598', '1600', '1718', '1431', '1286', '1519', '1495', '1621', '1597', '1031', '962', '1285', '1467', '1630', '1798', '1345', '1715', '1348', '1347', '1498', '963', '1499', '1759', '1596', '1845', '1835', '1711', '1638', '978', '971', '974', '973', '1152', '975', '976', '977', '972', '969', '970', '1626', '1143', '753', '1762', '751', '1827']
import urllib.parse
import urllib.request
import http.cookiejar
import re
#pl = ['1711', '1638', '978', '971', '974', '973', '1152', '975', '976', '977', '972', '969', '970', '1626', '1143', '753', '1762', '751', '1827']
#875, 1895, 687, 1784, 1031, 1729, 1285, 1835

pl = {'751': 'Joshua Tree', '1784': 'Chulilla', '1715': 'Tenerife - El Hoyo', '1519': 'Montsant', '1031': 'Rodellar', '1912': 'Perun', '1019': 'Korošica', '1111': 'Hvar - Podstine', '1743': 'Krkuž', '752': 'Košutnikov turn', '612': 'Pisano čelo', '635': 'Šoder graben', '1860': 'Paklenica - Vaganac', '1562': 'Okrešelj', '628': 'Slap ob Idrijci', '1498': 'Terradets - Paret de les Bruixes', '1109': 'Göltschach / Golšovo', '607': 'Mlinarjeva peč', '1553': 'Bast', '1720': 'Monteseel', '1762': 'Calico Hills, The Gallery', '978': 'Chiang Mai - Crazy Horse Buttress', '1087': 'Kochel', '601': 'Lutne Skale', '1157': 'Nugla', '1731': 'Catalunya - Tartareu', '608': 'Močilnik', '594': 'Kotečnik', '698': 'Plitvice - Gajina pećina', '969': 'Krabi - Ton Sai Wall and Roof', '1797': 'Voulismeno ALONI', '1564': 'Nomenj', '579': 'Čolnišče', '1704': 'Ewige Jagdgründe', '1492': 'Grazer Bergland', '687': 'Krk - Portafortuna', '570': 'Bitnje', '1746': 'Kanjon Rječine', '637': 'Pri Plajerju (Trenta)', '1825': 'Kameni most', '1566': 'Dov', '1898': 'Roč', '808': 'Križevska vas', '586': 'Gromberg', '1131': 'Krk - Bunculuka', '577': 'Burjakove peči', '750': 'Kot (nad Prevaljami)', '626': 'Rudnica', '705': 'Ugljan', '1599': 'alaro', '1679': 'Simmering', '614': 'Pod Reško planino', '605': 'Matvoz', '646': 'Završnica', '1559': 'Kanin', '1867': 'Pod Golico', '694': 'Pag - Stogaj', '634': 'Šnitov rob', '690': 'Marjan', '1211': 'Čreta', '1725': 'Catalunya - Cubelles', '1729': 'Catalunya - Santa Linya', '1728': 'Catalunya - Santa Ana', '1750': 'Krvavica', '689': 'Malačka', '1345': 'Tenerife - Arico', '649': 'Renke', '588': 'Iški Vintgar', '1796': 'Skoteino Cave', '1598': 'Gorg Blau', '1065': 'Lavamünd / Labot', '633': 'Šeginov potok', '1726': 'Catalunya - La Pauta', '1560': 'Škratova skala', '1348': 'Tenerife - El Rio', '1721': 'Boneyard (Kloof Gorge)', '970': "Krabi - Wee's Present Wall", '578': 'Čerjan', '736': 'Hunerkogel', '889': 'Petit gorge', '691': 'Markezina greda', '1012': 'Bad Eisenkappel / Železna Kapla', '1303': 'Telendos', '1638': 'Oberdörf-Bubichopf', '1845': 'Jelašnička klisura', '1113': 'Hvar - Velika Stiniva', '763': 'Peč (pri Bohinju)', '678': 'Dabarski kukovi', '973': 'Krabi - Eagle Wall', '1841': 'Woelfnitz - Eibischwandl', '624': 'Retovje', '704': 'Trogir - Sveti Vid', '673': 'Brač - Ložišća', '1835': 'Töllsjo', '1174': 'Konavle', '591': 'Kamniška bistrica', '710': 'Vela Draga', '1711': 'Engelberg', '1173': 'Žarkovica - Gornji Brgat', '621': 'Radlje', '1766': 'Arboli', '1678': 'Tumpen (Engelswand)', '1016': 'Cres - Babina', '1779': 'Šumberk', '700': 'Rabac', '1651': 'Krakow - Labajowa', '1580': 'Taghia', '1798': 'Tartareu', '714': 'Ljubelj', '1823': 'Bielsa', '1347': 'Tenerife - Las Bovedas', '1143': 'Geyikbayiri', '598': 'Lipje', '963': 'Tijuana (Santanyi)', '1673': 'Zrmanja Džebinovac', '606': 'Mišja peč', '580': 'Črni Kal', '630': 'Socka', '681': 'Dvigrad', '1579': 'Piljitor', '1495': 'Oliana', '596': 'Krvavec', '753': 'Calico Basin', '595': 'Kovačevec', '683': 'Istarske toplice', '620': 'Pri Žvikarju', '632': 'Strug', '1286': 'Margalef', '1834': 'Kršlenica', '572': 'Boč', '1563': 'Prepihova dolina', '1602': 'Cala Marganer', '1810': 'Predloka', '712': 'Zir', '703': 'Terihaj', '625': 'Risnik', '589': 'Kal-Koritnica', '1096': 'Frankenjura', '699': 'Ponte porton', '643': 'Vršič', '599': 'Logarska dolina', '1730': 'Catalunya - Sant Llorenç de Montgai', '618': 'Pri Čiginju', '583': 'Gore', '1176': 'Radetina greda', '890': 'Dalle holandes', '1162': 'Rotelstein', '1727': 'Catalunya - Os de Balaguer', '1399': 'Kalymnos - južni del (South)', '717': 'Pokojec', '1565': 'Šavnica', '1447': 'Belove stene', '604': 'Matjaževe kamre', '641': 'Vranja peč', '640': 'Vipavska Bela', '582': 'Dovžanova soteska', '1744': 'Bobanova greda', '1600': 'Les perxes', '1467': 'Sollius', '658': 'Rovinj', '569': 'Bitenj potok', '1852': 'Hvar - Pokrivenik', '1759': 'Vilanova de Prades', '616': 'Porezen', '1596': 'Grdoba', '1826': 'Suturlija', '1795': 'Foz de la canal', '587': 'Igla', '693': 'Okić', '679': 'Dolina Raše - Zub', '615': 'Pod Sušo', '1626': 'spyderman wall', '1894': 'Brač - Smrka', '1694': 'Bergstation', '585': 'Gornji Ig', '619': 'Pri Pavru', '1548': 'Töschling', '971': 'Krabi - Diamond Cave', '1893': 'Čikola kanjon', '657': 'Ravna gora', '672': 'Božin kuk', '837': 'Theopetra', '976': 'Krabi - One Two Three', '1655': 'Pod Škalo', '1707': 'Liebethal', '711': 'Zia', '629': 'Slomnik', '1913': 'Mallorca - Valldemossa', '1710': 'Karin', '584': 'Gorje', '1140': 'Marof', '1431': "Mallorca - S'estret", '766': 'Rabenstein', '696': 'Papuk - Sokoline stijene', '1603': 'cala barques', '1442': 'Drnulk', '1288': 'Sapotniza / Sopotnica', '600': 'Luknja', '590': 'Kamnik', '756': 'Kupljenik', '702': 'Strogir', '610': 'Nadiža', '639': 'Vipava', '1484': 'Kanzianiberg / Škocjanska gora', '697': 'Pazin', '609': 'Nad Savo', '1630': 'St. Llorenc de Montgai', '622': 'Radovna', '692': 'Mošćenićka Draga', '631': 'Sopota', '638': 'Turnc', '685': 'Klek', '680': 'Konavle - Pićete', '1824': 'Pecka', '1152': 'Krabi - Melting Wall', '1629': 'Klobuk', '574': 'Bohinj', '713': 'Omiš', '962': 'Sa Gubia', '975': 'Krabi - Muay Thai', '836': 'Agria', '974': "Krabi - Dum's Kitchen", '611': 'Osp', '688': 'Limski kanal', '1701': 'Obli kuk - Prezid', '701': 'Raspadalica', '1461': 'Prtovč', '952': 'Jammerwadl', '1785': 'Capçanes', '676': 'Cres - Lubenice', '1723': 'Catalunya - Alos de Balaguer', '1175': 'Pod Ključicom', '1601': 'eremita de betlem', '1597': 'port de solrer', '636': 'Štenge', '1558': 'Žvanov rob', '1316': 'Snovik', '576': 'Buncove skale', '1749': 'Drašnice', '1583': 'Oberried', '642': 'Vransko', '708': 'Vis - Crnjene stijene', '1745': 'Brseč', '682': 'Hvar - Šuplja stina', '1582': 'Wiesensee', '568': 'Armeško', '1030': 'Pod Kopitcem', '764': 'Senica', '1561': 'Kegl', '1690': 'Plakias', '1840': 'Arnoldstein - Kindergarten', '1650': 'Kamena vrata', '1910': 'Mallorca - La Creveta', '1191': 'Rosenbach / Podrožca', '1074': 'El Chorro', '647': 'Zelenc pri Izlakah', '1621': 'Port de Soller', '1891': 'Brač - Nerežišća', '757': 'Rupotine (Klis)', '715': 'Golubinjak', '1110': 'Hvar - Milna', '1772': 'Scharnitz Sonnenplatten', '573': 'Bodešče', '707': 'Vinkuran', '677': 'Čepić', '1438': 'Sopot', '706': 'Veli vrh', '835': 'Kalogria', '1454': 'Mixnitz', '1195': 'Urbasova skala', '977': 'Krabi - Thaiwand Wall', '709': 'Vranja peč', '792': 'Alkazar', '675': 'Buzetski kanjon', '623': 'Rakitnica', '684': 'Kamenjak', '571': 'Blažčeva skala', '845': 'Raunjak', '613': 'Lavorček', '686': 'Kozjak', '972': 'Krabi - The Nest/Wild Kingdom', '627': 'Sele', '648': 'Pri Skalarju - Zminec', '1112': 'Hvar - Straćine', '617': 'Preddvor', '695': 'Paklenica', '592': 'Kamnitnik', '1718': 'LLaberia/tivisa', '956': 'Thalhofergrat', '1822': 'Scharnitz Am Sportplatz', '1497': 'Collegats - La Pedrera', '1161': 'Kompanj', '869': 'Kalymnos - osrednji del (Central)', '575': 'Bohinjska Bela', '1285': 'Siurana', '674': 'Brela', '1892': 'Brač - Selca/Povlja', '1827': 'Smith Rock', '581': 'Dolge njive', '597': 'Lijak', '1748': 'Zadvarje', '875': 'Kalymnos - severni del (North)', '1499': 'Tres Ponts', '1747': 'Lošinj - Osoršćica', '1692': 'Pelješac - Orebić', '716': 'Kalnik', '1724': 'Catalunya - Camarasa', '1895': 'Leonidio', '1584': 'Agiofarago'}


for i in pl:
    if int(i) in [875, 1895, 687, 1784, 1031, 1729, 1285, 1835, 1895, 1729, 1431]:
         continue
    print(i)
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent:', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')]
    urllib.request.install_opener(opener)
    url = 'http://www.plezanje.net/climbing/db/showCrag.asp?crag=' + i + '&p_ctx=long'
    values = {}


    data  = urllib.parse.urlencode(values)
    data = data.encode('utf-8')


    req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(req)
    the_page = response.read().decode('utf-8')



    with open('plezalisca.html', 'w') as f:
        print(str(the_page), file=f)


    ###Tukaj program poišče naslove, države,... in zbrise tiste elemente, kjer na spletni strani ni navedenih vseh podatkov.


    s = r'<a href="showRoute.asp(.*?)</a></td>' 
    smer = re.findall(s, str(the_page))
    #print(smer)

    ss = r'<p>(.*?)</p>'
    tezavnost= re.findall(ss, str(the_page))
    #print(tezavnost)

    sss = r'<td class="right">(.*?)</td>'
    visina = re.findall(sss, str(the_page))
    #print(visina)
    S = []
    T = []
    V = visina
    for k in range(len(smer)):
        S += [smer[k].split('>')[1]]
        try:
            T += [(tezavnost[k].split('>')[1]).split('<')[0]]
        except IndexError:
            T += [tezavnost[k]]
      
   
    with open('smeri1.txt', 'a') as h:
        for j in range(len(smer)):
             try:
                h.write('INSERT INTO ' + 'smeri' + ' (ime, tezavnost, dolzina, plezalisce) VALUES (\'' + S[j] +'\', \'' + T[j]+ '\', '+ V[j][:-2] + ', '+ '\'' + pl[i]+ '\'' +');\n')
             except IndexError:
                h.write('INSERT INTO ' + 'smeri' + ' (ime, tezavnost, dolzina, plezalisce) VALUES (\'' + S[j] +'\', \'' + T[j]+ '\', '+ 'Null' + ',' + pl[i] +');\n')
            



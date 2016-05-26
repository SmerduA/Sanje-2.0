#!/usr/bin/python
# -*- encoding: utf-8 -*-

# uvozimo bottle.py
from bottle import *

# uvozimo ustrezne podatke za povezavo
import auth_public as auth

# uvozimo psycopg2
import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki

# odkomentiraj, če želiš sporočila o napakah
# debug(True)
@get('/')
def index():
    return template('zacetna')

@route('/drzave/')
def drzave_spisek():
    cur.execute("SELECT drzava FROM drzave ORDER BY drzava")
    return template('drzave.html', drzave=cur)

@route('/plezalisca/')
def plezalisce_spisek():
    """Glavna stran za urejanje postaj."""
    # Tu bi morali dobiti postaje iz baze
    cur.execute("SELECT plezalisce FROM plezalisca ORDER BY plezalisce")
    
    return template('plezalisca', plezalisca=cur)

@route('/smeri/')
def smeri_spisek():
    """Glavna stran za urejanje postaj."""
    # Tu bi morali dobiti postaje iz baze
    cur.execute("SELECT smer FROM smeri")
    
    return template('smeri', smeri=cur)

#@get('/transakcije/:x/')
#def transakcije(x):
 #   cur.execute("SELECT * FROM transakcija WHERE znesek > %s ORDER BY znesek, id", [int(x)])
 #   return template('transakcije.html', x=x, transakcije=cur)



######################################################################
# Glavni program

# priklopimo se na bazo
conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) # onemogočimo transakcije
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 

# poženemo strežnik na portu 8080, glej http://localhost:8080/
run(host='localhost', port=8080)

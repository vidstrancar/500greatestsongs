import csv
import os
import requests
import sys
import urllib.parse
import re
import pandas

def primerjajSeznama(sez1, sez2, R = 5):
    score = 0
    for index, vrstica in sez1.iterrows():
        if abs(pandas.Index(sez2).get_loc((vrstica['avtor'], vrstica['naslov'])) - index) <= R:
            score += 1
    return score

def poisciYtUrl(iskalni_niz):
	query_string = "http://www.youtube.com/results?" + urllib.parse.urlencode({"search_query" : iskalni_niz})
	html_content = requests.get(query_string, timeout=5).text
	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content)#.read().decode())
	if(len(search_results) > 0):
		URL = "http://www.youtube.com/watch?v=" + search_results[0] #vzamemo prvi link
		return URL
	return "NOY" #not on youtube.

def pripravi_imenik(ime_datoteke):
    '''Če še ne obstaja, pripravi prazen imenik za dano datoteko.'''
    imenik = os.path.dirname(ime_datoteke)
    if imenik:
        os.makedirs(imenik, exist_ok=True)

def shrani(url, ime_datoteke, vsili_prenos=False):
    '''Vsebino strani na danem naslovu shrani v datoteko z danim imenom.'''
    try:
        print('Shranjujem {}...'.format(url), end='')
        sys.stdout.flush()
        if os.path.isfile(ime_datoteke) and not vsili_prenos:
            print('shranjeno že od prej!')
            return
        r = requests.get(url, headers={'Accept-Language': 'en'})
    except requests.exceptions.ConnectionError:
        print('stran ne obstaja!')
    else:
        pripravi_imenik(ime_datoteke)
        with open(ime_datoteke, 'wb') as datoteka:
            datoteka.write(r.text.encode('utf-8'))
            print('shranjeno!')

def vsebina_datoteke(ime_datoteke):
    '''Vrne niz z vsebino datoteke z danim imenom.'''
    with open(ime_datoteke) as datoteka:
        vsebina = datoteka.read()
    return vsebina

def datoteke(imenik):
    '''Vrne imena vseh datotek v danem imeniku skupaj z imenom imenika.'''
    return [os.path.join(imenik, datoteka) for datoteka in os.listdir(imenik)]

def zapisi_tabelo(slovarji, imena_polj, ime_datoteke):
    '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
    pripravi_imenik(ime_datoteke)
    with open(ime_datoteke, 'w') as csv_dat:
        writer = csv.DictWriter(csv_dat, fieldnames=imena_polj)
        writer.writeheader()
        for slovar in slovarji:
            writer.writerow(slovar)

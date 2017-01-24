import csv
import requests
import re

urlSeznama = 'http://lyrics.wikia.com/wiki/LyricWiki:Lists/Rolling_Stone:_The_500_Greatest_Songs_of_All_Time'
vsebinaStrani = requests.get(urlSeznama).text
regexIzraz = """<li> <b><a href=".*?" title="(.*):(.*)">.*title.*</a>\s?</li>"""

with open('seznam.csv', 'w') as csvfile:
    fieldnames = ['avtor', 'naslov']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for ujemanje in re.finditer(regexIzraz, vsebinaStrani):
        avtor = re.sub('\&amp;', 'and', ujemanje.group(1))
        naslov = re.sub('\&quot;', '', ujemanje.group(2))
        try:
            writer.writerow({'avtor': avtor, 'naslov': naslov})
        except:
            writer.writerow({'avtor': 'cudna so', 'naslov': ' pota gospodova'})






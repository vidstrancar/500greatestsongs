import csv
import requests
import orodja

seznamAvtNasUrl = []
with open('seznam.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    
    with open('seznamUrl.csv', 'w') as csvfile2:
        fieldnames = ['avtor', 'naslov', 'url']
        writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            avtor = row['avtor']
            naslov = row['naslov']
            print(naslov)
            url = orodja.poisciYtUrl(avtor + ' ' + naslov)  
            writer.writerow({'avtor': avtor, 'naslov': naslov, 'url': url})
        #orodja.shrani(url, iskalniNiz + '.html')







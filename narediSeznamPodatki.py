import youtube_dl
import csv

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
seznam=[]


seznamAvtNasUrl = []
with open('seznamUrl.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    songId = 1
    
    with open('seznamPodatki.csv', 'w') as csvfile2:
        fieldnames = ['id', 'avtor', 'naslov', 'upload_date', 'duration', 'view_count', 'like_count',
        'dislike_count', 'average_rating']
        writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            avtor = row['avtor']
            naslov = row['naslov']
            url = row['url']
            print(songId, avtor, naslov)
            if url != "NOY" and avtor != "cudna so":
                with ydl:
                    result = ydl.extract_info(url,download=False)
                    upload_date = result['upload_date']
                    duration = result['duration']
                    view_count = result['view_count']
                    like_count = result['like_count']
                    dislike_count = result['dislike_count']
                    average_rating = result['average_rating']
                    writer.writerow({
                        'id': songId,
                        'avtor': avtor,
                        'naslov': naslov,
                        'upload_date': upload_date,
                        'duration': duration,
                        'view_count': view_count,
                        'like_count': like_count,
                        'dislike_count': dislike_count,
                        'average_rating': average_rating })
            else:
                upload_date=duration=view_count=like_count=dislike_count=average_rating= 0
                writer.writerow({
				    'id': songId,
                    'avtor': avtor,
                    'naslov': naslov,
                    'upload_date': upload_date,
                    'duration': duration,
                    'view_count': view_count,
                    'like_count': like_count,
                    'dislike_count': dislike_count,
                    'average_rating': average_rating })
            songId += 1
				
				
				
							

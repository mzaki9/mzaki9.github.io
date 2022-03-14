# Import package requests dan BeautifulSoup
import requests
from bs4 import BeautifulSoup

from datetime import datetime

now = datetime.now()

# Request ke website
page = requests.get("https://www.republika.co.id/")

# Extract konten menjadi objek BeautifulSoup
obj = BeautifulSoup(page.text, "html.parser")

print("Judul")
print("==========================================")
for headline in obj.find_all("div", class_="conten1"):
    print(headline.find("h2").text)


print("\nWaktu Publish berita")
print("========================")
for publish in obj.find_all("div", class_="date"):
    print(publish.text)
    
print("\nKategori Berita")
print("========================")
for publish in obj.find_all("div", class_="teaser_conten1_center"):
    print(publish.find("a").text)


print("\nWaktu Scraping")
print("========================")
for publish in obj.find_all("div", class_="date"):
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Waktu Scraping =", dt_string)


#import package json
import json
# Deklarasi list kosong
data=[]
# Lokasi file json
f=open('D:\\headline.json','w')
for publish in obj.find_all('div',class_='conten1'):
    # append headline ke variable data
    data.append({"judul":publish.find('h2').text,"kategori":publish.find('a').text,"waktu_publish":publish.find('div',class_='date').text,"waktu_scraping":now.strftime("%Y-%m-%d %H:%M:%S")})
# dump list dictionary menjadi json
jdumps=json.dumps(data, indent=2)
f.writelines(jdumps)
f.close()


from bs4 import BeautifulSoup
import urllib.request
import csv

url =  'https://www.statbunker.com/alltimestats/AllTimeLeagueTable?comp_code=EPL'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
tabel = soup.find('table', attrs={'class': 'table'})
hasil = tabel.find_all('tr')
kolom = []
kolom.append(['Peringkat', 'Nama Klub','Banyak Pertandingan','Menang','Seri', 'Kalah', 'Gol', 'Kemasukan','Selisih Gol','Poin',
             'Persentase Menang','Poin per match', 'Topskor', 'Banyaknya Gol'])

for bahan in hasil:
    data = bahan.find_all('td')
    if len(data)==0:
        continue
    peringkat = data[0].getText()
    namaklub = data[1].getText()
    pertandingan = data[2].getText()
    menang = data[3].getText()
    seri = data[4].getText()
    kalah = data[5].getText()
    gol = data[6].getText()
    kemasukan = data[7].getText()
    selisihgol = data[8].getText()
    poin = data[9].getText()
    persenmenang = '0.'+(data[10].getText().replace('%',''))
    poinpermatch = data[11].getText()
    
    url2 = 'https://www.statbunker.com'+data[1].find('a').get('href')
    page2 = urllib.request.urlopen(url2)
    soup2 = BeautifulSoup(page2, 'html.parser')
    top = soup2.find('tbody').find_all('tr')[0].find_all('td')
    topskor = top[0].getText()
    golnya = top[1].getText()
    
    kolom.append([peringkat,namaklub,pertandingan,menang,seri,kalah,gol,kemasukan,selisihgol,poin,persenmenang,poinpermatch,
                 topskor,golnya])
    
with open('alltime_epl_table.csv','w', newline='') as outputkita:
    myoutput = csv.writer(outputkita)
    myoutput.writerows(kolom)

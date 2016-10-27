import re , urllib


liste=["Kuyumcu Alis","Kuyumcu Satis"]

# gerekli olan adres
website=urllib.urlopen("http://www.bigpara.com/altin/ceyrek-altin-fiyati")

#buradan tüm datayı okuduk
htmltext=website.read()

# site icinde altin fiyatinin bulundugu alani sectik
getinspect='<span class="value up">(.+?)</span>'

pattern=re.compile(getinspect)
price=re.findall(pattern,htmltext)

j=0
for i in price:
    print liste[j]+" fiyati: "+i
    j+=1

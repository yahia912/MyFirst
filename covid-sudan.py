from bs4 import BeautifulSoup as soup
from requests import get 
print("""
░█████╗░░█████╗░██╗░░░██╗██╗██████╗░
██╔══██╗██╔══██╗██║░░░██║██║██╔══██╗
██║░░╚═╝██║░░██║╚██╗░██╔╝██║██║░░██║
██║░░██╗██║░░██║░╚████╔╝░██║██║░░██║
╚█████╔╝╚█████╔╝░░╚██╔╝░░██║██████╔╝
░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝╚═════╝░""")
print("\n")
print("======================================================")

print("""1)Sudan
2)UK
3)Egypt
4)USA
5)Worldwide
6)UAE
7)KSA
8)Qatar
9)Yemen
10)China""")
try:
	g=int(input("Choose country: "))
except:
	print("======================================================")
	print("                 Choose a valid number")
	print("======================================================")
	g=int(input("Choose country: "))
if g==1:
	url=("https://www.worldometers.info/coronavirus/country/sudan/")
	rq=get(url)
	page=soup(rq.content,"html.parser")
	f=((page.title).get_text())
	l=f.split()
	del l[7:9]
elif g==2:
	url=("https://www.worldometers.info/coronavirus/country/uk/")
	rq=get(url)
	page=soup(rq.content,"html.parser")
	f=((page.title).get_text())
	l=f.split()
	del l[8:10]
elif g==3:
	url=("https://www.worldometers.info/coronavirus/country/egypt/")
	rq=get(url)
	page=soup(rq.content,"html.parser")
	f=((page.title).get_text())
	l=f.split()
	del l[7:9]
elif g==4:
	url=("https://www.worldometers.info/coronavirus/country/us/")
	rq=get(url)
	page=soup(rq.content,"html.parser")
	f=((page.title).get_text())
	l=f.split()
	del l[8:10]
elif g==5:
	url=("https://www.worldometers.info/coronavirus/")
	rq=get(url)
	page=soup(rq.content,"html.parser")
	f=((page.title).get_text())
	l=f.split()
	l[1]="cases"
	l[2]="worldwide : "
	del l[12:14]
elif g==6:
	url=("https://www.worldometers.info/coronavirus/country/united-arab-emirates/")
	rq=get(url)
	page=soup(rq.content,"html.parser")
	f=((page.title).get_text())
	l=f.split()
	del l[9:11]
elif g==7:
	url=("https://www.worldometers.info/coronavirus/country/saudi-arabia/")
	rq=get(url)
	page=soup(rq.content,"html.parser")
	f=((page.title).get_text())
	l=f.split()
	del l[8:10]
elif g==8:
	url=("https://www.worldometers.info/coronavirus/country/qatar/")
	rq=get(url)
	page=soup(rq.content,"html.parser")
	f=((page.title).get_text())
	l=f.split()
	del l[7:9]
elif g==9:
	url=("https://www.worldometers.info/coronavirus/country/yemen/")
	
	rq=get(url)
	page=soup(rq.content,"html.parser")
	f=((page.title).get_text())
	l=f.split()
	del l[7:9]
elif g==10:
	url=("https://www.worldometers.info/coronavirus/country/china/")
	rq=get(url)
	page=soup(rq.content,"html.parser")
	f=((page.title).get_text())
	l=f.split()
	del l[7:9]
	
	
	
print("\n")

print(" ".join(l))
print("""
╭╮╱╱╭┳━━━╮
┃╰╮╭╯┃╭━╮┃
╰╮╰╯╭┻╯╭╯┣╮╱╭┳━━╮
╱╰╮╭╯╱╱┃╭┫┃╱┃┃╭╮┃
╱╱┃┃╱╱╱┃┃┃╰━╯┃╭╮┃
╱╱╰╯╱╱╱╰╯╰━╮╭┻╯╰╯
╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╰━━╯""")

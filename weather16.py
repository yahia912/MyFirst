from requests import get
from bs4 import BeautifulSoup as soup
print("""1)Khartoum
2)Dongola
3)Wadi Halfa
4)Port Sudan
5)Kassala
6)Atbara
7)El Obeid
8)Nyala
9)Omdurman
10)WadMadani
11)Kadugli
12)Kosti
13)Al Qadarif
14)Al Fashir
15)Suakin
""")
print("                   Type x for exit")
print("======================================================")
print("\n")

while True:
	city=(input("City number: "))
	if city=="1":
		url="https://www.weather-atlas.com/en/sudan/khartoum"
	elif city=="2":
		url="https://www.weather-atlas.com/en/sudan/dongola"
	elif city=="3":
		url="https://www.weather-atlas.com/en/sudan/Wadi-Halfa"
	elif city=="4":
		url="https://www.weather-atlas.com/en/sudan/Port-Sudan"
	elif city=="5":
		url="https://www.weather-atlas.com/en/sudan/Kassala"
	elif city=="6":
		url="https://www.weather-atlas.com/en/sudan/Atbara"
	elif city=="7":
		url="https://www.weather-atlas.com/en/sudan/El-Obeid"
	elif city=="8":
		url="https://www.weather-atlas.com/en/sudan/Nyala"
	elif city=="9":
		url="https://www.weather-atlas.com/en/sudan/Omdurman"
	elif city=="10":
		url="https://www.weather-atlas.com/en/sudan/WadMadani"
	elif city=="11":
		url="https://www.weather-atlas.com/en/sudan/Kadugli"
	elif city=="12":
		url="https://www.weather-atlas.com/en/sudan/Kosti"
	elif city=="13":
		url="https://www.weather-atlas.com/en/sudan/Al-Qadarif"
	elif city=="14":
		url="https://www.weather-atlas.com/en/sudan/Al-Fashir"
	elif city=="15":
		url="https://www.weather-atlas.com/en/sudan/Suakin"
	
	elif "x" in city or "X"in city:
		print("""
╭━━╮╱╱╱╱╱╱╱╱╱╱╭━━━╮
┃╭╮┃╱╱╱╱╱╱╱╱╱╱┃╭━╮┃
┃╰╯╰┳╮╱╭╮╭╮╭╮╱┣┫╭╯┣╮╱╭┳━━╮
┃╭━╮┃┃╱┃┃╰╯┃┃╱┃┃┃╭┫┃╱┃┃╭╮┃
┃╰━╯┃╰━╯┃╭╮┃╰━╯┃┃┃┃╰━╯┃╭╮┃
╰━━━┻━╮╭╯╰╯╰━╮╭╯╰╯╰━╮╭┻╯╰╯
╱╱╱╱╭━╯┃╱╱╱╭━╯┃╱╱╱╭━╯┃
╱╱╱╱╰━━╯╱╱╱╰━━╯╱╱╱╰━━╯""")
		exit()
	else:
		print("======================================================")
		print("               Choose a valid option\n")
		print("======================================================")
		continue
	
	rq=get(url)
	page=soup(rq.content,"html.parser")
	weather= page.find('li', class_='fs-2').text
	state=page.find('span', class_='fs-3 fw-bold').text
	place=url[39:]
	print(f"it is {weather} in {place}({state})")
					
		
	
	 
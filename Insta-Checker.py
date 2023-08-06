import sys
import colorama
from termcolor import colored
from colorama import Fore, Style
from bs4 import BeautifulSoup as soup
from requests import get
from threading import Thread
from termcolor import colored
import random
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


with open("Accounts.txt","r")as f:
	 c=[line.strip() for line in f]
len=len(c)
t1=int(1/10*len)
t2=int(2/10*len)
t3=int(3/10*len)
t4=int(4/10*len)
t5=int(5/10*len)
t6=int(6/10*len)
t7=int(7/10*len)
t8=int(8/10*len)
t9=int(9/10*len)

p1=c[0:t1]
p2=c[t1:t2]
p3=c[t2:t3]
p4=c[t3:t4]
p5=c[t4:t5]
p6=c[t5:t6]
p7=c[t6:t7]
p8=c[t7:t8]
p9=c[t8:t9]
p10=c[t9:len]
av=[]
def check1():
    for i in p1:
    	my_url=("https://www.instagram.com/%s/"%(i))
    	page_html=get(my_url)
    	page_soup=soup(page_html.text,"html.parser")
    	title=page_soup.title
    	for y in title:
    		if i in y:
    			print(i+colored(" taken","red"))
    		elif i not in y:
    			print(i+colored(" available","green"))
    			av.append(i)
def check2():
    for i in p2:
    	my_url=("https://www.instagram.com/%s/"%(i))
    	page_html=get(my_url)
    	page_soup=soup(page_html.text,"html.parser")
    	title=page_soup.title
    	for y in title:
    		if i in y:
    			print(i+colored(" taken","red"))
    		elif i not in y:
    			print(i+colored(" available","green"))
    			av.append(i)
def check3():
    for i in p3:
    	my_url=("https://www.instagram.com/%s/"%(i))
    	page_html=get(my_url)
    	page_soup=soup(page_html.text,"html.parser")
    	title=page_soup.title
    	for y in title:
    		if i in y:
    			print(i+colored(" taken","red"))
    		elif i not in y:
    			print(i+colored(" available","green"))
    			av.append(i)
def check4():
    for i in p4:
    	my_url=("https://www.instagram.com/%s/"%(i))
    	page_html=get(my_url)
    	page_soup=soup(page_html.text,"html.parser")
    	title=page_soup.title
    	for y in title:
    		if i in y:
    			print(i+colored(" taken","red"))
    		elif i not in y:
    			print(i+colored(" available","green"))
    			av.append(i)
def check5():
    for i in p5:
    	my_url=("https://www.instagram.com/%s/"%(i))
    	page_html=get(my_url)
    	page_soup=soup(page_html.text,"html.parser")
    	title=page_soup.title
    	for y in title:
    		if i in y:
    			print(i+colored(" taken","red"))
    		elif i not in y:
    			print(i+colored(" available","green"))
    			av.append(i)
def check6():
    for i in p6:
    	my_url=("https://www.instagram.com/%s/"%(i))
    	page_html=get(my_url)
    	page_soup=soup(page_html.text,"html.parser")
    	title=page_soup.title
    	for y in title:
    		if i in y:
    			print(i+colored(" taken","red"))
    		elif i not in y:
    			print(i+colored(" available","green"))
    			av.append(i)
def check7():
    for i in p7:
    	my_url=("https://www.instagram.com/%s/"%(i))
    	page_html=get(my_url)
    	page_soup=soup(page_html.text,"html.parser")
    	title=page_soup.title
    	for y in title:
    		if i in y:
    			print(i+colored(" taken","red"))
    		elif i not in y:
    			print(i+colored(" available","green"))
    			av.append(i)    			    	
def check8():
    for i in p8:
    	my_url=("https://www.instagram.com/%s/"%(i))
    	page_html=get(my_url)
    	page_soup=soup(page_html.text,"html.parser")
    	title=page_soup.title
    	for y in title:
    		if i in y:
    			print(i+colored(" taken","red"))
    		elif i not in y:
    			print(i+colored(" available","green"))
    			av.append(i)   			    	    			    	
def check9():
    for i in p9:
    	my_url=("https://www.instagram.com/%s/"%(i))
    	page_html=get(my_url)
    	page_soup=soup(page_html.text,"html.parser")
    	title=page_soup.title
    	for y in title:
    		if i in y:
    			print(i+colored(" taken","red"))
    		elif i not in y:
    			print(i+colored(" available","green"))
    			av.append(i)    			    	    			    	    			    	
def check10():
    for i in p10:
    	my_url=("https://www.instagram.com/%s/"%(i))
    	page_html=get(my_url)
    	page_soup=soup(page_html.text,"html.parser")
    	title=page_soup.title
    	for y in title:
    		if i in y:
    			print(i+colored(" taken","red"))
    		elif i not in y:
    			print(i+colored(" available","green"))
    			av.append(i)    			    	    			    	    			    	    			    	
    			    	    			    	    			    	    			    	    			    	    			    	
t1=Thread(target=check1)
t2=Thread(target=check2)
t3=Thread(target=check3)
t4=Thread(target=check4)
t5=Thread(target=check5)
t6=Thread(target=check6)
t7=Thread(target=check7)
t8=Thread(target=check8)
t9=Thread(target=check9)
t10=Thread(target=check10)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
list=["red","green","blue","yellow"]
o=random.choice(list)
print("Available usernames saved as available"+".txt")
print(colored(("""
██████╗░██╗░░░██╗
██╔══██╗╚██╗░██╔╝
██████╦╝░╚████╔╝░
██╔══██╗░░╚██╔╝░░
██████╦╝░░░██║░░░
╚═════╝░░░░╚═╝░░░

██╗░░░██╗███████╗██╗░░░██╗░█████╗░
╚██╗░██╔╝╚════██║╚██╗░██╔╝██╔══██╗
░╚████╔╝░░░░░██╔╝░╚████╔╝░███████║
░░╚██╔╝░░░░░██╔╝░░░╚██╔╝░░██╔══██║
░░░██║░░░░░██╔╝░░░░░██║░░░██║░░██║
░░░╚═╝░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝"""),o))
sys.stdout=open("available.txt","w")
for p in av:
	print(p)
sys.stdout.close()
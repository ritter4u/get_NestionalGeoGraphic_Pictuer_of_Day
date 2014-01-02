# -*- coding: utf-8 -*-
import sys, urllib.request, os,sqlite3
from bs4 import BeautifulSoup

url_prefix = "http://photography.nationalgeographic.com"

"""for debug"""
import pprint
"""for debug"""
def gethtml():
	page = urllib.request.urlopen(url_prefix+'/photography/photo-of-the-day/')
	html=page.read().decode("ascii","ignore")
	return html
def parseHtml(tmp):
	tmp=tmp.replace('\n','')
	tmp=tmp.replace('&laquo;','')
	tmp=tmp.replace('&raquo;','')

	data = {'html':tmp}
	soup=BeautifulSoup(tmp)
	#soup.prettify()
	data['caption']=soup.select("#caption").pop()
	data['publication_time']=soup.select("#caption > .publication_time").pop()
	data['title']=soup.select("#caption > h2").pop()
	data['credit']=soup.select("#caption > .credit").pop()
	data['previous']=soup.select(".prev > a").pop().attrs['href']
	data['download_link']=soup.select(".primary_photo img").pop().attrs['src']
	data['image_description']=soup.select(".primary_photo img").pop().attrs['alt']
	return data

def main():
	html=gethtml()
	data=parseHtml(html)
	print(data)


#def initDatabase():

#def store_to_database():
#	print('aa')

#def store_images():
#	print('bb')

if __name__ == "__main__":
	main()

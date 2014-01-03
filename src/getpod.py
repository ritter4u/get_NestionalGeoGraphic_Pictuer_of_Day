# -*- coding: utf-8 -*-
#TODO : exif 지원기능 추가
#TODO : DB sqllite3
#TODO : DB mysql
#TODO : DB mongodb
#TODO : app-engine
#TODO : django
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
	image=store_images(data)
	print(image)

	#img = Image.open("test.jpg")
	#exif = i._getexif()
	# decode exif using TAGS

#def initDatabase():

#def store_to_database():
#	print('aa')

def store_images(data):
	url=data['download_link']
	file_name = url.split('/')[-1]
	u = urllib.request.urlopen(url)
	meta = u.info()

	f = open(file_name, 'wb')
	f.write(u.read())
	f.close()
	return {'filename':file_name,'url':url}

if __name__ == "__main__":
	main()

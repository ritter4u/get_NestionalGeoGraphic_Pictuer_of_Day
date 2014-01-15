# -*- coding: utf-8 -*-
#TODO : class화 
#TODO : exif 지원기능 추가
#TODO : DB sqllite3
#TODO : DB mysql
#TODO : DB mongodb
#TODO : app-engine
#TODO : django
import sys, urllib.request, os,sqlite3
from bs4 import BeautifulSoup

def connectSqlite3():
	con = None
	try:
		con = sqlite3.connect('photo-of-the-day.db')
		cur = con.cursor()    
		cur.execute('SELECT SQLITE_VERSION()')  
		data = cur.fetchone() 
	except sqlite3.Error:
		print ("Error %s:" % e.args[0])
		sys.exit(1)
	finally:
		if con:
			con.close()
	return con

class PhotoOfTheDay():
	url_prefix = "http://photography.nationalgeographic.com"
	data=None
	info=None

	def getHtml(self,page_url=""):
		if(page_url==""):
			page_url=self.url_prefix+'/photography/photo-of-the-day/'
		page = urllib.request.urlopen(page_url)
		html=page.read().decode("ascii","ignore")
		data = {'html':html}
		self.data=data
		
	def parseHtml(self):
		data = self.data
		tmp=data['html']
		tmp=tmp.replace('\n','')
		tmp=tmp.replace('&laquo;','')
		tmp=tmp.replace('&raquo;','')
		soup=BeautifulSoup(tmp)
		#soup.prettify()
		data['caption']=soup.select("#caption").pop()
		data['publication_time']=soup.select("#caption > .publication_time").pop()
		data['title']=soup.select("#caption > h2").pop()
		data['credit']=soup.select("#caption > .credit").pop()
		data['previous']=soup.select(".prev > a").pop().attrs['href']
		data['download_link']=soup.select(".primary_photo img").pop().attrs['src']
		if(data['download_link'].find("http")==-1):
			data['download_link']=data['download_link'].replace("//","http://")
		data['image_description']=soup.select(".primary_photo img").pop().attrs['alt']
		self.data=data

	def store_images(self):
		data=self.data
		url=data['download_link']
		file_name = url.split('/')[-1]
		u = urllib.request.urlopen(url)
		meta = u.info()

		f = open(file_name, 'wb')
		f.write(u.read())
		f.close()
		self.info={'filename':file_name,'url':url}
#	def connectDB:
#		return ""

def main():
	pod = PhotoOfTheDay()
	pod.getHtml()
	pod.parseHtml()
	pod.store_images()
	print(pod.info)
	#pod.connectSqlite3()

	#
	#img = Image.open("test.jpg")
	#exif = i._getexif()
	# decode exif using TAGS

#def initDatabase():

#def store_to_database():
#	print('aa')

if __name__ == "__main__":
	main()


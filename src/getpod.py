# -*- coding: utf-8 -*-
# TODO : 세련된 class화
# TODO : exif 지원기능 추가
# TODO : DB sqllite3
# TODO : DB mysql
# TODO : DB mongodb
# TODO : using SQLAlchemy
# TODO : app-engine
# TODO : django
import sys, urllib.request, os, sqlite3
from bs4 import BeautifulSoup
from datetime import datetime

class DbSqlite3:
    db_name = 'photo-of-the-day.db'
    table_name = 'photo_of_the_day'
    data = None
    con = None

    def connectSqlite3(self):
        con = None
        targetTable = None
        try:
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            cur.execute('SELECT SQLITE_VERSION()')
            cur.execute(
                "CREATE TABLE " + self.table_name + "(Id INTEGER PRIMARY KEY,title TEXT,caption TEXT, publication_time TEXT,credit TEXT,previous TEXT,download_link TEXT,image_description TEXT,html TEXT, flag NUMERIC,created_at TEXT)")
            cur.execute("CREATE UNIQUE INDEX I_ID on" + self.table_name + "(id asc)")
            cur.execute("CREATE INDEX I_CREATED_AT on" + self.table_name + "(created_at asc)")
            cur.execute("CREATE INDEX I_FLAG_AT on" + self.table_name + "(flag asc)")
        except sqlite3.OperationalError:
            cur.execute("select count(*) from " + self.table_name)
        # finally:
        #     if con:
        #         con.close()
        self.con = con

    def getUnflaged(self):
	    data = self.data
	    cur = self.con.cursor()
	    cur.execute(
		    "select * from " + self.table_name + " where flag = '" + data['flag'] + "'")
	    result = cur.fatchall()
	    return result

    # def setFlag(self):
    #     data = self.data
    #     cur =  self.con.cursor()
    #     cur.execute(
    #         "select * from " + self.table_name + " where flag = '" + data['flag'] + "'")

    def insertData(self):
        data = self.data
        # print(self.data)
        cur = self.con.cursor()
        cur.execute(
            "select count(*) as cnt from " + self.table_name + " where download_link = '" + data['download_link'] + "'")
        result = cur.fetchone()
        if (result[0] <= 0):
            cur.execute("select max(id) from " + self.table_name)
            result = cur.fetchone()
            # print(result)
            '''print(data['caption'])
    		print(data['publication_time'])
	    	print(data['title'])
    		print(data['credit'])
    		print(data['previous'])
    		print(data['download_link'])
    		print(data['image_description'])'''

            data['flag'] = 0
            data['created_at'] = datetime.now()

            # print(data)
            cur.execute(
                "INSERT INTO " + self.table_name + "(title,caption,publication_time,credit,previous,download_link,image_description,html,flag,created_at) VALUES(?,?,?,?,?,?,?,?,?,?)",
                (str(data['title']), str(data['caption']), str(data['publication_time']), str(data['credit']),
                 str(data['previous']), str(data['download_link']), str(data['image_description']), str(data['html']),
                 int(data['flag']), str(data['created_at'])))
            self.con.commit()

class PhotoOfTheDay():
    url_prefix = "http://photography.nationalgeographic.com"
    data = None
    info = None

    def getHtml(self, page_url=""):
        if (page_url == ""):
            page_url = self.url_prefix + '/photography/photo-of-the-day/'
        page = urllib.request.urlopen(page_url)
        html = page.read().decode("ascii", "ignore")
        data = {'html': html}
        self.data = data

    def parseHtml(self):
        data = self.data
        tmp = data['html']
        tmp = tmp.replace('\n', '')
        tmp = tmp.replace('&laquo;', '')
        tmp = tmp.replace('&raquo;', '')
        soup = BeautifulSoup(tmp, "html.parser")
        # soup.prettify()
        data['caption'] = soup.select("#caption").pop()
        data['publication_time'] = soup.select("#caption > .publication_time").pop()
        data['title'] = soup.select("#caption > h2").pop()
        data['credit'] = soup.select("#caption > .credit").pop()
        data['previous'] = soup.select(".prev > a").pop().attrs['href']
        data['download_link'] = soup.select(".primary_photo img").pop().attrs['src']
        if (data['download_link'].find("http") == -1):
            data['download_link'] = data['download_link'].replace("//", "http://")
        data['image_description'] = soup.select(".primary_photo img").pop().attrs['alt']
        self.data = data

    def store_images(self):
        data = self.data
        url = data['download_link']
        file_name = url.split('/')[-1]
        u = urllib.request.urlopen(url)
        meta = u.info()
        directory = 'images'
        if not os.path.exists(directory):
            os.makedirs(directory)
        f = open('images/' + file_name, 'wb')
        f.write(u.read())
        f.close()
        self.info = {'filename': 'images/' + file_name, 'url': url}


# def connectDB:
#		return ""

def main():
<<<<<<< HEAD
    """
    :rtype : object
    """
    # print (sys.argv[0])
    pod = PhotoOfTheDay()
    pod.getHtml()
    pod.parseHtml()
    pod.store_images()
    print(pod.info)
    lite = DbSqlite3()
    lite.data = pod.data
    lite.connectSqlite3()
    # print(lite.data)
    lite.insertData()


# lite.prepareTables()
# pod.connectSqlite3()

#
# img = Image.open("test.jpg")
# exif = i._getexif()
# decode exif using TAGS

# def initDatabase():

# def store_to_database():
=======
	# print (sys.argv)
	# if sys.argv[1]=='once':
	# 	pod = PhotoOfTheDay()
	# 	pod.getHtml()
	# 	pod.parseHtml()
	# 	pod.store_images()
	# 	print(pod.info)
	# 	lite=Sqlite3()
	# 	lite.data=pod.data
	# 	lite.connectSqlite3()
	# 	#print(lite.data)
	# 	lite.insertData()
	# 	#lite.prepareTables()
	# 	#pod.connectSqlite3()
	# 	#
	# 	#img = Image.open("test.jpg")
	# 	#exif = i._getexif()
	# 	# decode exif using TAGS
	# else:
	print ('all')
	pod = PhotoOfTheDay()
	pod.getHtml()
	pod.parseHtml()
	# pod.store_images()
	print(pod.info)
	lite=Sqlite3()
	lite.data=pod.data
	lite.connectSqlite3()
	#print(lite.data)
	lite.insertData()
	# lite.selectOneData()

#def initDatabase():

#def store_to_database():
>>>>>>> develop
#	print('aa')

if __name__ == "__main__":
    main()

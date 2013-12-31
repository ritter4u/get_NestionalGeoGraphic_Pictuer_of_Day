# -*- coding: utf-8 -*-
import sys, urllib.request, os
from bs4 import BeautifulSoup


"""for debug"""
import pprint
"""for debug"""
def main():
	page = urllib.request.urlopen('http://photography.nationalgeographic.com/photography/photo-of-the-day/')
	html=page.read().decode("ascii","ignore")
	html=html.encode("utf8","xmlcharrefreplace")
	html=str(html)
	soup=BeautifulSoup(html)
	#soup.prettify()
	print (soup.select("#caption"))
	print (soup.select("#caption"))
	print (soup.select("#caption > .publication_time"))
	print (soup.select("#caption > h2"))
	print (soup.select("#caption > .credit"))
	print (soup.select("#caption > p"))
	list1=soup.select(".download_link > a")
	for i in list1:
		print (i.attrs['href'])
	list2= soup.select(".prev > a")
	for i2 in list2:
		print (i2.attrs['href'])
if __name__ == "__main__":
	main()

# -*- coding: utf-8 -*-
import sys, urllib.request, os
from bs4 import BeautifulSoup
"""for debug"""
import pprint
"""for debug"""
def main():
	page = urllib.request.urlopen('http://photography.nationalgeographic.com/photography/photo-of-the-day/')
	html=page.read()
	soup=BeautifulSoup(html)
	print (soup.prettify())
	#pp = pprint.PrettyPrinter(indent=4)
	#pp.pprint(page)
	
	#sys.exit()
	
if __name__ == "__main__":
	main()

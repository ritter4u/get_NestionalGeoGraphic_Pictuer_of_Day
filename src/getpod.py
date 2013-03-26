# -*- coding: utf-8 -*-
import sys, urllib.request, os

"""for debug"""
import pprint
"""for debug"""

def main():
	page = urllib.request.URLopener('http://photography.nationalgeographic.com/photography/photo-of-the-day/')
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(page)
	
	# sys.exit()
	
if __name__ == "__main__":
    main()

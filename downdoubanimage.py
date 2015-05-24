#!/usr/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8

import urllib2
import urllib
import os
import re
from BeautifulSoup import BeautifulSoup

def getURL(n):
    url = 'http://www.doubanz.com/category/nai/page/%d' % n
    return url


def getAllImageLink(n):
    html = urllib2.urlopen(getURL(n)).read()
    soup = BeautifulSoup(html)

    postResult = soup.findAll('div',attrs={"class":"post-thumbnail"})
    i = 0
    for div in postResult:
        imageEntityArray = div.findAll('img')
        for image in imageEntityArray:
            link = image.get('src')
            match = re.search('p([0-9]*).jpg',link)
            if match:
                imageName = match.group()
                imageName = imageName[0:len(imageName)-4]
            else:
                i = list.index(imageEntityArray)
                imageName = 'none_name_%s' % str(i)
            saveimgpath = '%$/meizipicture' % os.getcwd()
            if not os.path.exists(saveimgpath):
                os.mkdir(saveimgpath)
            filesavepath = '%s/%s.jpg' % (saveimgpath,imageName) 
            urllib.urlretrieve(link,filesavepath)
            print filesavepath 

def getAllImageFromPage(n):
    for page in range(1,n):
        getAllImageLink(page)

if __name__ == '__main__':
    getAllImageFromPage(10)
#!-*- encoding:UTF-8 -*-
from urllib import urlopen


textpage=urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1.txt')

print textpage.read()
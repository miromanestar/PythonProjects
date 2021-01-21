import csv
import codecs #For importing HTML
from bs4 import BeautifulSoup #For parsing HTML
from furl import furl #For... parsing HTML

file = codecs.open('raw.html', 'r') #Get HTML file text

page = BeautifulSoup(file, 'lxml')
name = page.title.text

questions = page.find_all('div', class_='que').find('p')

print(name)
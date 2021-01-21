import csv
import codecs #For importing HTML
from bs4 import BeautifulSoup #For parsing HTML
from furl import furl #For... parsing HTML

file = codecs.open('raw.html', 'r') #Get HTML file text

page = BeautifulSoup(file, 'lxml')
name = page.title.text

qContainers = page.find_all('div', class_='que')

questions = []
answers = []
for question in qContainers:
    qText = question.find('div', class_='content').find('div', class_='formulation').find('p').text
    questions.append(qText)

print(name)
import csv
import codecs #For importing HTML
from bs4 import BeautifulSoup #For parsing HTML
from furl import furl #For... parsing HTML

#Get fill-in-the-blank questions and answers
def get_blanks(input):
    qa = [''] * 2
    for item in input.find('p').contents:
        if isinstance(item, str):
            item = item.replace(u'Â\xa0', u' ') #Replace non-breaking space with proper space
            qa[0] += item
        else:
            qa[0] += '____'

            if qa[1] != '':
                qa[1] += separator + item.find('input').attrs['value']
            else:
                qa[1] += item.find('input').attrs['value']
        
    return qa

#Get questions which use a dropdown
def get_dropdowns(input):
    qa = [''] * 2
    qa[0] = input.find('div', class_='qtext').text

    for item in input.find_all('tr'):
        qa[0] += '<br /><br />' + item.find('td', class_='text').text
        
        if qa[1] == '':
            qa[1] += item.find('option', selected='selected').text
        else:
            qa[1] += separator + item.find('option', selected='selected').text
    return qa

#Get questions which are true/false
def get_tf(input):
    qa = [''] * 2
    qa[0] = input.find('div', class_='qtext').text
    qa[1] = input.find('div', class_='answer').find('label').text

    return qa

#Get question if it's asking for a list
def get_list(input):
    qa = [''] * 2
    qa[0] = input.find('p').text
    for item in input.find_all('li'):
        if qa[1] != '':
            qa[1] += separator + item.find('input').attrs['value']
        else:
            qa[1] += item.find('input').attrs['value']

file = codecs.open('raw.html', 'r') #Get HTML file text

page = BeautifulSoup(file, 'lxml')
name = page.title.text.replace(' ', '_')

separator = ', '

qContainers = page.find_all('div', class_='que')

q_a = []

for count, question in enumerate(qContainers):
    qItem = question.find('div', class_='content').find('div', class_='formulation') #Question item container

    if qItem.find('p', recursive=False): #If it's a "fill-in-the-blank question"
        q_a.append(get_blanks(qItem))
    elif qItem.find('td'): #If it's a dropdown question
        q_a.append(get_dropdowns(qItem))
    elif qItem.find('input', type='radio'): #If it's a true/false question
        q_a.append(get_tf(qItem))
    else: #If it's a question asking for a list BROKEN
        q_a.append(qItem)
    
    q_a[count][0] = str(count + 1) + '. ' + q_a[count][0]

with open('output.csv', mode='w') as output:
    writer = csv.writer(output)
    writer.writerow(['Questions', 'Answers'])
    writer.writerows(q_a)
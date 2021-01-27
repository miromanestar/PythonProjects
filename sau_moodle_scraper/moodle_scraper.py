import csv
import codecs #For importing HTML
from bs4 import BeautifulSoup #For parsing HTML
from furl import furl #For... parsing HTML

#Get fill-in-the-blank questions and answers
def get_multianswer(input):
    qa = [''] * 2
    for item in input.find('p').contents:
        if isinstance(item, str):
            item = item.replace(u'Â\xa0', u' ') #Replace non-breaking space with proper space
            qa[0] += item
        else:
            qa[0] += '____'

            if item.name != 'span':
                continue

            if qa[1] != '':
                qa[1] += separator + item.find('input').attrs['value']
            else:
                qa[1] += item.find('input').attrs['value']
        
    return qa

#Get questions which use a dropdown
def get_match(input):
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
def get_truefalse(input):
    qa = [''] * 2
    qa[0] = input.find('div', class_='qtext').text
    qa[1] = input.find('input', checked='checked').find_next_sibling('label').text

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

    return qa

def get_multichoice(input):
    qa = [''] * 2
    qa[0] = input.find('div', class_='qtext').text

    for item in input.find_all('input', checked='checked'):
        label = item.find_next_sibling('div')
        if qa[1] != '':
            qa[1] += separator + label.find('div').text
        else:
            qa[1] += label.find('div').text

    return qa


file = codecs.open('raw.html', 'r') #Get HTML file text

page = BeautifulSoup(file, 'lxml')
name = page.title.text.replace(' ', '_')

separator = ', '

qContainers = page.find_all('div', class_='que')

q_a = []

for count, question in enumerate(qContainers):
    qItem = question.find('div', class_='content').find('div', class_='formulation') #Question item container
    classList = question.attrs['class']

    if 'multianswer' in classList: #If it's a "fill-in-the-blank question"
        q_a.append(get_multianswer(qItem))
    elif 'match' in classList: #If it's a dropdown question
        q_a.append(get_match(qItem))
    elif 'truefalse' in classList: #If it's a true/false question
        q_a.append(get_truefalse(qItem))
    elif 'multichoice' in classList:
        q_a.append(get_multichoice(qItem))
    else: #If you've reached this point, it's going to break
        q_a.append(qItem)
    
    q_a[count][0] = str(count + 1) + '. ' + q_a[count][0]

with open('output.csv', mode='w') as output:
    writer = csv.writer(output)
    writer.writerow(['Questions', 'Answers'])
    writer.writerows(q_a)
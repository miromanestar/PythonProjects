import requests
import csv
import random
from time import sleep

nameEmails = []
with open('people.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        nameEmails.append({'name': row[0], 'email': row[1]})

print(nameEmails)

rockyou = open('rockyou.txt', 'rb').read().decode("utf-8", "replace")

lines = rockyou.splitlines()

session = requests.Session()

headers = {"Origin":"http://scotnpatti.us","Cache-Control":"max-age=0","Accept":"text/html,application/xhtml xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4202.0 Safari/537.36 autochrome/green","Referer":"http://scotnpatti.us/dra.cs.southern.edu/NetworkConfiguration/OpenVpnConfiguration.html","Accept-Language":"en-US,en;q=0.9","Proxy-Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded"}
while True:
    person = random.choice(nameEmails)
    password_old = random.choice(lines)
    password_new = random.choice(lines)

    paramsPost = {
        "name": person['name'],
        "password2": password_new,
        "password1": password_old,
        "password3": password_new,
        "email": person['email']
    }

    

    response = session.post("http://scotnpatti.us/dra.cs.southern.edu/NetworkConfiguration/mail_form.php", data=paramsPost, headers=headers)
    
    print(paramsPost, response.status_code)
    print(response.content)

    sleep(random.randint(1,7))

#print("Status code:   %i" % response.status_code)
#print("Response body: %s" % response.content)

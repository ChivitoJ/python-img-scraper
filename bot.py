import requests
from bs4 import BeautifulSoup
import os

url = 'https://simple.wikipedia.org/wiki/List_of_U.S._states_by_date_of_admission_to_the_Union'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

tds = soup.find_all('td')
state_names = [td.find('a').text for td in tds if td.find('a', {'title': True}) and not td.find('span', {'class': 'flagicon'})]
flags = soup.find_all('img', {'class': 'mw-file-element'})

states = []

for i in range(len(state_names)):
    states.append({
        'name': state_names[i]
    })
    print(state_names[i])

for i in flags:
    name = states[flags.index(i)]['name']
    img_url = i['src']
    with open(name + '.png', 'wb') as f:
        f.write(requests.get('https:'+img_url).content)
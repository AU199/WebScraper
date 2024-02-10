from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd

service = webdriver.ChromeService()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

light_green = []
light_Tan = []
School = "Cincinnati Sycamore"
players = []
positions = []
times = []
driver.get('https://www.swimmeet.com/swdistrict24/mason/psych-sheets/boys-d1-50-freestyle.html')


content = driver.page_source
soup = BeautifulSoup(content, features= "html.parser")
for element in soup.findAll('div', attrs= {'id': 'results'}):
    light_green_items = element.find_all('tr', attrs = {'class':"lightGreen"})
    light_tan_item = element.find_all('tr', attrs = {'class':"lightTan"})


    light_green = light_green_items
    light_tan = light_tan_item

for element in light_green:


    player = element.find('td', attrs = {'class':"name"}).string
    position = element.find('td', attrs = {'class':"rank"}).string
    time = element.find('td', attrs = {'class': "time"}).string
    team_d = element.find('td', class_='team')
    team = ' '.join(team_d.stripped_strings)

    if team == School:
        
        print(player, position, time,team)
        players.append(player)
        positions.append(position)
        times.append(time)


for element in light_tan:

    player = element.find('td', attrs = {'class':"name"}).string
    position = element.find('td', attrs = {'class':"rank"}).string
    time = element.find('td', attrs = {'class': "time"}).string
    team_d = element.find('td', class_='team')
    team = ' '.join(team_d.stripped_strings)


    if team == School:
        
        print(player, position, time,team)
        players.append(player)
        positions.append(position)
        times.append(time)

df = pd.DataFrame({'player': players, 'position': positions, 'time': times} )
df.to_csv('players.csv',index=False, encoding= 'utf-8')
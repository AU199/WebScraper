from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

service = webdriver.ChromeService()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


websites_to_get = ['https://www.swimmeet.com/swdistrict24/mason/psych-sheets/boys-d1-100-freestyle.html', 'https://www.swimmeet.com/swdistrict24/mason/psych-sheets/boys-d1-50-freestyle.html']
players = []
positions = []
times = []
event = []

for i in range(len(websites_to_get)):
    print(i)
    light_green = []
    light_Tan = []
    School = "Cincinnati Sycamore"

    driver.get(websites_to_get[i])

    content = driver.page_source
    soup = BeautifulSoup(content, features= "html.parser")

    event_name_getter = soup.find('div', attrs= {'id':'eventName'})
    event_name = event_name_getter['value']
    print(event_name)
    
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
        
            players.append(player)
            positions.append(position)
            times.append(time)
            event.append(event_name)


    for element in light_tan:

        player = element.find('td', attrs = {'class':"name"}).string
        position = element.find('td', attrs = {'class':"rank"}).string
        time = element.find('td', attrs = {'class': "time"}).string
        team_d = element.find('td', class_='team')
        team = ' '.join(team_d.stripped_strings)


        if team == School:
            players.append(player)
            positions.append(position)
            times.append(time)
            event.append(event_name)
    print(event)
print(len(players),len(positions),len(times),len(event))
df = pd.DataFrame({'player': players, 'position': positions, 'time': times, 'event' : event} )
df.to_csv('players.csv',index=False, encoding= 'utf-8')
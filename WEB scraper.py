from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import string

service = webdriver.ChromeService()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
file = open("events.txt","r")
events_to = []
for line in file.readlines():
    if line != "\n":
        events_to.append(line)
main_website = 'https://www.swimmeet.com/swdistrict24/qualifiers/boys-d1'
players = []
positions = []
times = []
events = []

for i in range(len(events_to)):
    light_green = []
    light_Tan = []
    School = "Cincinnati Sycamore"
    event = events_to[i].split(' ')
    fixed_event = ''
    item_to_fix = event[1]
    for i in range(len(event[1])):
        if item_to_fix[i] in string.ascii_letters:
            fixed_event += item_to_fix[i]

    event[1] = fixed_event
    website = (main_website+'-'+f'{event[0]}'+'-'f'{event[1]}'+'.'+'html')



    driver.get(website)

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
            events.append(event_name)


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
            events.append(event_name)
    print(event)
players.append("\n")
players.append("CREATOR: AKUL GUMUDAVALLI")

for i in range(len(players)-len(positions)):
    positions.append("")
    times.append("")
    events.append("")
print(len(players),len(positions),len(times),len(events))
data_frame = pd.DataFrame({'player': players, 'position': positions, 'time': times, 'event' : events} )
data_frame.to_csv('players.csv',index=False, encoding= 'utf-8')

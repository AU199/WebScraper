from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd

service = webdriver.ChromeService()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

light_green = []
light_Tan = []

players = []
positions = []
times = []
driver.get('https://www.swimmeet.com/swdistrict24/mason/psych-sheets/boys-d1-50-freestyle.html')


content = driver.page_source
soup = BeautifulSoup(content, features= "html.parser")
for element in soup.findAll('div', attrs= {'id': 'results'}):
    light_green_items = element.find_all('tr', attrs = {'class':"lightGreen"})
    
    position = element.find('tr', attrs = {'class':"lightTan"})



    light_green.append(light_green_items)
    light_Tan.append(position)

print("light green", light_green)
print(len(light_green))

for element in light_green:
    print(element)

    player = element.find('td', attrs = {'class':"name"}).string
    position = element.find('td', attrs = {'class':"rank"}).string
    time = element.find('td', attrs = {'class': "time"}).string

    print(player, position, time)


df = pd.DataFrame({'player': players, 'position': positions, 'time': times} )
df.to_csv('players.csv',index=False, encoding= 'utf-8')
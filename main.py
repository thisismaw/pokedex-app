import requests
import pandas as pd
from bs4 import BeautifulSoup as bs4

pokeIcon = []  # okay
pokeNum = []  # okay
pokeName = []  # okay
PokeFirstType = [] # okay
PokeSecondType = [] # okay
totalStats = []
HP = []
Atk = []
Defense = []
SpAtk = []
SpDef = []
Speed = []
pages = []

url = 'https://pokemondb.net/pokedex/all'
pages.append(url)

for item in pages:
    page = requests.get(item)
    soup = bs4(page.text, 'html.parser')
    getPokeNum = soup.find_all('tbody')
    for i in getPokeNum:
        findTr = i.find_all('tr')
        for num in findTr:
            getNum = num.find('span', class_="infocard-cell-data")
            pokeDexNumber = getNum.getText()
            pokeNum.append(pokeDexNumber)
        getIconCoord = soup.find_all('span', class_="infocard-cell-img")
        for icon in getIconCoord:
            getSpanIcon = icon.find('span', class_="img-fixed icon-pkmn")
            grabSpanIcon = str(getSpanIcon['data-src'])
            pokeIcon.append(grabSpanIcon)
        for name in findTr:
            getName = name.find('a', class_='ent-name')
            grabPokeName = getName.getText()
            pokeName.append(grabPokeName)
        for type in findTr:
            getType = type.find('td', class_="cell-icon")
            firstType = type.find('a', class_="type-icon")
            getFirstType = firstType.getText()
            secondType = firstType.find_next_sibling('a')
            getSecondType = secondType.getText() if secondType else "None"
            print(getFirstType + " " + getSecondType)



# data = {"Number" : pokeNum , "Name" : pokeName , "Type" : pokeType , "Icon" : pokeIcon}
# df = pd.DataFrame(data=data)
# df.to_excel("D:/pokemonDB/pokemondb.xlsx", index=False)

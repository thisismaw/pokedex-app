import requests
import pandas as pd
from bs4 import BeautifulSoup as bs4

pokeIcon = []  # okay
pokeNum = []  # okay
pokeName = []  # okay
PokeFirstType = []  # okay
PokeSecondType = []  # okay
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
            # can be improved
            getName = name.find('span', class_="img-fixed icon-pkmn")
            getPokeName = str(getName['data-alt'])
            finalGetName = getPokeName.replace('icon', '')
            pokeName.append(finalGetName)
        for gettype in findTr:
            getType = gettype.find('td', class_="cell-icon")
            firstType = gettype.find('a', class_="type-icon")
            getFirstType = firstType.getText()
            secondType = firstType.find_next_sibling('a')
            getSecondType = secondType.getText() if secondType else "None"
            PokeFirstType.append(getFirstType)
            PokeSecondType.append(getSecondType)
        for stats in findTr:
            grabTotalStats = stats.find('td', class_="cell-total")
            getTotalStats = grabTotalStats.getText()
            totalStats.append(getTotalStats)
            grabHP = grabTotalStats.find_next_sibling('td')
            getHP = grabHP.getText()
            HP.append(getHP)
            grabAtk = grabHP.find_next_sibling('td')
            getAtk = grabAtk.getText()
            Atk.append(getAtk)
            grabDef = grabAtk.find_next_sibling('td')
            getDef = grabDef.getText()
            Defense.append(getDef)
            grabSpAtk = grabDef.find_next_sibling('td')
            getSpAtk = grabSpAtk.getText()
            SpAtk.append(getSpAtk)
            grabSpDef = grabSpAtk.find_next_sibling('td')
            getSpDef = grabSpDef.getText()
            SpDef.append(getSpDef)
            grabSpd = grabSpDef.find_next_sibling('td')
            getSpd = grabSpd.getText()
            Speed.append(getSpd)

data = {"Icon": pokeIcon, "Number": pokeNum, "Name": pokeName, "First Type": PokeFirstType,
        "Second Type": PokeSecondType, "Total Stats": totalStats,
        "HP": HP, "Attack": Atk, "Defense": Defense, "Sp.Atk": SpAtk, "Sp.Def": SpDef, "Speed": Speed}
df = pd.DataFrame(data=data)
df.to_excel("D:/pokemonDB/pokemondb.xlsx", index=False)

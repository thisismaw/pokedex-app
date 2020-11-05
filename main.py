import requests
import pandas as pd
from bs4 import BeautifulSoup as bs4

openWebName = [] #okay
pokeIcon = []  # okay
pokeNum = []  # okay
pokeName = []  # okay
PokeFirstType = []  # okay
PokeSecondType = []  # okay
totalStats = []  # okay
HP = []  # okay
Atk = []  # okay
Defense = []  # okay
SpAtk = []  # okay
SpDef = []  # okay
Speed = []  # okay
pages = []  # okay
pokeArtWork = [] # okay
species = [] #okay
height = []
weight = []
pageToScrape = 1
url = 'https://pokemondb.net/pokedex/all'
pokeWebPage = []
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
        for name in findTr:
            grabWebName = name.find('a', class_="ent-name")
            grabHTML = 'https://pokemondb.net/' + str(grabWebName['href'])
            openWebName.append(grabHTML)

for pokePage in openWebName:
    getPokePage = requests.get(pokePage)
    soup = bs4(getPokePage.text,'html.parser')
    grabImg = soup.find_all('div', class_="grid-col span-md-6 span-lg-4 text-center")
    getVitals = soup.find('table',class_= "vitals-table")
    for items in grabImg:
        getImg = items.find('a')
        saveImg = str(getImg['href'])
        pokeArtWork.append(saveImg)
        getImg = items.find('a')
        saveImg = str(getImg['href'])
        pokeArtWork.append(saveImg)
    for pokemon in getVitals.find_all('tbody'):
        pokeNum = pokemon.find('tr')
        getDataFirst = pokeNum.find('td')
        grabSecond = pokeNum.find_next_sibling('tr')
        grabSpecies = grabSecond.find_next_sibling('tr')
        pokeSpecies = grabSpecies.find('td').text
        species.append(pokeSpecies)
        grabHeight = grabSpecies.find_next_sibling('tr')
        pokeHeight = grabHeight.find('td').text
        height.append(pokeHeight)
        grabWeight = grabHeight.find_next_sibling('tr')
        pokeWeight = grabWeight.find('td').text
        weight.append(pokeWeight)

data = {"Icon": pokeIcon, "Number": pokeNum, "Name": pokeName, "First Type": PokeFirstType,
"Second Type": PokeSecondType, "Total Stats": totalStats,  "HP": HP, "Attack": Atk, "Defense": Defense
    , "Sp.Atk": SpAtk, "Sp.Def": SpDef, "Speed": Speed, "Species" : species , "Height" : height , "Weight" : weight , "Image" : pokeArtWork}
df = pd.DataFrame(data=data)
df.to_csv("D:/pokemonDB/pokemondb.csv", index=False)

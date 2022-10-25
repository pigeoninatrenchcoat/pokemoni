import requests, json

raw = 'https://raw.githubusercontent.com/yorkcshub/Miscellanous/master/effectiveness.json'
data = requests.get(raw)
dataJson = json.loads(data.text)

bodiky = {
    "Normal": {}, "Fire": {}, "Water": {}, "Electric": {}, "Grass": {}, "Ice": {}, "Fighting": {}, "Poison": {}, "Ground": {}, "Flying": {}, "Psychic": {}, "Bug": {}, "Rock": {}, "Ghost": {}, "Dragon": {}, "Dark": {}, "Steel": {}, "Fairy": {}
}

def hodnoty(na):
    return {"super effective":2.0, "normal effective":1.0, "not very effective":0.5, "no effect":0.0}[na]

def vypocitaj(a, b):
    my = 0.0
    for moj_poke in a:
        if " " in moj_poke:
            moj_poke = moj_poke.split(" ")
            for jeho_poke in b:
                if " " in jeho_poke:
                    jeho_poke = jeho_poke.split(" ")
                    my += max(bodiky[moj_poke[0]][jeho_poke[0]]*bodiky[moj_poke[0]][jeho_poke[1]], bodiky[moj_poke[1]][jeho_poke[0]]*bodiky[moj_poke[1]][jeho_poke[1]])
                else: my += max(bodiky[moj_poke[0]][jeho_poke], bodiky[moj_poke[1]][jeho_poke])
        else:
            for jeho_poke in b:
                if " " in jeho_poke:
                    jeho_poke = jeho_poke.split(" ")
                    my += bodiky[moj_poke][jeho_poke[0]]*bodiky[moj_poke][jeho_poke[1]]
                else: my += bodiky[moj_poke][jeho_poke]
    return round(my,1)

def citatelne():
    for power, pokemons in dataJson.items():
        for pokemon, against in pokemons.items():
            for one in against:
                bodiky[pokemon].update({one:hodnoty(power)})

def attack(nasi, vasi, zoz):
    global bodiky
    tym_1, tym_2 = zoz.split(",")[:nasi:],zoz.split(",")[nasi::]
    my, oni = vypocitaj(tym_1, tym_2), vypocitaj(tym_2, tym_1)
    if my > oni: vys = "ME" 
    elif my == oni: vys = "EQUAL"
    else: vys= "FOE"
    return my,oni,vys

citatelne()

print(attack(2,6,"Psychic Dark,Fire,Ghost,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug"))


# Diccionarios
# {"Key": "value", "key": "value"}
team ={
    "name": "City",
    "country": "England",
    "campions": 1,
    "players": ['haland', 'grealinsh']
    }

print(type(team))
print(team)
print(team("name"))
print(team["players"])
team["players"].append("kevin")
team["name"] = "Manchester city"
team["leage"] = "Premiere league"
print(team)


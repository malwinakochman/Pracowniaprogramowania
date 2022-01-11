import json
film = {
    "Title": "The Fast and The Furious",
    "Director": "Vin Diesel",
    "Year": 2001,
    "Country": "USA",
    "Studio": "Universal Studios",
    }
with open("favourite.json", "w") as file:
    json.dump(film, file, indent = 4)
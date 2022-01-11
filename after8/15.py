import json
student = {
    "Imie": "Jan",
    "Nazwisko": "Kowalski",
    "Wiek": 19,
    "Rok urodzenia": 2002,
    "Średnia ocen": 5.2,
    "Posiadanie zwierzęcia": True,
}

with open("student1.json", "w") as file:
    json.dump(student, file, indent = 4)
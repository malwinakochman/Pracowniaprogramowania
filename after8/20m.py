import json

with open("students.json") as file:
    students = json.load(file)
   
with open("limited.json", "w") as file:
    studentsLimited = []
    for i in students:
        limitedDane = {
                "first_name": i["first_name"],
            "last_name": i["last_name"],
            "student_card": i["student_card"],
        }
        
        
        studentsLimited.append(limitedDane)
    file.write(f"{json.dumps(studentsLimited, indent=2)}\n")
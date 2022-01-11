film_titles = ["Szybcy i Wściekli", "Incepcja", "Boże ciało", "Kraina lodu", "Noce i dnie"]
file = open("films.txt", "w")
for i in film_titles:
    file.write(i)
    file.write("\n")

file.close()

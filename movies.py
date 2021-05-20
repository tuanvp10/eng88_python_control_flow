# Movie Ratings Task

while True:
    age = int(input("Hello!, how old are you? "))
    if age < 3:
        print("Everyone can watch.")
    elif age >= 3 and age <= 12:
        print("General viewing, but some scenes may be unsuitable for young children.")
    elif age >= 12 and age <= 14:
        print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
    elif age >=15 and age <=18:
        print("No one younger than 15 may see a 15 film in a cinema.")
    elif age >= 18:
        print("No one younger than 18 may see an 18 film in a cinema.")
    else:
        break

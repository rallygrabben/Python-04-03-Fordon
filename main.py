import fordon
import personbil
import lastbil


looping = True

# Personbilar
volvo_red = personbil.personbil("Volvo", "röd", 200)
opel_red = personbil.personbil("Opel", "röd", 250)
ferrari_gul = personbil.personbil("Ferrari", "röd", 30)

# Lastbilar
scania_blue = lastbil.lastbil("Scania", "Blå", 3440)
volvo_grey = lastbil.lastbil("Scania", "Grå", 5000)


# Skapar Lista
PersonbilArray = [volvo_red, opel_red, ferrari_gul]
LastbilsArray = [scania_blue, volvo_grey]


while looping == True:
    


    go = input(f"\n Vill du lista fordon igen? (j/n): ")
    print(\n)
    if go == ("n"):
        break

print(volvo_red.color)

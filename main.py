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
volvo_grey = lastbil.lastbil("Volvo", "Grå", 5000)


# Skapar Lista
PersonbilArray = [volvo_red, opel_red, ferrari_gul]
LastbilsArray = [scania_blue, volvo_grey]

def print_fordonslista(fordonslista):

    for ett_fordon in fordonslista:
        if (isinstance(ett_fordon, lastbil.lastbil)):
            print(f"\n\t{ett_fordon.fabrikat} \n\t\tFärg: {ett_fordon.color} \n\t\tFlak Volym: {ett_fordon.flakvolym} Ton")

        elif (isinstance(ett_fordon, personbil.personbil)):
            print(f"\n\t{ett_fordon.fabrikat} \n\t\tFärg: {ett_fordon.color} \n\t\tBagage Volym: {ett_fordon.bagagevolym} L")


while looping == True:

    val_av_fordon = input("\nVilket typ av fordon vill du visa? \n\t1.\tLastbilar \n\t2. \tPersonbilar\n\t\t:")


    if (val_av_fordon == "1"):
        print("\n\n\n\n\nLista med lastbilar \n\n")
        print_fordonslista(LastbilsArray)
    elif (val_av_fordon == "2"):
        print("\n\n\n\n\nLista med personbilar \n\n")
        print_fordonslista(PersonbilArray)
    else:
        print("Yo kanske ska skriva en av siffrorna??")


    go = input("\n Vill du lista fordon igen? (j/n): ")
    
    print("--------------------------------")
    print(f"\nKlasser och Arv")

   

    if (go == "n"):
        break


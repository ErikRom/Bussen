# ------------------------------- Information --------------------------------- #
"""
Titel: Bussen
Författare: Erik och Jack
Datum: 2022-11-16
Det här är ett program för hantering av passagerare på en buss. Programmet
lagrar passagerare i en lista.
"""
# ------------------------- Biblioteksimportering ----------------------------- #
import random as rand #  importerar en funktion för att kunna skapa funktioner som slumpar fram b.la åldrar och namn.
import time
# ---------------------------------- listor ----------------------------------- #
namn_lista_kille = ["Jack", "Erik", "Bob", "Leo", "Nikodemus", "Samuel", "David", "Lucas", "Marcus", "Noah",
                    "Simon", "Harley", "Lewis", "John", "Gus", "Robin", "Jakob", "Chris", "Jimmy",
                    "Clay", "Gus", "Melvin", "Isak", "Candide", "Joe", "Kung", "Kingkong", "Hunk", "Hnulk"]

namn_lista_tjej = ["Anna", "Abigale", "Magdalena", "Marie", "Kunigunda", "Candice", "Birgitt",
                   "Britt-marie", "Anna-lena", "Elise", "Jeanette", "Åsa", "Lara", "Linnea", "Annet", "Hanna",
                   "Elsa", "Helena", "Jana", "Athena"]
buss = []
ålder_lista = []
kön_lista_kille = ["kille", "kille", "kille", "kille", "kille", "kille", "attackhelikopter"]  # fler exemplar av könet för att förändra oddsen att
kön_lista_tjej = ["tjej", "tjej", "tjej", "tjej", "tjej", "tjej", "attackhelikopter"]  # få tjej/kille instället för attackhelikopter

# Person är en klass för att representera personer i bussen. Varje objekt
# som skapas ur klassen har ett namn och en ålder, samt metoder för att returnera
# alternativt modifiera respektive attribut
# ---------------------------- Klassdefinitioner ------------------------------ #
class Person():
    def __init__(self, namn, ålder, kön):
        self.namn = namn
        self.ålder = ålder
        self.kön = kön
    # Strängrepresentation av objektet.
    def __str__(self):
        if self.kön == "kille":
            pronomen = "han"
        if self.kön == "tjej":
            pronomen = "hon"
        return f"Det här är {self.namn}, {pronomen} är {self.ålder} år gammal och är en {self.kön}."

    # Setters
    def set_namn(self, nytt_namn):
        self.namn = nytt_namn

    def set_ålder(self, ny_ålder):
        self.ålder = ny_ålder

    def set_kön(self, nytt_kön):
        self.kön = nytt_kön

    # Getters
    def get_namn(self):
        return self.namn

    def get_ålder(self):
        return self.ålder

    def get_kön(self):
        return self.kön

# ------------------------- Funktionsdefinitioner ---------------------------- #

# Lägger till en ny person i bussen.
def plocka_upp():
    if len(buss) == 25:
        print("Bussen är full, någon behöver gå av.")
    else:
        try:
            antal_upp = int(input("Hur många passagerare vill du plocka upp?" "\n-> "))
            for räknare in range(antal_upp):
                nummer = rand.randint(1,2)
                if nummer == 1:
                    namn = rand.choice(namn_lista_tjej) #slumpat namn
                    namn_lista_tjej.remove(namn)  # tar bort namn från slumpen så alla blir unika
                    kön = rand.choice(kön_lista_tjej)
                elif nummer == 2:
                    namn = rand.choice(namn_lista_kille)  # slumpat namn1
                    namn_lista_kille.remove(namn)  # tar bort namn från slumpen så alla blir unika
                    kön = rand.choice(kön_lista_kille)

                ålder = rand.randint(1, 120) #slumpad ålder
                person = Person(namn, ålder, kön)
                buss.append(person)
        except Exception:
            print("Ogiltig inmatning, vänligen försök igen.")
        else:
            print(f"Plockade upp {antal_upp} personer.")

# Avlägsnar en person från bussen.
def gå_av():
    hur_många_av = int(input("Hur många passagerare vill du ska gå av?" "\n-> "))
    if hur_många_av == 1:
         vem_av = int(input("Vem vill du ska gå av(nummer)?" "\n-> "))
         buss.pop(vem_av)
         print(f"{vem_av} gick av.")
    if hur_många_av > 1:
        for passagerare in buss:
                vilka_av = int(input("Vilka vill du ska gå av?" "\n1.-> "))
        buss.pop(vilka_av)
        print(f"{vilka_av} gick av")

# Listar alla passagerare på bussen.
def skriv_ut():
    i = 0
    for person in buss:
        print(i, person.namn, person.ålder, person.kön)
        i += 1
# Skriver ut den sammanlagda åldern på passagerarna.
def sammanlagd_ålder():
    ålder = 0
    for person in buss:
        ålder += person.ålder
    print(f"Den sammanlagda åldern av passagerarna är {ålder}")

# Skriver ut medelåldern på passagerarna i bussen.
def medel_ålder():
    ålder_medel = 0
    try:
        for person in buss:
            ålder_medel += person.ålder
        medelålder = ålder_medel / len(buss)
    except Exception:
        print("Det finns inga passagerare på bussen.")
    else:
        print(f"Medelåldern av passagerarna är {medelålder} år")

# Skriver ut personen som är äldst på bussen.
def äldst():
    try:
        for person in buss:
            ålder_lista.append(person.ålder)
        äldsta_passageraren = max(ålder_lista)
    except Exception:
        print("Det finns inga passagerare på bussen.")
    else:
        print(f"Den äldsta passageraren är {äldsta_passageraren}")

# Sorterar bussen, antingen efter namn i bokstavsordning eller efter ålder.
def bus_sort():
    sortera_hur = input("Vill du sortera passagerarna efter namn- eller åldersordning?(n/å)" "\n-> ")
    if sortera_hur == "n":
        fram_eller_bak = input("Fram- eller baklänges?(f/b)" "\n-> ")
        #nånting
    else:
        fram_eller_bak = input("Fram- eller baklänges?(f/b)" "\n-> ")
        if fram_eller_bak == "f":
            passagerare = buss.sort
            print(passagerare)
        else:
            passagerare = buss.sort[::-1]
            print(passagerare)

# Skriver ut en lista på alla passagerare inom ett visst åldersspann.
def hitta_passagerare(min_ålder, max_ålder):
  for person in buss:
    if person.ålder >= min_ålder and person.ålder <= max_ålder:
      print(person)

# Petar på en passagerare. Skriver ut en text som beskriver passagerarens
# reaktion när denne blir petad på. För lite svårare uppgift kan reaktionerna
# variera från person till person, t.ex. beroende på ålder.
def peta():
    peta_på_vem = input("Vilken av passagerarna vill du peta på?(nummer)" "\n-> ")
    print(f"Du petade på {peta_på_vem}...")
    if person.ålder >= 100 and person.ålder <= 120:
        print(f"...verkar som att {peta_på_vem} är död")
    elif person.ålder >= 70 and person.ålder < 100:
        print(f"{peta_på_vem}: Ungdomen har då tappat all respekt för de äldre" "\n>:(")
    elif person.ålder >= 40 and person.ålder < 70:
        print(f"{peta_på_vem}: Kan jag hjälpa dig med något?")
    elif person.ålder >= 30 and person.ålder < 40:
        print(f"{peta_på_vem}: Lämna mig ifred." "\n:(")
    elif person.ålder >= 20 and person.ålder < 30:
        print(f"{peta_på_vem} Muckar du eller?!")
    elif person.ålder >= 15 and person.ålder < 20:
        print(f"{peta_på_vem}: ...")
    elif person.ålder >= 10 and person.ålder < 15:
        print(f"{peta_på_vem}: Ouch!")
    elif person.ålder >= 2 and person.ålder < 10:
        print(f"{peta_på_vem}: Mamma! Hjälp!")
    elif person.ålder < 2:
        print(f"{peta_på_vem}: Wäääää" "\nD;")
def hitta_passagerare_kön(vilket_kön):
  for person in buss:
    if person.kön == vilket_kön:
      print(person)

# ------------------------------ Huvudprogram --------------------------------- #
def main():
    meny_val = ""


    while meny_val != "q":

        print(
            """
                                           _____________
                                         _/_|[][][][][] | - -
                                        (      Bussen   | - -
                                        =--OO-------OO--=
            """)

        print(
        """
                                         --- MENY ---
                    Välkommen till buss-simulatorn. Välj ett av alternativen nedan:
            1. Plocka upp ny passagerare                        2. Låt passagerare gå av
            3. Skriv ut alla passagerare                        4. Beräkna sammanlagd ålder
            5. Beräkna medelåldern                              6. Hitta äldst person
            7. Sortera bussen                                   8. Hitta personer inom ett specifikt åldersspann
            9. Peta på passagerare                              10. Hitta personer inom ett specifikt kön
            q. Avsluta
        ---------------------------------------------------------------------------------------
        """)

        meny_val = input("-> ")



        if meny_val == "1":
            plocka_upp()
            time.sleep(0.5)
        elif meny_val == "2":
            gå_av()
            time.sleep(0.5)
        elif meny_val == "3":
            skriv_ut()
            time.sleep(1)
        elif meny_val == "4":
            sammanlagd_ålder()
            time.sleep(1)
        elif meny_val == "5":
            medel_ålder()
            time.sleep(1)
        elif meny_val == "6":
            äldst()
            time.sleep(1)
        elif meny_val == "7":
            bus_sort()
        elif meny_val == "8":
            min_ålder = int(input("Från ålder" "\n->"))
            max_ålder = int(input("Till ålder" "\n->"))
            hitta_passagerare(min_ålder, max_ålder)
        elif meny_val == "9":
            peta()
        elif meny_val == "10":
            vilket_kön = input("Vilket kön letar du efter?" "\n-> ")
            hitta_passagerare_kön(vilket_kön)
        else:
            if meny_val != "q":
                print("Ogiltig inmatning, vänligen ge ett värde på 1-9 eller 'q'")
            else:
                print("Program avslutat.")
main()

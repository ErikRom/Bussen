# ------------------------------- Information --------------------------------- #
"""
Titel: Bussen
Författare: Erik och Jack
Datum: 2022-11-16
Det här är ett program för hantering av passagerare på en buss. Programmet
lagrar passagerare i en lista.
"""
# ------------------------- Biblioteksimportering ----------------------------- #
import random as rand
import time
# ---------------------------------- listor ----------------------------------- #
namn_lista = ["Jack", "Erik", "Bob", "Anna", "Leo", "Nikodemus", "Samuel", "David", "Lucas", "Marcus", "Noah", "Simon",
             "Harley", "Abigale", "Magdalena", "Marie", "Lewis", "John", "Gus", "Robin", "Jakob", "Chris", "Jimmy",
             "Clay", "Gus", "Melvin", "Isak", "Kunigunda", "Candice", "Candide"]
buss = []
ålder_lista = []

    #Person är en klass för att representera personer i bussen. Varje objekt
    #som skapas ur klassen har ett namn och en ålder, samt metoder för att returnera
    #alternativt modifiera respektive attribut
# ---------------------------- Klassdefinitioner ------------------------------ #
class Person():
    def __init__(self, namn, ålder):
        self.namn = namn
        self.ålder = ålder

    # Strängrepresentation av objektet.
    def __str__(self):
        return f"Det här är {self.namn}. Hen är {self.ålder} år gammal."

    # Setters
    def set_namn(self, nytt_namn):
        self.namn = nytt_namn

    def set_ålder(self, ny_ålder):
        self.ålder = ny_ålder

    # Getters
    def get_namn(self):
        return self.namn

    def get_ålder(self):
        return self.ålder

# ------------------------- Funktionsdefinitioner ---------------------------- #

# Lägger till en ny person i bussen.
def plocka_upp():
    if len(buss) == 25:
        print("Bussen är full, någon behöver gå av.")
    else:
        antal_upp = int(input("Hur många passagerare vill du plocka upp?" "\n-> "))
        for räknare in range(antal_upp):
            namn = rand.choice(namn_lista)
            namn_lista.remove(namn)
            ålder = rand.randint(1, 120)
            person = Person(namn, ålder)
            buss.append(person)

        print(f"Plockade upp {antal_upp} personer.")

# Avlägsnar en person från bussen.
def gå_av():
    hur_många_av = int(input("Hur många passagerare vill du ska gå av?" "\n-> "))
    if hur_många_av == 1:
        vem_av = input("Vem vill du ska gå av?" "\n-> ")
        buss.pop(vem_av) #hur ska man få inte indexnummret att gå av? kan man söka upp vilket indexnummer det är, eller kan man döpa om indexnummret till passagerarnamnet? kommer fuckas upp sen när man sorterar.
        print(f"{vem_av} gick av.")
    else:
        hur_många_av = int(input("Hur många vill du ska gå av=" "\n-> "))
        vilka_av = input("Vilka vill du ska gå av?" "\n1.-> ")
        buss.pop(hur_många_av)
        print(f"{vilka_av} gick av")

# Listar alla passagerare på bussen.
def skriv_ut():
    for person in buss:
        print(person.namn, person.ålder)

# Skriver ut den sammanlagda åldern på passagerarna.
def sammanlagd_ålder():
    ålder = 0
    for person in buss:
        ålder += person.ålder
    print(f"Den sammanlagda åldern av passagerarna är {ålder}")

# Skriver ut medelåldern på passagerarna i bussen.
def medel_ålder():
    ålder_medel = 0
    for person in buss:
        ålder_medel += person.ålder
    medelålder = ålder_medel / len(buss)
    print(f"Medelåldern av passagerarna är {medelålder} år")

# Skriver ut personen som är äldst på bussen.
def äldst():
    for person in buss:
        ålder_lista.append(person.ålder)
    äldsta_passageraren = max(ålder_lista)
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
def hitta_passagerare():
    från_ålder = int(input("Från vilken ålder vill du hitta passagerare?" "\-> "))
    till_ålder = int(input("Till vilken ålder vill du hitta passagerare?" "\-> "))
    print(buss(range(från_ålder, till_ålder)))

# petar på en passagerare. Skriver ut en text som beskriver passagerarens
# reaktion när denne blir petad på. För lite svårare uppgift kan reaktionerna
# variera från person till person, t.ex. beroende på ålder.
def peta(passagerare):
    peta_på_vem = input("Vilken av passagerarna vill du peta på?" "\n-> ")
    print(f"Du petade på {peta_på_vem}...")
    print(f"{peta_på_vem}: Ouch!")

# ------------------------------ Huvudprogram --------------------------------- #
def main():
    meny_val = ""

    while meny_val != "q":

        print(
        """
                                         --- MENY ---
                    Välkommen till buss-simulatorn. Välj ett av alternativen nedan:
            1. Plocka upp ny passagerare                        2. Låt passagerare gå av
            3. Skriv ut alla passagerare                        4. Beräkna sammanlagd ålder
            5. Beräkna medelåldern                              6. Hitta äldst person
            7. Sortera bussen                                   8. Hitta personer inom ett specifikt åldersspann
            9. Peta på passagerare                              q. Avsluta
        ---------------------------------------------------------------------------------------
        """)

        meny_val = input("-> ")

        if meny_val == "1":
            plocka_upp()
            time.sleep(0.5)
        elif meny_val == "2":
            gå_av()
        elif meny_val == "3":
            skriv_ut()
            time.sleep(1)
        elif meny_val == "4":
            sammanlagd_ålder()
            time.sleep(1)
        elif meny_val == "5":
            medel_ålder()
        elif meny_val == "6":
            äldst()
        elif meny_val == "7":
            bus_sort()
        elif meny_val == "8":
            hitta_passagerare()
        elif meny_val == "9":
            peta()


print(
"""
                                           _____________
                                         _/_|[][][][][] | - -
                                        (      Bussen   | - -
                                        =--OO-------OO--=
""")

main()

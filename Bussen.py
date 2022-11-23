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
namnLista = ["Jack", "Erik", "Bob", "Anna", "Leo", "Nikodemus", "Samuel", "David", "Lucas", "Marcus", "Noah", "Simon",
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
    def setNamn(self, nyttNamn):
        self.namn = nyttNamn

    def setÅlder(self, nyÅlder):
        self.ålder = nyÅlder

    # Getters
    def getNamn(self):
        return self.namn

    def getÅlder(self):
        return self.ålder

# ------------------------- Funktionsdefinitioner ---------------------------- #

# Lägger till en ny person i bussen.
def plockaUpp():
    if len(buss) == 25:
        print("Bussen är full, någon behöver gå av.")
    else:
        antalUpp = int(input("Hur många passagerare vill du plocka upp?" "\n-> "))
        for räknare in range(antalUpp):
            namn = rand.choice(namnLista)
            namnLista.remove(namn)
            ålder = rand.randint(1, 120)
            person = Person(namn, ålder)
            buss.append(person)

        print(f"Plockade upp {antalUpp} personer.")

# Avlägsnar en person från bussen.
def gåAv():
    hurMångaAv = int(input("Hur många passagerare vill du ska gå av?" "\n-> "))
    if hurMångaAv == 1:
        vemAv = input("Vem vill du ska gå av?" "\n-> ")
        buss.pop(vemAv) #hur ska man få inte indexnummret att gå av? kan man söka upp vilket indexnummer det är, eller kan man döpa om indexnummret till passagerarnamnet? kommer fuckas upp sen när man sorterar.
        print(f"{vemAv} gick av.")
    else:
        HurMångaAv = int(input("Hur många vill du ska gå av=" "\n-> "))
        vilkaAv = input("Vilka vill du ska gå av?" "\n1.-> ")
        buss.pop(HurMångaAv)
        print(f"{vilkaAv} gick av")

# Listar alla passagerare på bussen.
def skrivUt():
    for person in buss:
        print(person.namn, person.ålder)

# Skriver ut den sammanlagda åldern på passagerarna.
def sammanlagdÅlder():
    ålder = 0
    for person in buss:
        ålder += person.ålder
    print(f"Den sammanlagda åldern av passagerarna är {ålder}")

# Skriver ut medelåldern på passagerarna i bussen.
def medelÅlder():
    medelVärde = sum(listan) / len(listan)
    print(f"Medelåldern av passagerarna är {medelVärde}")

# Skriver ut personen som är äldst på bussen.
def äldst():
    for person in buss:
        ålder_lista.append(person.ålder)
    äldsta_passageraren = max(ålder_lista)
    print(f"Den äldsta passageraren är {äldsta_passageraren}")

# Sorterar bussen, antingen efter namn i bokstavsordning eller efter ålder.
def busSort():
    sortera_hur = input("Vill du sortera passagerarna efter namn- eller åldersordning?(n/å)" "\n-> ")
    if sortera_hur == "n":
        fram_eller_bak = input("Fram- eller baklänges?(f/b)" "\n-> ")
        #nånting
    else:
        fram_eller_bak = input("Fram- eller baklänges?(f/b)" "\n-> ")
        if fram_eller_ak == "f":
            passagerare = buss.sort
            print(passagerare)
        else:
            passagerare = buss.sort[::-1]
            print(passagerare)

# Skriver ut en lista på alla passagerare inom ett visst åldersspann.
def hittaPassagerare():
    frånÅlder = int(input("Från vilken ålder vill du hitta passagerare?" "\-> "))
    tillÅlder = int(input("Till vilken ålder vill du hitta passagerare?" "\-> "))
    print(buss(range(frånÅlder, tillÅlder)))

# petar på en passagerare. Skriver ut en text som beskriver passagerarens
# reaktion när denne blir petad på. För lite svårare uppgift kan reaktionerna
# variera från person till person, t.ex. beroende på ålder.
def peta(passagerare):
    petaPåVem = input("Vilken av passagerarna vill du peta på?" "\n-> ")
    print(f"Du petade på {petaPåVem}...")
    print(f"{petaPåVem}: Ouch!")

# ------------------------------ Huvudprogram --------------------------------- #
def main():
    menyVal = ""

    while menyVal != "q":

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

        menyVal = input("-> ")

        if menyVal == "1":
            plockaUpp()
            time.sleep(0.5)
        elif menyVal == "2":
            gåAv()
        elif menyVal == "3":
            skrivUt()
            time.sleep(1)
        elif menyVal == "4":
            sammanlagdÅlder()
            time.sleep(1)
        elif menyVal == "5":
            medelÅlder()
        elif menyVal == "6":
            äldst()
        elif menyVal == "7":
            busSort()
        elif menyVal == "8":
            hittaPassagerare()
        elif menyVal == "9":
            peta()


print(
"""
                                           _____________
                                         _/_|[][][][][] | - -
                                        (      Bussen   | - -
                                        =--OO-------OO--=
""")

main()

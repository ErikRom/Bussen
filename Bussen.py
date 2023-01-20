# ------------------------------- Information --------------------------------- #
"""
Titel: Bussen
Författare: Erik och Jack
Datum: 2022-11-16
Det här är ett program för hantering av passagerare på en buss. Programmet
lagrar passagerare i en lista.
"""
# ------------------------- Biblioteksimportering ----------------------------- #
import random as rand  # importerar en funktion för att kunna skapa funktioner som slumpar fram b.la åldrar och namn.
import time  # importerar en funktion för att kunna fördröja hur snabbt saker och ting händer i terminalen

# ---------------------------------- listor ----------------------------------- #
namn_lista_kille = ["Jack", "Erik", "Bob", "Leo", "Nikodemus", "Samuel", "David", "Lucas", "Marcus", "Noah",
                    "Simon", "Harley", "Lewis", "John", "Gus", "Robin", "Jakob", "Chris", "Jimmy",
                    "Clay", "Gus", "Melvin", "Isak", "Candide", "Joe", "Kung", "Kingkong", "Hunk", "Hnulk", "Chad"]

namn_lista_tjej = ["Anna", "Abigale", "Magdalena", "Marie", "Kunigunda", "Candice", "Birgitt",
                   "Britt-marie", "Anna-lena", "Elise", "Jeanette", "Åsa", "Lara", "Linnea", "Annet", "Hanna",
                   "Elsa", "Helena", "Jana", "Athena"]
buss = []
ålder_lista = []


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
            if antal_upp > 25:
                print("För många passagerare, max antal är 25.")
                return
            for räknare in range(antal_upp):  # slumpar om det blir en kille/tjej och väljer därefter
                nummer = rand.randint(1, 2)  # för att ge 50/50 chans för kille/tjej
                if nummer == 1:
                    namn = rand.choice(namn_lista_tjej)  # slumpat namn
                    namn_lista_tjej.remove(namn)  # tar bort namn från slumpen så alla blir unika
                    kön = "tjej"
                elif nummer == 2:
                    namn = rand.choice(namn_lista_kille)  # slumpat namn1
                    namn_lista_kille.remove(namn)  # tar bort namn från slumpen så alla blir unika
                    kön = "kille"
                ålder = rand.randint(1, 120)  # slumpad ålder
                person = Person(namn, ålder, kön)
                buss.append(person)
        except (
        ValueError, IndexError):  # vid en ogiltig inmatning körs programmet om istället för att ge ett felmeddelande
            print("Ogiltig inmatning, vänligen försök igen.")
        else:
            print(f"Plockade upp {antal_upp} personer.")


# Avlägsnar en person från bussen.
def gå_av():
    if len(buss) == 0:
        print("Det finns inga passagerare på bussen. Börja med att lägga till några!")
    else:
        try:
            hur_många_av = int(input("Hur många personer vill du ska gå av? " "\n-> "))
            if hur_många_av > len(buss):
                print("Det finns inte så många personer i bussen.")
            else:
                for passagerare in range(hur_många_av):
                    namn = input("Ange namnet på personen som ska gå av: ").capitalize()
                    borttagen = False
                    for index in range(len(buss)):
                        if buss[index].get_namn() == namn:
                            buss.pop(index)
                            print(f"{namn} gick av.")
                            borttagen = True
                            break
                    if not borttagen:
                        print(f"Det finns ingen person med namnet {namn} i bussen.")
        except Exception:
            print("Ogiltig inmatning, vänligen försök igen.")


# Listar alla passagerare på bussen.
def skriv_ut():
    if len(buss) == 0:
        print("Det finns inga passagerare på bussen. Börja med att lägga till några!")
    else:
        for person in buss:
            print(person.namn, person.ålder, person.kön)


# Skriver ut den sammanlagda åldern på passagerarna.
def sammanlagd_ålder():
    sammanlagd_ålder = 0
    for person in buss:
        sammanlagd_ålder += person.ålder
    print(f"Den sammanlagda åldern av passagerarna är {sammanlagd_ålder}")


# Skriver ut medelåldern på passagerarna i bussen.
def medel_ålder():
    if len(buss) == 0:
        print("Det finns inga passagerare på bussen. Börja med att lägga till några!")
    else:
        ålder_medel = 0
        for person in buss:
            ålder_medel += person.ålder
        medelålder = ålder_medel / len(buss)
        print(f"Medelåldern av passagerarna är {medelålder:.2f} år")


# Skriver ut personen som är äldst på bussen.
def äldst():
    if len(buss) == 0:
        print("Det finns inga passagerare på bussen. Börja med att lägga till några!")
    else:
        for person in buss:
            ålder_lista.append(person.ålder)
        äldsta_passageraren = max(ålder_lista)
        print(f"Den äldsta passageraren är {äldsta_passageraren}")


# Sorterar bussen, antingen efter namn i bokstavsordning eller efter ålder.
def efter_namn(person):
    return person.get_namn()


def efter_ålder(person):
    return person.get_ålder()


def buss_sort():
    if len(buss) == 0:
        print("Det finns inga passagerare på bussen. Börja med att lägga till några!")
    else:
        sortera_efter = input("Sortera efter namn eller ålder?" "\n-> ")
        if sortera_efter == "namn":
            buss.sort(key=efter_namn)
            print("Listan sorterad efter bokstavsordning." "\n")
            for person in buss:
                print(person.namn, person.ålder, person.kön)
        elif sortera_efter == "ålder":
            buss.sort(key=efter_ålder)
            print("Listan sorterad efter ålder." "\n")
            for person in buss:
                print(person.namn, person.ålder, person.kön)
        else:
            print("Otillåten sorteringsmetod, vänligen försök igen")


# Skriver ut en lista på alla passagerare inom ett visst åldersspann.
def hitta_passagerare():
    if len(buss) == 0:
        print("Det finns inga passagerare på bussen. Börja med att lägga till några!")
    else:
        try:
            min_ålder = int(input("Från ålder" "\n-> "))
            max_ålder = int(input("Till ålder" "\n-> "))
        except Exception:
            print("Ogiltig inmatning, vänligen försök igen.")
        else:
            print(f"Passagerare inom åldersspannet {min_ålder} - {max_ålder} år:" "\n")
            for person in buss:
                if min_ålder <= person.ålder <= max_ålder:
                    print(person)


# Petar på en passagerare. Skriver ut en text som beskriver passagerarens
# reaktion när denne blir petad på. För lite svårare uppgift kan reaktionerna
# variera från person till person, t.ex. beroende på ålder.
def peta():  # Ger olika responser från passagerarna beroende på deras ålder
    if len(buss) == 0:
        print("Det finns inga passagerare på bussen. Börja med att lägga till några!")
    else:
        peta_på_vem = input("Vilken av passagerarna vill du peta på?" "\n-> ").capitalize()
        for person in buss:
            if person.namn == peta_på_vem:
                print(f"Du petade på {peta_på_vem}...")
                if 100 <= person.ålder <= 120:
                    print(f"...verkar som att {peta_på_vem} är död")
                elif 70 <= person.ålder < 100:
                    print(f"{peta_på_vem}: NEJ")
                elif 40 <= person.ålder < 70:
                    print(f"{peta_på_vem}: AY")
                elif 30 <= person.ålder < 40:
                    print(f"{peta_på_vem}: GRR")
                elif 20 <= person.ålder < 30:
                    print(f"{peta_på_vem} OUCH!")
                elif 15 <= person.ålder < 20:
                    print(f"{peta_på_vem}: ...")
                elif 10 <= person.ålder < 15:
                    print(f"{peta_på_vem}: AJE!")
                elif 2 <= person.ålder < 10:
                    print(f"{peta_på_vem}: OW!")
                elif person.ålder < 2:
                    print(f"{peta_på_vem}:" "AAA!")

    print("Otillåten inmatning, vänligen försök igen.")


def hitta_passagerare_kön(vilket_kön):
    if vilket_kön == "man":
        vilket_kön = "kille"
    elif vilket_kön == "kvinna":
        vilket_kön = "tjej"
    for person in buss:
        if person.kön == vilket_kön:
            print(person)

# ------------------------------ Huvudprogram --------------------------------- #
def main():
    meny_val = ""

    while True:

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
            time.sleep(0.5)
        elif meny_val == "4":
            sammanlagd_ålder()
            time.sleep(0.5)
        elif meny_val == "5":
            medel_ålder()
            time.sleep(0.5)
        elif meny_val == "6":
            äldst()
            time.sleep(0.5)
        elif meny_val == "7":
            buss_sort()
            time.sleep(0.5)
        elif meny_val == "8":
            hitta_passagerare()
            time.sleep(0.5)
        elif meny_val == "9":
            peta()
            time.sleep(0.5)
        elif meny_val == "10":
            if len(buss) == 0:
                print("Det finns inga passagerare på bussen. Börja med att lägga till några!")
            else:
                vilket_kön = input("Vilket kön letar du efter?" "\n-> ").lower()
                hitta_passagerare_kön(vilket_kön)
            time.sleep(0.5)
        elif meny_val == "q":
            print("Bussen kraschade")
            break
        else:
            print("Ogiltig inmatning, vänligen ge ett värde på 1-10 eller 'q'")

main()

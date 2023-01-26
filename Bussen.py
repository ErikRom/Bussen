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
namn_lista_kille = ["Jack", "Erik", "Bob", "Leo", "Samuel", "David", "Lucas", "Marcus", "Noah",
                    "Simon", "Harley", "Lewis", "John", "Robin", "Jakob", "Chris", "Jimmy",
                    "Melvin", "Isak", "Joe", "William", "Adam", "Oliver", "Elias"]

namn_lista_tjej = ["Anna", "Magdalena", "Marie", "Birgitt", "Britt-marie", "Anna-lena",
                   "Elise", "Jeanette", "Åsa", "Lara", "Linnea", "Annet", "Hanna", "Elsa", "Helena",
                   "Jana", "Ella", "Maja", "Felicia", "Matilda", "Alice", "Vera"]
använda_namn = []
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
            if antal_upp + len(buss) > 25:
                print("För många passagerare, max antal är 25.")
                return
            for räknare in range(antal_upp):  # slumpar om det blir en kille/tjej och väljer därefter
                nummer = rand.randint(1, 2)  # för att ge 50/50 chans för kille/tjej
                if nummer == 1:
                    namn = rand.choice(namn_lista_tjej)  # slumpat namn
                    använda_namn.append(namn)  # lista med använda namn för att användas senare
                    namn_lista_tjej.remove(namn)  # tar bort namn från slumpen så alla blir unika
                    kön = "tjej"
                elif nummer == 2:
                    namn = rand.choice(namn_lista_kille)
                    använda_namn.append(namn)
                    namn_lista_kille.remove(namn)
                    kön = "kille"
                ålder = rand.randint(1, 120)  # slumpad ålder
                person = Person(namn, ålder, kön)
                buss.append(person)
        except (ValueError, IndexError):  # vid en ogiltig inmatning körs programmet om istället för att ge ett felmeddelande
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
            elif hur_många_av > 0:
                print(använda_namn)  # lättare att veta vilka möjliga personer som kan gå av
                for passagerare in range(hur_många_av):
                    namn = input(f"Ange namnet på personen som ska gå av: ").capitalize()
                    borttagen = False
                    for index in range(len(buss)):  # går igenom alla bussens index
                        if buss[index].get_namn() == namn:  # när någon av objektens namn stämmer av tas objektet bort
                            buss.pop(index)
                            print(f"{namn} gick av.")
                            borttagen = True
                            break
                    if not borttagen:  # om ingen med inskrivet namn existerar bland listan
                        print(f"Det finns ingen person med namnet {namn} i bussen.")
            else:
                print("Ogiltig inmatning")
        except Exception:  # för att göra inmatningssäkert
            print("Ogiltig inmatning, vänligen försök igen.")
            gå_av()


# Listar alla passagerare på bussen.
def skriv_ut():
    if len(buss) == 0:
        print("Det finns inga passagerare på bussen. Börja med att lägga till några!")
    else:
        for person in buss:  # loopar igenom lista och skriver ut alla attribut
            print(person.namn, person.ålder, person.kön)


# Skriver ut den sammanlagda åldern på passagerarna.
def sammanlagd_ålder():
    ålder_tot = 0

    for person in buss:  # lägger ihop allas åldrar i en variabel
        ålder_tot += person.ålder
    print(f"Den sammanlagda åldern av passagerarna är {ålder_tot}")


# Skriver ut medelåldern på passagerarna i bussen.
def medel_ålder():
    if len(buss) == 0:
        print("Det finns inga passagerare på bussen. Börja med att lägga till några!")
    else:
        ålder_tot = 0
        for person in buss:
            ålder_tot += person.ålder
        medelålder = ålder_tot / len(buss)  # medelålder = total ålder / antal personer
        print(f"Medelåldern av passagerarna är {medelålder:.2f} år")


# Skriver ut personen som är äldst på bussen.
def äldst():
    if len(buss) == 0:
        print("Det finns inga passagerare på bussen. Börja med att lägga till några!")
    else:
        for person in buss:
            ålder_lista.append(person.ålder)
        högst_ålder = max(ålder_lista)  # skapar en lista av alla personers åldrar, det största värdet är den äldsta
        print(f"Den äldsta passageraren är {högst_ålder}")


# Sorterar bussen, antingen efter namn i bokstavsordning eller efter ålder.
def efter_namn(person):
    return person.get_namn()


def efter_ålder(person):
    return person.get_ålder()


def buss_sort():
    if len(buss) == 0:
        print("Det finns inga passagerare på bussen. Börja med att lägga till några!")
    else:
        sortera_efter = input("Sortera efter namn eller ålder?" "\n-> ").lower()
        if sortera_efter == "namn":
            buss.sort(key=efter_namn)  # använder funktionen efter_namn() som finns ovan
            print("Listan sorterad efter bokstavsordning." "\n")
            for person in buss:  # skriver ut det sorterade resultatet, men ändrar dessutom originalet
                print(person.namn, person.ålder, person.kön)
        elif sortera_efter == "ålder":
            buss.sort(key=efter_ålder)
            print("Listan sorterad efter ålder." "\n")
            for person in buss:
                print(person.namn, person.ålder, person.kön)
        else:  # inmatningssäkert
            print("Otillåten sorteringsmetod, vänligen försök igen")
            buss_sort()


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
                if min_ålder <= person.ålder <= max_ålder:  # om ett objekt i bussen uppfyller kraven skrivs all info ut
                    print(person)


# Petar på en passagerare. Skriver ut en text som beskriver passagerarens
# reaktion när denne blir petad på.
def peta():
    if len(buss) == 0:
        print("Det finns inga passagerare på bussen. Börja med att lägga till några!")
    else:
        print("Personer på bussen: " f"{använda_namn}")
        peta_på_vem = input("Vilken av passagerarna vill du peta på?" "\n-> ").capitalize()
        if peta_på_vem in använda_namn:  # check om namnet på personen som ska petas faktiskt finns
            for person in buss:  # loopar igenom alla personobjekt för att hitta en med matchande namn
                if person.namn == peta_på_vem:
                    print(f"Du petade på {peta_på_vem}...")
                    if 100 <= person.ålder <= 120:  # Nedan ges olika responser från passageraren beroende på dess ålder
                        print(f"...verkar som att {peta_på_vem} är död")
                    elif 70 <= person.ålder < 100:
                        print(f"{peta_på_vem}: NEJ")
                    elif 40 <= person.ålder < 70:
                        print(f"{peta_på_vem}: AY")
                    elif 30 <= person.ålder < 40:
                        print(f"{peta_på_vem}: GRR")
                    elif 20 <= person.ålder < 30:
                        print(f"{peta_på_vem}: OUCH!")
                    elif 15 <= person.ålder < 20:
                        print(f"{peta_på_vem}: ...")
                    elif 10 <= person.ålder < 15:
                        print(f"{peta_på_vem}: AJE!")
                    elif 2 <= person.ålder < 10:
                        print(f"{peta_på_vem}: OW!")
                    elif person.ålder < 2:
                        print(f"{peta_på_vem}:" "AAA!")
        else:
            print("Otillåten inmatning, vänligen försök igen.")

# För att hitta och skriva ut passagerare av ett visst kön
def hitta_passagerare_kön():
    if len(buss) == 0:
        print("Det finns inga passagerare på bussen. Börja med att lägga till några!")
    else:
        vilket_kön = input("Vilket kön letar du efter? (kille/tjej)" "\n-> ").lower()
        if vilket_kön == "man":  # för att undvika misstag där olika könssynonymer används
            vilket_kön = "kille"
        elif vilket_kön == "kvinna":
            vilket_kön = "tjej"
        for person in buss:
            if person.kön == vilket_kön:
                print(person)  # skriver ut full info om varje person av ditt valda kön

# ------------------------------ Huvudprogram --------------------------------- #
def main():

    while True:  # loop för att alltid komma tillbaka till "main menu" efter felinmatning eller
                 # om en delfunktion är färdigkörd

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
        #  beroende på vilket tal 1-10 man skriver in körs respektive funktion för att hantera bussen på olika sätt
        if meny_val == "1":
            plocka_upp()
            time.sleep(0.5)  # för att ge lite mellanrum mellan text när koden körs
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
            hitta_passagerare_kön()
            time.sleep(0.5)
        elif meny_val == "q":  # programmet avslutas när man skriver in "q"
            print("Bussen kraschade")
            break
        else:  # vid annan inmatning är 1-10 eller "q" körs programmet om istället
            print("Ogiltig inmatning, vänligen ge ett värde på 1-10 eller 'q'")


main()  # Startar programmet

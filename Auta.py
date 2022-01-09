class Auta:
    def __init__(self, liczba_drzwi, rok_prod):
        self.drzwi = liczba_drzwi
        self.produkcja = rok_prod
        self.status_drzwi = False

    def wyswietl(self):
        print("Auto dziala")

    def otworz_drzwi(self):
        self.status_drzwi = True
        print("Drzwi zostały otwarte.")

    def zamknij_drzwi(self):
        print("Drzwi zostały zamknięte.")
        self.status_drzwi = False

    def sprawdz_drzwi(self):
        if self.status_drzwi == True:
            print("Drzwi są otwarte")
        else:
            print("Drzwi są zamknięte")
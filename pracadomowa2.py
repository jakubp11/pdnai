import random

class Sigma:
    def __init__(self):
        self.hp = 100
        self.atak = 10
        self.zyje = True
        self.poziom = 1
        self.exp = 0
        self.zloto = 0
        self.obrona = False

    def odejmij_hp(self, dmg):
        if self.obrona:
            dmg //= 2  
        self.hp -= dmg
        if self.hp <= 0:
            self.zyje = False

    def czy_zyje(self):
        return self.zyje

    def basic_atak(self):
        return self.atak

    def superatak(self):
        return self.atak * 2

    def zdobadz_exp(self, ilosc):
        self.exp += ilosc
        if self.exp >= 10 * self.poziom:
            self.poziom += 1
            self.atak += 2
            self.hp += 20
            print(f"Sigma awansowała na poziom {self.poziom}!")

    def zdobycie_zlota(self, ilosc):
        self.zloto += ilosc

class Przeciwnik:
    def __init__(self, nazwa, hp, atak, exp, zloto):
        self.nazwa = nazwa
        self.hp = hp
        self.atak = atak
        self.exp = exp
        self.zloto = zloto
        self.zyje = True

    def odejmij_hp(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.zyje = False

    def czy_zyje(self):
        return self.zyje

    def basic_atak(self):
        return self.atak

class Goblin(Przeciwnik):
    def __init__(self):
        super().__init__("Goblin", random.randint(30, 70), random.randint(3, 8), 5, 10)

sigma = Sigma()
licznik_zabitych = 0

while sigma.czy_zyje():
    przeciwnik = Goblin()
    print(f"Nowy przeciwnik: {przeciwnik.nazwa} (HP: {przeciwnik.hp})")
    
    while przeciwnik.czy_zyje():
        print(f"Twoje HP: {sigma.hp}")
        print("Wybierz akcję: a) Atak b) Superatak c) Obrona d) Ucieczka")
        wybor = input().lower()

        if wybor == "a":
            przeciwnik.odejmij_hp(sigma.basic_atak())
            print("Zadałeś cios!")
        elif wybor == "b":
            przeciwnik.odejmij_hp(sigma.superatak())
            print("Użyłeś superataku!")
        elif wybor == "c":
            sigma.obrona = True
            print("Przyjąłeś postawę obronną!")
        elif wybor == "d":
            print("Uciekłeś!")
            break
        else:
            print("Nieznana opcja, spróbuj ponownie.")
            continue

        if przeciwnik.czy_zyje():
            sigma.odejmij_hp(przeciwnik.basic_atak())
            print(f"Przeciwnik atakuje! Twoje HP: {sigma.hp}")
        sigma.obrona = False

    if sigma.czy_zyje() and przeciwnik.hp <= 0:
        licznik_zabitych += 1
        sigma.zdobadz_exp(przeciwnik.exp)
        sigma.zdobycie_zlota(przeciwnik.zloto)
        print(f"Pokonałeś {przeciwnik.nazwa}!")

print("Sigma poległa w walce...")

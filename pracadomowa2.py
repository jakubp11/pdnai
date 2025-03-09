import random

class Postac:
    def __init__(self, imie, hp, atak, obrona, zloto, exp):
        self.imie = imie
        self.hp = hp
        self.max_hp = hp
        self.atak = atak
        self.obrona = obrona
        self.zloto = zloto
        self.exp = exp
        self.poziom = 1
        self.zyje = True
        self.ekwipunek = []
        self.mikstury = 3  

    def odejmij_hp(self, dmg):
        dmg = max(0, dmg - self.obrona)
        self.hp -= dmg
        if self.hp <= 0:
            self.zyje = False

    def basic_atak(self):
        return self.atak + random.randint(1, 5)

    def superatak(self):
        return self.atak * 2

    def zdobycie_zlota(self, ilosc):
        self.zloto += ilosc

    def zdobadz_exp(self, ilosc):
        self.exp += ilosc
        if self.exp >= 10 * self.poziom:
            self.poziom += 1
            self.atak += 3
            self.max_hp += 20
            self.hp = self.max_hp
            print(f"{self.imie} awansował na poziom {self.poziom}!")

    def dodaj_ekwipunek(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    def wyswietl_ekwipunek(self):
        if self.ekwipunek:
            print("Ekwipunek:", ", ".join(self.ekwipunek))
        else:
            print("Ekwipunek jest pusty.")

    def uzyj_mikstury(self):
        if self.mikstury > 0:
            self.hp = min(self.max_hp, self.hp + 20)
            self.mikstury -= 1
            print("Wypiłeś miksturę i odzyskałeś zdrowie!")
        else:
            print("Brak mikstur!")

class Sigma(Postac):
    def __init__(self):
        super().__init__("Sigma", 100, 10, 3, 0, 0)

class Wojownik(Postac):
    def __init__(self):
        super().__init__("Wojownik", 120, 15, 5, 0, 0)

class Mag(Postac):
    def __init__(self):
        super().__init__("Mag", 80, 25, 2, 0, 0)

class Zlodziej(Postac):
    def __init__(self):
        super().__init__("Złodziej", 90, 12, 4, 0, 0)

class Rycerz(Postac):
    def __init__(self):
        super().__init__("Rycerz", 150, 18, 6, 0, 0)

class Nekromanta(Postac):
    def __init__(self):
        super().__init__("Nekromanta", 100, 20, 3, 0, 0)

class Zabojca(Postac):
    def __init__(self):
        super().__init__("Zabójca", 85, 30, 2, 0, 0)

class Przeciwnik:
    def __init__(self, nazwa, hp, atak, obrona, exp, zloto):
        self.nazwa = nazwa
        self.hp = hp
        self.atak = atak
        self.obrona = obrona
        self.exp = exp
        self.zloto = zloto
        self.zyje = True

    def odejmij_hp(self, dmg):
        dmg = max(0, dmg - self.obrona)
        self.hp -= dmg
        if self.hp <= 0:
            self.zyje = False

    def basic_atak(self):
        return self.atak + random.randint(1, 4)

class Goblin(Przeciwnik):
    def __init__(self):
        super().__init__("Goblin", random.randint(30, 70), random.randint(3, 8), 1, 5, 10)

class Ork(Przeciwnik):
    def __init__(self):
        super().__init__("Ork", random.randint(50, 100), random.randint(6, 12), 3, 8, 15)

class Smok(Przeciwnik):
    def __init__(self):
        super().__init__("Smok", random.randint(100, 200), random.randint(10, 20), 5, 20, 50)

class Szkielet(Przeciwnik):
    def __init__(self):
        super().__init__("Szkielet", random.randint(40, 80), random.randint(5, 10), 2, 7, 12)

class Troll(Przeciwnik):
    def __init__(self):
        super().__init__("Troll", random.randint(80, 150), random.randint(8, 15), 4, 15, 25)

class Minotaur(Przeciwnik):
    def __init__(self):
        super().__init__("Minotaur", random.randint(120, 250), random.randint(12, 22), 6, 30, 60)

klasy_postaci = {"a": Sigma, "b": Wojownik, "c": Mag, "d": Zlodziej, "e": Rycerz, "f": Nekromanta, "g": Zabojca}
print("Wybierz swoją postać:")
print("a) Sigma, b) Wojownik, c) Mag, d) Złodziej, e) Rycerz, f) Nekromanta, g) Zabójca")
wybor = input("Twój wybór: ").lower()
bohater = klasy_postaci.get(wybor, Sigma)()

licznik_zabitych = 0
while bohater.czy_zyje():
    przeciwnik = random.choice([Goblin(), Ork(), Smok(), Szkielet(), Troll(), Minotaur()])
    print(f"Nowy przeciwnik: {przeciwnik.nazwa} (HP: {przeciwnik.hp})")

    while przeciwnik.czy_zyje():
        print(f"Twoje HP: {bohater.hp}")
        print("Wybierz akcję: a) Atak b) Superatak c) Użyj mikstury d) Ucieczka e) Ekwipunek")
        wybor = input().lower()

        if wybor == "a":
            przeciwnik.odejmij_hp(bohater.basic_atak())
            print("Zadałeś cios!")
        elif wybor == "b":
            przeciwnik.odejmij_hp(bohater.superatak())
            print("Użyłeś superataku!")
        elif wybor == "c":
            bohater.uzyj_mikstury()
        elif wybor == "d":
            print("Uciekłeś!")
            break
        elif wybor == "e":
            bohater.wyswietl_ekwipunek()
        else:
            print("Nieznana opcja, spróbuj ponownie.")
            continue

        if przeciwnik.czy_zyje():
            bohater.odejmij_hp(przeciwnik.basic_atak())
            print(f"Przeciwnik atakuje! Twoje HP: {bohater.hp}")

    if bohater.czy_zyje() and przeciwnik.hp <= 0:
        licznik_zabitych += 1
        bohater.zdobadz_exp(przeciwnik.exp)
        bohater.zdobycie_zlota(przeciwnik.zloto)
        print(f"Pokonałeś {przeciwnik.nazwa}!")

print("Twoja postać poległa w walce...")

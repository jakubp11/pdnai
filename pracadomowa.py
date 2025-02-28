class Auto:
    def __init__(self, marka, model, rok, kolor, przebieg, paliwo, moc, skrzynia, liczba_drzwi, cena):
        self.marka = marka
        self.model = model
        self.rok = rok
        self.kolor = kolor
        self.przebieg = przebieg
        self.paliwo = paliwo
        self.moc = moc
        self.skrzynia = skrzynia
        self.liczba_drzwi = liczba_drzwi
        self.cena = cena

    def przedstaw(self):
        return self.marka ,self.model ,self.rok ,self.kolor,self.cena

    def zwieksz_przebieg(self, km):
        self.przebieg += km

    def zmien_kolor(self, nowy_kolor):
        self.kolor = nowy_kolor

    def zmien_cene(self, nowa_cena):
        self.cena = nowa_cena

    def typ_paliwa(self):
        return  {self.paliwo}

    def moc_silnika(self):
        return {self.moc}

    def rodzaj_skrzyni(self):
        return {self.skrzynia}


class Tel:
    def __init__(self, marka, model, ekran, bateria, aparat, ram, pamiec, system, cena, kolor):
        self.marka = marka
        self.model = model
        self.ekran = ekran
        self.bateria = bateria
        self.aparat = aparat
        self.ram = ram
        self.pamiec = pamiec
        self.system = system
        self.cena = cena
        self.kolor = kolor

    def przedstaw(self):
        return self.marka ,self.model,self.ekran,self.kolor,self.cena

    def zmien_kolor(self, nowy_kolor):
        self.kolor = nowy_kolor

    def aktualizuj_system(self, nowy_system):
        self.system = nowy_system

    def zmniejsz_cene(self, kwota):
        self.cena -= kwota

    def sprawdz_pamiec(self):
        return {self.pamiec} 

    def stan_baterii(self):
        return {self.bateria}

    def aparat_info(self):
        return {self.aparat}


class Stud:
    def __init__(self, imie, nazwisko, wiek, kierunek, rok_studiow, srednia_ocen, indeks, adres, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.kierunek = kierunek
        self.rok_studiow = rok_studiow
        self.srednia_ocen = srednia_ocen
        self.indeks = indeks
        self.adres = adres
        self.telefon = telefon
        self.email = email

    def przedstaw(self):
        return self.imie ,self.nazwisko, self.kierunek,  self.rok_studiow
    def zmien_adres(self, nowy_adres):
        self.adres = nowy_adres
    def aktualizuj_email(self, nowy_email):
        self.email = nowy_email
    def popraw_ocene(self, nowa_srednia):
        self.srednia_ocen = nowa_srednia
    def rok_ukonczenia(self):
        return {2024 + (5 - self.rok_studiow)}
    def dane_kontaktowe(self):
        return  {self.telefon},{self.email}
    def sprawdz_indeks(self):
        return {self.indeks}
auto1 = Auto("Toyota", "Corolla", 2020, "Czerwony", 45000, "Benzyna", 150, "Automatyczna", 5, 70000)
auto2 = Auto("BMW", "X5", 2018, "Czarny", 120000, "Diesel", 300, "Automatyczna", 5, 180000)
auto3 = Auto("Audi", "A4", 2022, "Biały", 10000, "Hybryda", 250, "Manualna", 4, 150000)


telefon1 = Tel("Samsung", "Galaxy S21", 6.2, 4000, 64, 8, 128, "Android", 3500, "Niebieski")
telefon2 = Tel("Apple", "iPhone 13", 6.1, 3200, 12, 6, 256, "iOS", 4500, "Czarny")
telefon3 = Tel("Xiaomi", "Redmi Note 11", 6.5, 5000, 50, 6, 128, "Android", 1500, "Srebrny")


student1 = Stud("Jan", "Kowalski", 21, "Informatyka", 3, 4.5, "123456", "Warszawa, ul. Nowa 5", "500-600-700", "jan.kowalski@example.com")
student2 = Stud("Anna", "Nowak", 22, "Ekonomia", 4, 4.0, "654321", "Kraków, ul. Stara 10", "600-700-800", "anna.nowak@example.com")
student3 = Stud("Piotr", "Wiśniewski", 20, "Medycyna", 2, 4.8, "987654", "Gdańsk, ul. Zielona 15", "700-800-900", "piotr.wisniewski@example.com")

print(auto1.przedstaw())
print(auto2.typ_paliwa())
auto3.zmien_kolor("Czarny")
print(auto3.przedstaw())

print(telefon1.przedstaw())
telefon2.zmien_kolor("Złoty")
print(telefon2.przedstaw())

print(student1.przedstaw())
student3.popraw_ocene(5.0)
print(student3.srednia_ocen)

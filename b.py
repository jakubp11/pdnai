class Matma:
    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b

    @staticmethod
    def pomnoz(a, b):
        return a * b

    @staticmethod
    def podziel(a, b):
        if b == 0:
            return "Nie można"
        return a / b

    @staticmethod
    def potega(pod, wyk):
        return pod ** wyk

    @staticmethod
    def pierwiastek(n):
        if n < 0:
            return "Nie można"
        return n ** 0.5


    @staticmethod
    def srednia(lista):
        if not lista:
            return 0
        return sum(lista) / len(lista)

    @staticmethod
    def minimum(lista):
        if not lista:
            return None
        return min(lista)

    @staticmethod
    def maksimum(lista):
        if not lista:
            return None
        return max(lista)

    @staticmethod
    def czy_parzysta(n):
        return n % 2 == 0

    @staticmethod
    def czy_pierwsza(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
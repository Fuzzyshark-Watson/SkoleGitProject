"""
Fil-struktur: Tildele passende filer til passende mapper
Repo: For at holde alt skolerelateret samlet, vælges samme repo
Adgangskontrol: Privat repo med contributer
Struktur i filer:
    - Navngivning: Tilpasset navn af fil der indikere hvad filen/metoden gør
    - Kommentar: Bruges til at forklare hvad en metode eller funktion gør, eller hvordan den fungere.
    - Variabler/Metoder: Navngiv dem efter funktionalitet
Commit besked: Hvad committet har ændret
Branch: Flere kan arbejde på samme projekt uden at redigere på det oprindelige projekt
Code review: Fungere de forskellige branches sammen og kan merges til main
"""

class Lommeregner(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2
    
    def multiplication(self):
        return self.num1 * self.num2
    
    def division(self):
        if self.num2 == 0:
            return 0
        return self.num1 / self.num2
    
if __name__ == "__main__":
    obj = Lommeregner(1, 3)
    print(obj.addition())
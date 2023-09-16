from faker import Faker
import random

fake = Faker()


class BaseContact:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

    def contact(self):
        print(f"Wybieram numer {self.telefon} i dzwonie do {self.imie} {self.nazwisko}")

    @property
    def label_length(self):
        return len(self.imie + " " + self.nazwisko)
    
class BusinessContact(BaseContact):
    def __init__(self, imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy):
        super().__init__(imie, nazwisko, telefon, email)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon_sluzbowy = telefon_sluzbowy

    def contact(self):
        print(f"Wybieram numer {self.telefon_sluzbowy} i dzwonie do {self.imie} {self.nazwisko} w firmie {self.firma}")


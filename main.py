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
    

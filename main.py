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

def create_contact(rodzaj_wizytowki, ilosc):
    contacts = []

    for _ in range(ilosc):
        imie = fake.first_name()
        nazwisko = fake.last_name()
        telefon = fake.phone_number()
        email = fake.email()
        if rodzaj_wizytowki == "base":
            contact = BaseContact(imie, nazwisko, telefon, email)
        elif rodzaj_wizytowki == "business":
            stanowisko = fake.job()
            firma = fake.company()
            telefon_sluzbowy = fake.phone_number()
            contact = BusinessContact(imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy)
        contacts.append(contact)
    return contacts

#Przyklad uzycia kratora wizytowek

ilosc_wizytowek = 5
rodzaj_wizytowki = random.choice(["base", "business"])
wizytowki = create_contact(rodzaj_wizytowki, ilosc_wizytowek)

for wizytowka in wizytowki:
    wizytowka.contact()
    print(f"Dlugosc imienia i nazwiska: {wizytowka.label_length}")
    print()
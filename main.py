from Auta import Auta
from Budynek import Budynek
import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error
import sys


dom1 = Budynek(7)
print(dom1.liczba_pieter)

auto1 = Auta(5, 2018)
print(auto1.drzwi, auto1.produkcja)
auto1.wyswietl()
auto1.sprawdz_drzwi()
auto1.otworz_drzwi()
auto1.sprawdz_drzwi()
auto1.zamknij_drzwi()
auto1.sprawdz_drzwi()

#try:
#    with connect(
#        host = "localhost",
#        user = input("Enter username: "),
#        password = getpass("Enter password: ")
#    ) as connection:
#        print(connection)
#except Error as e:
#    print(e)

print(sys.getsizeof(auto1))
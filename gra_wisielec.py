import random
from colorama import Fore, Back

def printBlue(data):
    print(Fore.BLUE,data,end="",sep="")

def printRed(data):
    print(Fore.RED,data,end="",sep="")

def printYellow(data):
    print(Fore.YELLOW,data,end="",sep="")



def slowoNaLitery(slowo):
    litery = []
    for el in slowo:
        litery.append(el)
    return litery

def wyswietlListe(lista):
    for el in lista:
        print(el, end=" ")
    print()

def odgadywanie(litery):
    i = 0
    odgadywane = []
    while i<len(litery):
        odgadywane.append('_')
        i+=1
    return odgadywane


print()
print()
printYellow('~~~~~~~~WISIELEC~~~~~~~~~')
print('\n')
printYellow("zasady gry -> 'z'\ngraj -> 'g'\n")

odp = 'g' #input('>')
if odp == 'z':
    print('zasady gry... *w trakcie budowy*')

hasla = ['samolot']

slowo = random.choice(hasla)

litery = slowoNaLitery(slowo)
odgadywane = odgadywanie(litery)

wyswietlListe(odgadywane)


while True:
    l = input('> ')
    print()
    i = 0
    for el in litery:
        if el == l:
            odgadywane.pop(i)
            odgadywane.insert(i, l)
        i+=1

    wyswietlListe(odgadywane)









print('\n\n\n')

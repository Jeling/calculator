import sys
import os

def cls():
    os.system('cls')

def get_data():
    action = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

    if (action == '1'):
        addition()
    elif (action == '2'):
        subtraction()
    elif (action == '3'):
        multiplication()
    elif (action == '4'):
        division()
    else:
        print("Podaj poprawną wartość")

def get_quantity():
    numbers_table = []
    quantity = int(input("Ile liczb chcesz podać? "))
    for number in range (1, quantity+1):
        number = float(input("Podaj składnik %s: " % number))
        numbers_table.append(number)
    return numbers_table

def addition():
    numbers_table = get_quantity()
    result = sum(numbers_table)
    print(f"""Suma podanych liczb wynosi {result}""")

def subtraction():
    a = float(input("Podaj składnik 1: "))
    b = float(input("Podaj składnik 2: "))
    print(f"""Różnica {a} i {b} wynosi {a-b}""") 

def multiplication():
    result = 1.0
    numbers_table = get_quantity()
    for num in range(len(numbers_table)):
        result = numbers_table[num] * result 
    print(f"""Iloczyn podanych liczb wynosi {result}""")

def division():
    a = float(input("Podaj składnik 1: "))
    b = float(input("Podaj składnik 2: "))
    if b != 0:
        print(f"""Iloraz {a} i {b} wynosi {a/b}""")
    else:
        print("Nie można dzielić przez 0")

def again():
    run_again = input("Jeszcze raz? T/N ")

    if run_again.upper() == "T":
        cls()
        main()
    elif run_again.upper() == "N":
        print("Do zobaczenia")
    else:
        again()

def main():
    
    cls()

    get_data()
    
    again()


main()
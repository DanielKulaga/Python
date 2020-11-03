#Zadanie 3.3
for i in range (31):
    if (i % 3) != 0:
        print(i)
#Zadanie 3.4
while True:
    x = input( "Podaj liczbę, ktora chcesz podniesc do 3 potegi: ")
    if x == "stop":
        break
    try:
        x = float(x)
    except ValueError:
        print("To nie jest liczba")
    else:
       K = x, pow(x,3)
       print(K)
#Zadanie 3.5
size = input("Podaj dlugosc linijki:")
size_i = int(size)
linijka = "   |"

for i in range(size_i):
    linijka += "'''|"

print("Linijka o dlugosci:\n" + size +"\n" + linijka)

for x in range(size_i+1):
    print("{0:4}".format(x), end="")
print("\n")

#Zadanie 3.6
while True:
    num_of_lines = input("Podaj liczbe wieszy:")
    num_of_columns = input("Podaj liczbe kolumn: ")
    try:
        num_of_lines = int(num_of_lines)
        num_of_columns = int(num_of_columns)
    except ValueError:
        print("To nie jest  liczba calkowita")
    else:
        break

line ="|"
column ="+"
grid = ""
for i in range (num_of_lines):
    column=column + "---+"
    line = line + "   |"
    grid = (column + "\n" + line +"\n") * num_of_columns + column
print(grid)

#Zadanie 3.8
#Lista wszytskich elementów z obu sekwencji bez powtórzeń
sek_1 = "rododendron"
sek_2 = "dendryt"
L1 = list(sek_1)
L2 = list(sek_2)

print(L1)
print(L2)
print("Lista wszystkich elementów z obu sekwencji bez powtórzeń:")
print(set(L1) | set(L2)) #suma zbiorow

#Lista elementów powtarzajacych sie w obu listach
print("Lista elementów powtarzajacych sie w obu listach")
print(set(L1) & set(L2)) #przeciecie zbiorow

#Zadanie 3.9
sequence =[(1,2),(2,4,5),[],[4,1],(2323,33,33)]
result =[]
for item in sequence:
    sum_of_element = sum(item)
    result.append(sum_of_element)
    #Wykorzystanie funkcji assert, jesli nic sie nie dzieje to dobrze
assert result == [3, 11, 0, 5, 2389 ], "ERROR IN SUMMING"

#Zadanie 3.10
roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def romantoint(number):
    return roman_numbers.values(number)

def wholeRomanToInt(number_r):
    value =0
    list(number_r)
    for i in range (len(number_r)):
        if i > 0 and roman_numbers[number_r[i]] > roman_numbers[number_r[i-1]]:
            value += roman_numbers[number_r[i]] - 2 * roman_numbers[number_r[i-1]]
        else:
            value += roman_numbers[number_r[i]]
    return value

L = input("Podaj liczbe rzymska: ")
print(str(wholeRomanToInt(L)) + " to twoja rzymska liczba zapisana po arabsku")



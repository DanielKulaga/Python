#Zestaw 4
#Zadanie 4.2
# zadanie 3.5 jako funkcja
def draw_ruler(n):
    #size = input("Podaj dlugosc linijki:")
    #size_i = int(size)
    linijka = "   |"

    for i in range(n):
        linijka += "'''|"
    linijka+="\n"

    #print("Linijka o dlugosci:\n" + n + "\n" + linijka)

    for x in range(n + 1):
        linijka += str("{0:4}".format(x))


    return linijka
print(draw_ruler(12))
#return
#Zadanie 4.2 jako Zadanie 3.6
def draw_grid():
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

    line = "|"
    column = "+"
    grid = ""
    for i in range(num_of_lines):
        column = column + "---+"
        line = line + "   |"
        grid = (column + "\n" + line + "\n") * num_of_columns + column
    return grid
#Zadanie 4.3
number1 = 4
n = 5
def factorial (number1, n):
    last = 1
    while n > 0:
        result1 = last * number1
        last = result1
        n = n-1
    return last
assert factorial(number1,n) == pow(number1,n)

#Zadanie 4.4
def fibonacci (n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    a = 0
    b = 1
    for i in range (n):
        b = a + b #pod b a+b
        a = b - a
    return a
assert fibonacci(6) == 8

#Zadanie 4.5
#iteracyjnie

L = [1, 2, 3, 4, 5, 6, 7]
L1 = [1, 2, 3, 4, 5, 6, 7]
def reverse_list_iter(L, left, right):
    r = right
    l = left
    for i in range(int(len(L)/2)):
        w = L[r]
        L[r] = L[l]
        L[l] = w
        l = l + 1
        r = r - 1
    return L
reversed_list = L [::-1]
print(reverse_list_iter(L,0,6))
print(reversed_list)


#rekurencyjnie
L2 = [3, 4, 5, 6, 7, 8, 9, 0]
def reverse_list_rek(L2,l,r) :
    t = L2[r]
    L2[r] = L2[l]
    L2[l] = t
    if l < r:
        reverse_list_rek(L2,l+1,r-1)
    return L2

print("\n"+ str(L2))
print(reverse_list_rek(L2, 0, 7))

#Zad 4.6
sequence_1 = [23, 4, 56, (4, 5), [10, 1], 2]
def sum_seq(sequence):
    sum_of_sequence = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            sum_of_sequence += sum_seq(item)
        else:
            sum_of_sequence = item + sum_of_sequence
    return sum_of_sequence
assert sum_seq(sequence_1) == 105

#sequence_2 = [8, (7,9), (8,9), [23, 4, 56, (4, 5), [10, 1], 2]]
#Zad 4.7
def flatten(sequence):
    sum_of_sequence = 0
    new_sequence = []
    for item in sequence:
        if isinstance(item,(list,tuple)):
            new_sequence = new_sequence + flatten(item)
        else:
            new_sequence.append(item)
    return new_sequence
print("\nSekwencja do spłaszczenia:" + str(sequence_1))
print ("Spłaszczona sekwencja :" + str(flatten(sequence_1)))






#Zadanie 2.10
line = """""""""Pletwal 
blekitny    jest
najwiekszy       ssakiem,
na          planecie 
Ziemia  ."""""""""

words = line.split()
print("Ilosc slow to:" + str(len(words)))

#Zadanie 2.11
word = "Subiektywny"
print("_".join(word))

#Zadanie 2.12
first_letters = [word1[0] for word1 in words]
print("".join(first_letters)) #wyraz z pierwszych liter
last_letters = [word2[-1:] for word2 in words]
print("".join(last_letters)) #wyraz z ostatnich liter

#Zadanie 2.13
sum_of_letters = sum([len(word3) for word3 in words])
print("Laczna dlugosc wyrazow to: " + str(sum_of_letters))

#Zadanie 2.14
#Najdluzszy wyraz i jego dlugosc
num_of_longest_word = max([len(word3) for word3 in words])
print("Dlugosc najdluzszego slowa to: " + str(num_of_longest_word))
for word4 in words:
    if len(word4) == num_of_longest_word:
        print("Najdluzsze slowo to: " + word4)

#Zadanie 2.15
L = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15]
#text = [L[i] for i in range (0,len(L))]
#text = str(L)[1:-1]
#text.split(",")
print("Napis zlozony z kolejnych cyfr w tablicy: " + ''.join(str(x) for x in L ))

#Zadanie 2.16
line1 = "adasdasdasdbhGvRjfsrasdasd sfsfsdf gbr ssdff fgggd"
print(line1)
print(line1.replace("GvR","Guido van Rossum"))

#Zadanie 2.17
line2 ="Wisla to najdłuższa rzeka Polski, a także najdłuższa rzeka uchodząca do Morza Bałtyckiego"
words_to_sort = line2.split()
alphabet_sort = sorted(words_to_sort,key=str.lower)
length_sort = sorted(words_to_sort,key = len)
lenght_sort_reverse = sorted(words_to_sort, key=len, reverse=True)

print("Posortowane slowa alfabetycznie: " + str(alphabet_sort))
print("Posortowane slowa pod względem dlugosci od min do max:" + str(length_sort))
print("Posortowane slowa pod względem dlugosci od max do min:" + str(lenght_sort_reverse))

#Zadanie 2.18
longnumber = 12700912709701328018309377170971209730980870137701090
longnumber_changed = str(longnumber)
number_of_characters = 0
for char in longnumber_changed:
    if char == '0':
        number_of_characters += 1

print("Liczba zer w podanej liczbie wynosi: " + str(number_of_characters))

#Zadanie 2.19

L = [145, 23, 1, 14, 34, 345, 390, 5, 69]
for i in range(0,len(L)) :
     L[i] = str(L[i]).zfill(3)
print("Napis z potrojnych blokow:  ", L)




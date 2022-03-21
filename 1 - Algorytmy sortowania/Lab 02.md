# Sortowanie 2

## Definicje

- Złożoność algorytmiczna algorytmow opartych o porównanie wynosi $\Omega(n \logn)$

## Quicksort

Przykładowa lista:

$$
[5,6,4,2,8,3,1,7]
$$

- Algorytm działający na zasadzie 'dziel i rządź'
- Jest to metoda rekurencyjna

- Wybieramy 2 (środek) jako pivot, element dzielący
	- Rozdzielamy mniejsze z lewej, większe z prawej
	- z lewej szukamy elementów $A[i] \geq x$
	- napotykamy 5 jako pierwszy element z lewej większy od 2
	- z prawej szukamy elementów $A[i] \leq x$
	- napotykamy 1 jako pierwszy element z prawej mniejszy od 2
	- zamieniamy 5 z 1

- Mamy pivot 2
	- z lewej 6 napotkane
	- z prawej dwójka jest równa
	- zamieniamy 6 i 2

- Pivot sie nie zmienia, teraz jest na indexie 1
	- Z lewej teraz są mniejsze, z prawej większe

Tablica teraz:

$$
[1,2,4,6,8,3,5,7]
$$

Teraz zablice dzielimy i wywołujemy rekurencyjnie:
- Quicksort dla tablicy $[1,2]$
	- Dla niej się od razu kończy bo jest posortowane
- Quicksort dla tablicy $[4,6,8,3,5,7]$
	- 8 jako pivot
		- z lewej na 8
		- z prawej na 7
		- zamieniamy

## Przypadki

O efektywności tego algorytmu decyduje ilość wywołań rekurencyjnych

- Najgorszy przypadek
	- Kiedy największy/najmniejszy zawsze jest na środku mamy $O(n)$ podziałów, czyli złożoność $O(n^2)$

- Optymistyczny przypadek, również średni
	- Dzielimy zawsze na 2, $O(\log[2]n n$
	- Jest przy medianie jako pivot, czyli tablicy posortowanej

- Znajdywanie mediany (żeby łatwo znaleźć pivota)

- Ulepszanie
	- Kończenie wcześniej rekurencji (np przy 2 elementach, lub przy 100 dla algorytmów prostych)

- Pamięć
	- Obsługa rekurencji wymaga pamięci
	- w najgorszym przypadku zagłębienie rekurencji to $n$

## Sortowanie przez scalanie (Merge sort)

Przykładowa lista:

$$
[5,6,4,2,8,3,1,7]
$$

- Dzieli tablice na pół, aż dojdzie do jednoelementowych tablic (etap podziału)

- Porównujemy 5 i 6
	- Zostaje takie samo
- Porównujemy 4 i 2
	- 2 i 4
- Porównujemy $[2,4]$ i $[5,6]$
	- porównujemy szczyty tych stosów (2 i 5)
	- 2, potem 5 i 4
	- Jak 2,4 jest juz wyczerpane to mozna przepisac pierwszta tablice
	- $[2,4,5,6]$
- ...

## Przypadki

Złożoność czasowa:
- $O(\log[2]n)$ podziałów w etapie podziału
- $O(\log[2]n)$ scaleń * $n$ operacji
- $O(n \log[2]n)$ - złożoność w przypadku optymistycznym, neutralnym i pesymistycznym

Złożoność przestrzeni:
- dodatkowe zapotrzebowanie pamięciowe (tablica wynikowa)
- $O(n)$ - nie działa w miejscu
- Nie jest wrażliwy na dane wejściowe (stała złożoność)

Dobre jeśli mamy górna granice czasową:
- Limit górny jest mniejszy w merge sorcie
- Unika się ogromnego skoku quicksorta
- Np decyzja samochodu autonomicznego

## Sortowanie stogowe (przez kopcowanie) - Heap sort

Strutkura danych - stóg, kopiec, sterta
- struktura drzewiasta
	- drzewo binarne
	- wejściowo posortowane
	- liście we 2 ostatnich poziomach

Jest to rozszerzenie metody selection sort

Jeśli narzucimy takie warunki na tablice to będzie to kopiec:
	-$A[i]\geq A[2i]$
	-$A[i]\geq A[2i+1]$

Przykładowa lista:

$$
[5,6,4,2,8,3,1,7]
$$

```
5 ma dzieci 6,4
6 ma dzieci 2,8
2 ma dzieci 7
4 ma dzieci 3,1

Nie jest to kopiec!
```

## Budowa kopca

Budujemy liste tak, aby nasza relacja wyżej była spełniona

Wystarczy sprawdzać od połowy tablicy czy ta relacja jest prawdziwa, porównujemy z gałęzią wyżej, jeśli tak to zamieniamy, dopóki niżej nie będzie niżej mniejszych

- Zamieniamy pierwszy (najwiekszy) z ostatnim nieposortowanym
- Stóg jest zepsuty, trzeba go odbudować, tak samo jak na początku

## Przypadki

- $n-1$ iteracji max
	- 1 zamiana
	- odbudowa stogu
	- daje to max $O(\log[2] n)$
	- minimalnie $O(1)$

- Średnio daje to O(n \log[2]n) dla pesymistycznego, średniego
- Optymistyczny $O(n)$

## Sortowanie przez zliczanie - Counting sort

Przykładowa lista:

$$
[3,6,4,1,3,4,1,4]
$$

Nadaje się do sortowania liczb całkowitych z wąskiego zakresu

W naszej tablicy największa wartość $k=6$:
-	maksymalna wartość musi być $O(n)$

Dodatkowa tablica o wielkości zakresu naszych elementów (6)

Tablica counting:

$$
[2,0,2,3,0,1]
$$

Musi być wąski zakres!

## Przypadki

- Duże wymaganie pamięciowe
- Kompletna niewrażliwość na dane
- Zakres i liczba elementów wpływają na czas

## Sotrowanie pozycyjne

Całkowite o tej samej precyzji (ilość liczb):

- Patrzymy na ostatnie cyfry - robimy tam counting sort
- Potem sortujemy po drugiej pozycji
- Potem po trzeciej

# Sortowanie

## Definicje

- Sortowanie
	- Ustalenie sekwencji elementów
	- Metod sortowanie jest co najmniej kilkanaście
	- Patrzymy czym się różnią

- Funkcja złożoności obliczeniowej
	- Określa max ilość kroków wykonywanych przez DTM (deterministyczna maszyna turinga) dla instancji o określonym rozmiarze

- Instancja
	- Konkretne dane
	- Rozmiar instancji to długość łancucha kodującego dane

- Stabilność algorytmu
	- Zachowanie wejściowej kolejności elementów o tym samym kluczu

## Proste wstawianie (Insertion sort)

Przykładowa lista:

$$
[5,6,2,4,8,3,1,7]
$$

- Dzielimy ciąg na dwie części
	- część posortowaną i nieposortowaną
	- na początku tylko pierwszy element jest w części posortowanej.

- Porównujemy pierwszy element
	- Tutaj 6 jest wieksze od 5 (nic sie nie zmienia)
	- Część posortowana zwiększa się do: $[5,6]$

- W przypadku dwójki
	- Porównujemy ją z 6, jest mniejsza (zamieniamy)
	- to samo z 5, jest mniejsza (zamieniamy)
	- Część posortowana zwiększa się do $[2,5,6]$

- W przypadku 4
	- Porównujemy z 6, jest mniejsza (zamiana)
	- Porównujemy z 5, jest mniejsza (zamiana)
	- Porównujemy z 2, jest wieksza (nic)
	- Część posortowana zwiększa się do $[2,4,5,6]$

### Czas i pamięć

- Zapotrzebowanie pamięciowe
	- Stała liczba zmiennnych - działa **w miejscu**

- Efektywność czasowa
	- $O(n^2)$

### Przypadki

- Przypadek optymistyczny
	- ciąg posortowany ($O(n)$, ponieważ mamy $n$ iteracji)

- Przypadek pesymistyczny
	- ciąg odwrotnie posortowany ($O(n^2), dalej mamy $n$ iteracji, ale o 1 wiecej porownan za kazdym razem)

- Zachowaniem naturalnym
	- optymistyczny to posortowane dane
	- pesymistyczny to odwrotnie posortowane

- Algorytm jest wrażliwy na układ danych
	- między najgorszym a najlepszym przypadkiem jest $n$ różnicy

## Proste wybieranie (Selection sort)

Przykładowy ciąg liczbowy:

$$
[5,6,2,4,8,3,1,7]
$$

- Dzielimy na ciąg posortowany i nieposortowany
- Na początku tylko pierwszy element
- Znajdujemy najmniejszy element z nieposortowanej
- Zamieniamy z pierwszym nieposortowanym

- Przykładowy przypadek:
	- Tutaj zamieniamy 5 z 1
	- Potem 6 z 2
	- Potem 6 z 3

### Czas i pamięć

- Zapotrzebowanie pamięciowe
	- Stała liczba zmiennnych - działa **w miejscu**

- Efektywność czasowa
	- $n-1$ iteracji
	- Operacje w ramach poszczególnej iteracji
		- Żeby znaleźć minimum, trzeba zawsze przejrzeć całą nieposortowaną część
			- $n$
			- $n-1$
			- $n-2$
	- Przypadek optymistyczny, średni i pesymistyczny to $O(n^2)$
	- Jest wolny, nie jest w stanie przyśpieszyć

- Właściwości
	- Niewrażliwy na układ danych
	- Bardzo słabe zachowanie naturalne (praktycznie 0 różnicy między optymistycznym i pesymistycznym)
	- Algorytm nie jest stabilny

## Sortowanie bąbelkowe (Bubble sort)

Przykładowy ciąg liczbowy:

$$
[5,6,2,4,8,3,1,7]
$$

- Idziemy od końca tablicy
- Porównujemy je od końca parami

- Siedem z jeden, nic
- Jeden z osiem, zamiana
- ...
- Jedynka przechdozi na sam początek

### Przypadki

- Złożoność czasowa
	- $n-1$ iteracji - $O(n^2)$

- Właściwości
	- Nie jest wrażliwy na rozkład danych
	- Bardziej naturalny niż selection sort (większa różnica)
	- Jest stabilny

### Ulepszenia

- Wykrycie posortowanie (binarna flaga "czy była zamiana?")
	- Przypadek optymistyczny (posortowane dane)
		- Liczba iteracji spada do $n$

- Zapamiętanie pozycji ostatniej zmiany
	- Jak nie trzeba zmieniać np dwóch ostatnich elementów to można je "wykluczyć", żeby nie marnować porównań
	- Redukuje to liczbę porównań, ale nie zamian (poprawia czas, ale nie iteracje)

## Shaker sort

- Bubble sort, tylko że wykonywane asymetryczne
	- Każda kolejna iteracja jest od innego końca (początek -> koniec -> początek itd.)

## Metoda Shella (Shell sort czyli malejące przyrosty)

Przykładowy ciąg liczbowy:

$$
[5,6,2,4,8,3,1,7]
$$

- Bierzemy element 5 i 8 (o 4 od siebie)
	- Sortujemy je jakby nic innego nie istniało

- Bierzemy element 3 i 6 (o 4 od siebie)
	- Sortujemy je jakby nic innego nie istniało

- ...

- Potem robimy gęstsze sito (na przykład co 2)
	-	Insertion sort dla $[5,1,8,2]$

- Na koniec sito co 1

### Przypadki

-	Złożoność obliczeniowa $O(n^{1.2})$
	- Trzeba dobrać taką odległość, żeby był optymalny
	- Zwykle iteracje to
		-	$n_1=1$ - sito ostatnie to zawsze 1
		-	$n_{t+1}=3n_t+1$ - sito ostatnie to zawsze 1

# Grafy jako struktury do modelowania problemów

Graf skierowany $G=(V,E)$

- $E$ to krawędź. Nie mają kierunków
- Symetryczny charakter problemu (sąsiedztwo państw)
  - Kolorowanie wierzchołków

Graf nieskierowany to $G=(V,A)$

- $A$ to arc
- Łuk może być łączony sam ze sobą
- Jeśli to mapa - dodajemy etykiety (np długość)
  - Mamy wtedy graf etykietowany

Graf jest strukturą abstrakcyjną

## Reprezentacje maszynowe grafu

Przykładowy graf:

![](/home/Adam/.config/marktext/images/2022-04-01-12-01-07-image.png)

### Macierz sąsiedztwa

$$
P=n\times n = O(n^2)
$$

|     | 1   | 2   | 3   | 4   | 5   | 6   |
| --- | --- | --- | --- | --- | --- | --- |
| 1   | 0   | 1   | 1   | 0   | 0   | 0   |
| 2   | 0   | 0   | 0   | 0   | 0   | 0   |
| 3   | 0   | 0   | 0   | 1   | 0   | 0   |
| 4   | 1   | 0   | 0   | 0   | 0   | 1   |
| 5   | 0   | 1   | 0   | 1   | 0   | 0   |
| 6   | 0   | 0   | 0   | 0   | 0   | 1   |

Cechy:

- Im rzadszy graf (mniej łuków) tym mniej się opłaca

- Jedyna struktura implementowana na bitach (istnieje możliwość implementacji bitowej)

Algorytmy często sprawdzają czy są sąsiadujące (test łuku)

- Na przykład czy możemy z portu nr 5 przelecieć do portu nr 1

- Adresowanie - $O(1)$ - nic lepiej nie działa dla tej operacji

Algorytmu często wyznaczają zbiory następników

- Algorytm jest w jakimś wierzchołku i sprawdza gdzie może iść dalej

- Sprawdzamy cały wiersz (np w przypadku wiersza 4 przechodzi cały wiersz)

- $O(n)$ dla wszystkich następników

- Dla pierwszego następnika od $O(1)$ do $O(n)$

Zbiór poprzedników

- Idziemy po kolumnach - $O(n)$

- Pierwszy poprzednik od $O(1)$ do $O(n)$

Zbiór łuków

- $O(n^2)$

W grafie nieskierowanym mamy symetryczną tablicę tzn. $[3][2]=1$ to $[2][3]=1$

- jest tam zbiór sąsiadów zamiast poprzedników i następników - też $O(n)$

### Listy następników

Hierarchia danych - $P(n+m)$, gdzie jest $m$ łuków

![](/home/Adam/.config/marktext/images/2022-04-01-12-13-13-image.png)

Im rzadsza jest lista, tym jest bardziej oszczędna pamięciowo (teoretycznie bo tamtą można zrobić na bitach). Jest to tablica list

Test łuku

- Do przejrzenia jest lista

- od $O(1)$ do $O(n)$

- średnio $O(\frac{n}m)$

Następniki

- Adresujemy, przeglądamy

- $O(n)$ z minimalną liczbę operacji zależną od następników

Poprzedniki

- Trzeba przejrzeć wszystkie listy i szukać poprzednika

- Szukamy 4 przez cała listę w każdym indeksie i jak znajdziemy to zwracamy indeks

- Może przejść całą listę - $O(n+m)$

Zbiór łuków

- Zawsze trzeba przejść całą strukturę

- $O(n+m)$

### Listy poprzedników

Tak jakbyśmy macierz kolumnami czytali

![](/home/Adam/.config/marktext/images/2022-04-01-12-20-17-image.png)

Test łuków

- To samo

Sprawdzanie następników

- Tak jak poprzedniki wcześniej

Sprawdzanie poprzedników

- Tak jak następniki wcześniej

Lista łuków

- Tak jak wyżej

### Obie wyżej to listy sąsiedztwa (w nieskierowanym)

Niektóre algorytmy usuwają krawędź lub łuk

![](/home/Adam/.config/marktext/images/2022-04-01-12-22-37-image.png)

Wszystko jest podwójnie, musimy w dwóch miejscach usuwać

### Lista łuków

Tablica dwuelementowa

![](/home/Adam/.config/marktext/images/2022-04-01-12-24-00-image.png)

$P=O(m)$ - Każdy łuk zajmuje dwie komórki, najlepiej dostosowuje się do gęstości grafu

Test łuku

- Wyszukiwanie liniowe

- $O(m)$ lub w posortowanej $O(\log m)$

Test następników

- W najgorszym przypadku - $O(m)$

Test poprzedników

- W najgorszym przypadku - $O(m)$

Zbiór łuków

- $O(m)$

### Macierz incydencji

$P=O(n * m)$

Tyle wierszy ile jest wierzchołków i tyle kolumn ile jest łuków

| 1   | -1  | -1  | 0   | 1   | 0   | 0   | 0   | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2   | 1   | 0   | 0   | 0   | 0   | 1   | 0   | 0   |
| 3   | 0   | 1   | -1  | 0   | 0   | 0   | 0   | 0   |
| 4   | 0   | 0   | 1   | -1  | -1  | 0   | 1   | 0   |
| 5   | 0   | 0   | 0   | 0   | 0   | -1  | -1  | 0   |
| 6   | 0   | 0   | 0   | 0   | 1   | 0   | 0   | 2   |

Test łuku

- Po dwóch wierszach jednocześnie sprawdzamy gdzie jest -1 oraz 1

- $O(m)$

Następniki i poprzedników

- Szukamy pierwszego -1 albo 1, potem na kolumnę patrzymy

- $O(n*m)$

Wszystkie łuki

- $O(n*m)$

W hiper grafach, gdzie pojedyncza krawędź jest zbudowana z wielu połączeń możemy zapisać je w macierzy incydencji.

## Algorytmy grafowe

Implementując musimy dobrać reprezentacje, sprawdzamy co chce robić nasz algorytm i dobieramy do tego implementacje

### Przeglądanie grafu

Dwie podstawowe strategie, zaczynamy od pierwszej etykiety (dla algorytmu to nie ma znaczenia)

![](/home/Adam/.config/marktext/images/2022-04-01-12-35-11-image.png)

#### DFS - Depth first search - "w głąb"

Wykorzystywana struktura - stos

- 1 - kładziemy na stosie
  
  - 2 - do najmniejszej etykiety (nie musimy), dajemy na stos
  
  - 4 - kładziemy na stos
  
  - 6-> 5 -> 8 -> 9

- Zdejmujemy 9 ze stosu i nie ma nieodwiedzonych i zdejmujemy aż do 6
  
  - Do 7 kładziemy na stosie potem 3
  
  - W trójcie utknęliśmy
  
  - Cofamy się do 7 i do 6

- Idziemy do 13, zdejmujemy 13 i 6 bo już nie ma nieodwiedzonych

- Idziemy z 4 do 12
  
  - Kładziemy 10 i 11 na stosie

- Zdejmujemy wszystko ze stosu

Stos jest pusty, ale nie skończyliśmy 

- restartujemy procedurę od pierwszego lepszego nieodwiedzonego wierzchołka
- Jeśli nie ma restartu - jest spójny
- Jeśli mamy restart i jest niespójny to wiemy ile jest niepołączonych
- Wiemy jakie wierzchołki są osiągalne z punktu startowego
- Las rozpinający - najmniejszy podgraf spójny
- Jeśli przykład byłby spójny to byłoby drzewo rozpinające

$$
[1,2,4,6,5,8,9,7,3,13,12,10,14,15]
$$

$n$ operacji, jak cofaliśmy się to sprawdzaliśmy dodatkowe wierzchołki i jest robione raz - $O(n+m)$  dla listy sąsiadów bądź listy następników dla skierowanego.

#### BFS - Breadth first search - "wszerz"

Wykorzystywana struktura - kolejka. Ten sam graf co wyżej.

Zaczynamy na 1

- Idziemy do wszystkich sąsiadów jeden po drugim

- do 2,4 oraz do 12

- Kolejka to  1,2,4,12

- Jak nie ma gdzie pójść do zdejmujemy 1, potem 2

Kolejka to $4,12$

- Najpierw do 6,7

- Kolejka do 4,12,6,7

- 4 usuwamy

Kolejka to 12,6,7

- Z 12 do 10,11

- 12,6,7,10,11

- Usuwamy 12 bo nie ma już

Kolejka to 6,7,10,11

- Do 5,9,13

- 6,7,10,11,5,9,13

- 6 usuwamy

Kolejka to 7,10,11,5,9,13

- Z 5 do 5,9,13,3,8

- Zdejmujemy wszystko kolejka jest pusta

- Restartujemy od pierwszego nieodwiedzonego (14)

Końcowy zapis to

$$
[1,2,4,12,6,7,10,11,5,9,13,3,8,14,15]
$$

$O(m+n)$ dla listy sąsiedztwa lub następników.

- Wszystkie ścieżki są najkrótsze (liczone w krawędziach)

### Sortowanie topologiczne

Dla grafów skierowanych acyklicznych

- kolejność wykonywania czynności, co musi coś poprzedzać,

![](/home/Adam/.config/marktext/images/2022-04-01-13-01-31-image.png)

Jeśli $(u,v)\in A$ to $u$ poprzedza $v$. Aby posortować topologicznie należy użyć algorytmu opartego na DFS. 

- $d[v]$ etykieta startowa analizy (położenie na stosie)

- $f[v]$ - etykieta końcowa (zdjęcie ze stosu)

Porządek topologiczny - malejąca $f[v]$. Poniżej jest wykres w którym kroku nadana została etykieta

| $v$    | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $d[v]$ | 1   | 2   | 3   |     | 7   |     |     |     | 4   |
| $f[v]$ | 10  | 9   | 6   |     | 8   |     |     |     | 5   |

Skoro wcześniej zaczęliśmy od 1 etykietę więc odwiedzamy 2. Po 10 krokach mamy powyższą tabelę. Bierzemy pierwszy nieodwiedzony wierzchołek, czyli pierwsza nieustawiona etykieta.

| $v$    | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $d[v]$ | 1   | 2   | 3   | 11  | 7   | 13  | 15  | 16  | 4   |
| $f[v]$ | 10  | 9   | 6   | 12  | 8   | 14  | 18  | 17  | 5   |

Porządek topologiczny - malejąca $f[v]$

![](/home/Adam/.config/marktext/images/2022-04-01-13-11-02-image.png)

Sprawdzamy czy nie ma loopów, łuków powrotnych - takie łuki które idą w prawo

$d[v] < d[u] < f[u] < f[v]$ <- wtedy jest powrotny

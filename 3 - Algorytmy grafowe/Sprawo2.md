## Wprowadzenie

W tym sprawozdaniu zbadaliśmy sposoby analizy grafów i ich reprezentacji maszynowych, byliśmy  w stanie dzięki temu zweryfikować wiadomości poznane w trakcie zajęć. Kod źródłowy został napisany w języku **python** ze względu na prostotę implementacji.

Zaimplementowaliśmy metodę sortowania topologicznego działającą w dwóch wyodrębnionych etapach: obliczającą dla każdego wierzchołka etykiety czasowe rozpoczęcia i zakończenia analizy oraz sprawdzającą acykliczność przez zliczanie łuków powrotnych. Wygenerowaliśmy 10 losowych grafów skierowanych $G=(V,A)$ o rożnych $|V|=n$.

## Reprezentacje maszynowe grafów

Grafy są strukturami abstrakcyjnymi, więc potrzebujemy reprezentacji maszynowej, by informacje w nich zawarte można było przetwarzać za pomocą komputera.

## Obliczanie etykiet czasowych w zależności od gęstości grafu

Etykiety czasowe to dwie unikalne wartości przydzielane każdemu wierzchołkowi oznaczające czas, w którym dany wierzchołek został włożony na stos, oraz z niego zdjęty podczas działania algorytmu DFS (Depth First Search, czyli wyszukiwanie "w głąb"). Algorytm działa w następujący sposób:

- Zaczynamy algorytm na dowolnym nieodwiedzonym wierzchołku w grafie.

- Dokładamy wierzchołek na stos

- Znajdujemy pierwszego nieodwiedzonego następnika, jeśli go nie ma - zdejmujemy ten wierzchołek ze stosu

- Wykonujemy kroki 2-4 dla każdego wierzchołka na szczycie stosu do momentu wyczerpania stosu. Jeśli po wyczerpaniu stosu graf dalej posiada wierzchołki nieodwiedzone, uruchamiamy DFS ponownie.

Złożoność algorytmu DFS to $O(n+m)$, gdzie $n$ to liczba wierzchołków w grafie, a $m$ to łączna ilość łuków. Dodatkowym nakładem czasowym przy wykonywaniu DFS jest sprawdzanie następników danego wierzchołka - czas tej operacji jest uzależniony od wybranej reprezentacji maszynowej grafu. Tworząc algorytm zliczający etykiety czasowe zauważyliśmy, że najbardziej trafną reprezentacją przy naszym zastosowaniu jest **lista następników**. Struktura ta działa w następujący sposób:

1. Tworzymy tablicę o szerokości $n$ elementów, gdzie $n$ to liczba wierzchołków

2. Do każdej komórki w tablicy wstawiamy listę następników dla danego wierzchołka

Ta reprezentacja pozwala na szybsze wyszukiwanie następników niż w macierzy sąsiedztwa, z racji ograniczenia ilości operacji do minimum. Lista następników posiada złożoność od $O(1)$ do $O(n)$ i była bardzo prosta do implementacji w języku **python**.

Najgorszą reprezentacją grafu dla wyszukiwania następnika jest macierz incydencji, gdzie aby znaleźć następnika dla danego wierzchołka trzeba liczyć się z czasem rzędu $O(n\times m)$, więc im większa jest gęstość grafu, tym mniej korzystna jest ta reprezentacja.  Gęstość grafu $d$ jest stosunkiem liczby łuków w danym grafie do największej możliwej liczby łuków (w grafie pełnym). Każdy nasz test spełniał zależność $m>n$, gdzie $m=d\times n\times (n-1)$ .

W następującej tabeli przedstawiliśmy przy dwóch gęstościach zależność czasu trwania etapu obliczania etykiet czasowych od liczby wierzchołków $n$.

##### ETYKIETY TABELA

Z wyników z stworzyliśmy następujący wykres:

##### ETYKIETY

Test obliczania etykiet czasowych został wykonany na liście następników. Można zaobserwować, że wraz ze wzrostem gęstości czas na obliczanie wszystkich etykiet również rośnie, dzieje się tak ponieważ gęstość wpływa na średnią ilość następników danego wierzchołka. Zwiększona gęstość grafu najbardziej wpływa na czas działania algorytmu przy reprezentacji, gdzie wyszukiwanie następnika zależy w dużym stopniu od ilości łuków. Reprezentacje, które są wrażliwe na gęstość to między innymi:

- Lista łuków - $O(m)$

- Lista poprzedników - $O(n+m)$

- Macierz incydencji - $O(n\times m)$

Macierz sąsiedztwa jest niewrażliwa na ilość istniejących łuków z racji czasu wyszukiwania następnika od $O(1)$ do $O(n)$, w tej strukturze zmiana gęstości grafu jest najmniej widoczna przy stałych wartościach $n$.

## Zliczanie łuków powrotnych

Zliczanie łuków powrotnych w przypadku naszego zastosowania odbywa się używając etykiet czasowych obliczanych przy przejściu algorytmu DFS - $d[v]$ jest etykietą startową analizy, a $f[v]$ jest etykietą zakończenia analizy. Sprawdzanie, czy dany łuk $(u,v)\in A$ jest powrotny wiąże się ze spełnieniem poniższej zależności: $d[v] < d[u] < f[u] < f[v]$. Jeśli ta zależność jest prawdziwa dla analizowanego łuku - wiemy, że jest on powrotny.

W poniższej tabeli przedstawiliśmy liczbę łuków powrotnych dla poszczególnych liczby wierzchołków $n$ oraz gęstości $d$.

#### TABELA

Nasz eksperyment wykazał znaczącą ilość łuków powrotnych w każdym grafie, przez co żaden graf analizowany podczas eksperymentu nie był acykliczny, co jest warunkiem koniecznym do sortowania topologicznego.

Jeśli uporządkujemy wierzchołki malejąco według etykiety zakończenia analizy $f[v]$ otrzymamy porządek topologiczny dla danego grafu skierowanego. Porządek topologiczny pozwala na ustalenie kolejności wykonywania operacji tak, aby nie doszło do kolizji - przykładowym zastosowaniem sortowania topologicznego jest unikanie konfliktów zależności przy instalowaniu wielu programów jednocześnie. W porządku topologicznym łuk powrotny jest łukiem, który dąży w odwrotnym kierunku do ustalonego i nie pozwala na praktyczne zastosowania takiego układu (w przypadku wcześniejszego przykładu zaszedłby konflikt zależności) - z tego powodu grafów cyklicznych nie można posortować topologicznie.

## Zliczanie łuków powrotnych dla różnych reprezentacji grafu

W tym teście sprawdziliśmy zależność czasu trwania etapu zliczania łuków powrotnych dla 3 reprezentacji grafu: macierzy sąsiedztwa, listy następników oraz listy łuków.  W naszej implementacji macierzy sąsiedztwa dla grafu skierowanego o wymiarze $n\times n$ wierzchołek o numerze wiersza jest poprzednikiem a wierzchołek o numerze kolumny jest następnikiem. Istnienie krawędzi między tymi dwoma wierzchołkami zaznaczane jest przez istnienie wartości 1 w danej komórce, w przeciwnym przypadku w komórce znajduje się wartość 0. Lista łuków jest natomiast tablicą dwuelementową, gdzie pierwszy element wstawiany to poprzednik, a drugi to następnik.

Operacją wykonywaną przy zliczaniu liczby łuków powrotnych jest sprawdzenie zbioru łuków. Najgorsza dla tej operacji jest macierz sąsiedztwa, w której zawsze musimy przejść całą macierz - jest to czas rzędu $O(n^2)$. Lista następników wykonuje tą operacje w czasie $O(n+m)$, jest przez to w dużym stopniu zależna od gęstości grafu. Najlepsza dla tej operacji jest lista łuków, gdzie cała lista jest zbiorem łuków - $O(m)$. 

Otrzymane wyniki przedstawiliśmy poniżej w dwóch tabelach, dla różnych wartości $d$

###### TABELA

###### TABELA 2

Z wyników stworzyliśmy następujący wykres

###### WYKRES

###### WYKRES 2

Porównując ze sobą oba wykresy warto zauważyć, że czas wykonywania przy macierzy sąsiedztwa jest prawie taki sam, podczas gdy reprezentacje zależne od wartości $m$ doświadczają prawie dwukrotnego zwiększenia czasu operacji.

## Podsumowanie

Wszystkie maszynowe reprezentacje grafów mają swoje wady i zalety - używając wiadomości poznanych w trakcie zajęć oraz doświadczeń wykonanych na potrzeby tego sprawozdania byliśmy w stanie sporządzić zbiór wad oraz zalet poznanych reprezentacji grafów.

Macierz sąsiedztwa ma dużą zaletę w postaci prostoty implementacji oraz małego śladu na pamięci - pozwala ona na stworzenie macierzy bitowej i zajęcia znacznie mniejszej ilości pamięci. Ma ona również szybkie czasy sprawdzania poprzedników i następników mieszczące się w $O(n)$ oraz żadna jej operacja nie jest zależna od ilości łuków $m$. Wadą tej reprezentacji jest niepraktyczność w sytuacji malej gęstości grafu.

Macierze incydencji znajdują swoje najlepsze zastosowanie w hipergrafach, gdzie pojedyncza krawędź może być zbudowana z wielu połączeń - żadna inna poznana reprezentacja nie pozwala na przedstawienie tego w klarowny sposób. W przypadku rozpatrywanych w tym sprawozdaniu grafów ta reprezentacja wydaje się być najgorszą z poznanych - w grafie pełnym test wszystkich łuków zajmowałby czas rzędu aż $O(n^3)$.

Lista następników jest bardzo przydatna, kiedy zależy nam na szybkim wyszukiwaniu i analizowaniu następników, lub zbiorów następników - na przykład w algorytmie wyszukiwania "w głąb" omawianym wcześniej w tej pracy. Struktura jest prosta w implementacji w **python** oraz opłacalna przy niskich gęstościach - stanowi dobrą alternatywę dla macierzy sąsiedztwa podczas wykonywania DFS.

Lista łuków to dobra reprezentacja przy niskich wartościach $m$ pozwalająca na największe teoretyczne oszczędzenie pamięci zakładając małą gęstość grafu - jej główną zaletą jest zwracanie listy łuków w czasie $O(m)$ oraz wyszukiwanie binarne przy teście łuku w $O(\log m)$ . Zakończenie
Wszystkie reprezentacje mają swoje wady oraz zalety i warto rozważyć wiele czynników podczas decydowania, która z nich jest lepsza do próby rozwiązania okazanego problemu.



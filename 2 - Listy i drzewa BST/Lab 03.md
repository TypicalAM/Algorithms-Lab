# Drzewa BST

## Lista jednokierunkowa

Lista jednokierunkowa zaimplementowana za pomocą listy, statyczna implementacja listy (tablica).

$$
[6,11,4,7,5,8,10,12,2,3,9,1,13,14,15]
$$

- Wyszukiwanie liniowe (wyczerpujące)
  
  - W najgorszym wypadku wyczerpujemy cała listę
  
  - Pesymistycznie mamy element 15 - $O(n)$

- Dopisywanie (na końcu)
  
  - $O(1)$

- Żeby nie wyszukiwać w $O(n)$ lepiej posortować tą tablicę
  
  - $[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]$
  
  - Teraz możemy wyszukiwać binarnie

### Wyszukiwanie binarne w posortowanej

- Szukamy 10
  
  - Indeksujemy element środkowy (8)
  
  - Odrzucamy całą lewą część

- Indeksujemy element środkowy prawej części
  
  - Mamy 12
  
  - Odrzucamy całą prawą część

- Indeksujemy element środkowy lewej pozostałej
  
  - Mamy 10 - sukces!
  
  - Tylko trzy porównania - $O(\log_2 n)$

- Dopisywanie - najgorzej $O(n)$

## Drzewo Binary Search Tree

![](/home/Adam/.config/marktext/images/2022-03-18-12-04-22-image.png)

- Wyszukiwanie binarne
  
  - Szukanie 10
    
    - Przez korzeń (6 jest mniejsze)
      
      - Całe lewe poddrzewo jest wyeliminowane
    
    - Przez korzeń (11 jest większe)
      
      - Całe prawe poddrzewo jest wyeliminowane
  
  - Decyduje najdłuższa ścieżka w drzewie - $O(h)$, gdzie $h$ to wysokość drzewa
    
    - Maksymalna wysokość to $O(n)$
      
      - Zdarzy się jeśli drzewo wpisujemy z posortowanej listy (lub odwrotnie posortowanej)
      
      - Jest to drzewo zdegenerowane do listy
    
    - Minimalna wysokość $h=O(\log_2n)$
      
      - Drzewo dokładnie wyważone
      
      - Dla każdego elementu ilość w lewym i prawym poddrzewie różni się max o 1

- Dopisywanie
  
  - Dopisujemy do drzewa według tej relacji
  
  - Kolejność wpisywanych elementów decyduje o kształcie

- Ta struktura wymaga o wiele więcej pamięci

### Drzewo dokładnie wyważone

Musimy wziąć posortowaną tablicę i wprowadzić do drzewa w następującej kolejności. Jako przykład

$$
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
$$

Środek (8) staje się korzeniem

- Strzelamy w środek lewej tablicy
  
  - Trafiamy na 4, idzie na lewo

- Strzelamy w środek lewej tablicy
  
  - Trafiamy na 2, idzie na lewo -> lewo

Wysokość takiego drzewa to $h=4$

- Przypadek losowy jest bardziej zbliżony do najlepszego niż do najgorszego.

Dopisywanie

- Wadą dokładnie wyważonego drzewa jest fakt, że przy dodawaniu elementów musimy wyważać znowu drzewo.

- Niezmienność danych jest ważna

### Drzewo wyważone

Dla każdego elementu wysokość lewego i prawego poddrzewa różni się o maksymalnie 1.

![](/home/Adam/.config/marktext/images/2022-03-18-12-24-57-image.png)

To jest drzewo wyważone, ale nie dokładnie wyważone

- Wysokości poddrzew, a nie liści różnią się o maks 1

- Lepiej się dokłada elementy, poprawiamy dopiero jak zepsujemy

## Przeglądanie drzewa

### In-order (poprzeczny) L, K, P

Wypisywanie

- Korzeń, zamiast korzenia lewe poddrzewo, potem prawe

- Wszystko robimy rekurencyjnie

## Pre-order (wzdłużny) K, L, P

Wypisywanie

- Korzeń

- Lewe poddrzewo

- Prawe poddrzewo

## Post-order (wsteczny) L, P, K

Wypisywanie

- Zamiast korzenia wypisujemy cały czas w lewo, potem cały czas w prawo.

- To pozwala na usuwanie całego drzewo, jest to zwijane od dołu

### Usunięcie elementu

- Jak mamy liść do po prostu usuwamy

- Poddrzewo
  
  - Podwiązujemy do rodzica zamiast jego

- Dwa poddrzewa
  
  - Coś wstawiamy w miejsce tej wartości
    
    - Spośród mniejszych elementów bierzemy największy
      
      - Raz na lewo, max na prawo
    
    - Spośród większych elementów bierzemy najmniejszy
      
      - Raz na prawo, max na lewo
  
  - jakoś te dwa poddrzewa złączymy
    
    - Dajemy lewy element usuwanego pod jego rodzica,
    
    - Pod podwiązujemy pod największy z najmniejszych
      
      - Z lewej ma jakiś mode
      
      - Z prawej ma prawe dziecko usuwanego elementu

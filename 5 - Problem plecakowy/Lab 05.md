## Problem plecakowy / programowanie dynamiczne

Dane wejściowe

- Zbiór elementów $A=\{a_1,a_2,...,a_n\}$

- Każdy element jest opisany
  
  - Rozmiarem $S(a_i)/S_i$
  
  - Wartością $W(a_i)/W_i$

- Mamy limitowany rozmiar plecaka

- Chcemy wybrać podzbiór elementów taki, że suma elementów nie przekracza rozmiaru plecaka (żebyśmy byli w stanie to unieść) o maksymalnej wartości.

- Jest to problem optymalizacyjny (przeszukiwanie z kryterium)
  
  - Mieliśmy problemy przeszukiwania
  
  - Mieliśmy problemy decyzyjne

Zmienna decyzyjna - $x_i$

- Jeśli wynosi 1 to $a_i$ należy do $A'$ (plecaka)

- Jeśli wynosi 0 to nie

Wszystkich możliwych rozwiązań jest $2^n$

$$
max \sum_{i=1}^nx_iw_i
$$

Mamy jedno ograniczenie

$$
\sum_{i=1}^nx_is_i\leq b
$$

Jest to zadanie programowania matematycznego



### Złożoność opisania problemu

Dla każdego problemu optymalizacyjnego można podać wersję decyzyjną. Dla naszego problemu wersja decyzyjna to - *Czy istnieje rozwiązanie o wartości co najmniej $y$?*. Problemy optymalizacyjne są tak samo trudne, albo trudniejsze niż ich wersje decyzyjne. **Wersja decyzyjna problemu plecakowego jest NP-zupełna (na podstawie dowodu)**. Problem optymalizacyjny jest NP-trudny , a decyzyjny jest NP-zupełny.

- Jeśli jest NP-trudny, to nie ma algorytmu wielomianowego ($P\neq NP$)

- Wszystkie rozwiązania są do sprawdzenia

## Przykład instancji problemu

- $n=5$

- $b=10$

| $i$   | 1   | 2   | 3   | 4   | 5   |
| ----- | --- | --- | --- | --- | --- |
| $s_i$ | 5   | 3   | 4   | 2   | 3   |
| $w_i$ | 3   | 4   | 2   | 6   | 1   |

- Jakie elementy należy wybrać, aby wartość w plecaku była największa

### Metoda siłowa - Brute Force $BF_1$

Chcemy stworzyć wszystkie kombinacje bez powtórzeń - jest $2^n$ podzbiorów. Dla każdego podzbioru trzeba posumować $s_i$ oraz $w_i$ więc dokłada się - $O(n*2^n)$. Na przykład

![](/home/Adam/.config/marktext/images/2022-05-13-12-12-45-image.png)

Lepszym podejściem jest algorytm z powracaniem.

### Algorytm z powracaniem $BF_2$

To samo co Hamilton, jest szybszy od brute force bo nie sprawdzamy wszystkiego i ucinamy rozwiązania. Dalej jest $O(n*2^n)$, ale ten jest szybszy.

![](/home/Adam/.config/marktext/images/2022-05-13-12-15-02-image.png)

## Programowanie dynamiczne $PD$

Dla jakich problemów to się nadaje:

- Dla problemów podzielnych na podproblemy

- Podproblemy są zależne od siebie, czyli posiadających własność optymalnej podstruktury
  
  - Jeśli wybór $k$ elementów jest optymalny to wybór $k-1$ elementów był optymalny

- Ma jakąś funkcję rekurencyjną

Funkcja:

- `f(i,l)` - Opmtymalna wartość elementów `i`  elementów umieszczonych w plecaku o rozmiarze `l`

- `f(n,b)=?`

- Warunki początkowe
  
  - `f(i,0)=0`
  
  - `f(0,l)=0`
  
  - `f(i,l)`
    
    - Jeśli rozmiar elementu i-tego jest większy niż pozostałe miejsce w plecaku $l$
    
    - Mamy rozwiązanie do $l-1$ elementu
    
    - Jeśli element się w plecaku zmieści
      
      - Bierzemy max z dwóch rozwiązań
        
        - `f(i-1,l)`
        
        - `f(i-1,l-S_i)+W+i`, zużyliśmy miejsce w plecaku żeby zwiększyć jego wartość

Liczymy tą funkcję

![](/home/Adam/.config/marktext/images/2022-05-13-12-31-08-image.png)



| i/l | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
|:---:| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
| 1   | 0   | 0   | 0   | 0   | 0   | 3   | 3   | 3   | 3   | 3   | 3   |
| 2   | 0   | 0   | 0   | 4   | 4   | 4   | 4   | 4   | 7   | 7   | 7   |
| 3   | 0   | 0   | 2   | 4   | 4   | 6   | 6   | 6   | 7   | 7   | 9   |
| 4   | 0   | 0   | 2   | 4   | 6   | 6   | 8   | 10  | 10  | 12  | 12  |
| 5   | 0   | 0   | 2   | 4   | 6   | 6   | 8   | 10  | 10  | 12  | 12  |

Na przykład

$f(3,9)=max \{f(2,9),f(2,9-2)+2\}$

Czytanie wyników na koniec

- $f(5,10)=f(4,10) ?x_5=0$

- $f(4,10)\neq f(3,10), x_4=1$

- $f(3,10-4)=f(3,6)\neq f(2,6), x_3=1$

- $f(2,6-2)=f(2,4)\neq f(1,4), x_2=1$

- $f(1,4-3)=f(1,1)=f(1,0),x_1=0$

Tą tabelkę trzeba wypełnić - każda komórka jest liczona w stałym czasie

- Złożoność wypełnienia tabelki i sprawdzania rozwiązania to $O(nb)+O(n)=O(nb)$

- Żeby zapisać dane potrzebujemy $2+2n$

- Algorytm nie jest wielomianowy bo zależy od $b$, które nie jest podane w danych (jeśli $b=100$ to mamy tyle samo danych wejściowych, a złożoność jest kiczowata)

- W maszynie turinga mamy problem
  
  - Jeśli $b$ jest maksymalna, ile potrzebujemy miejsca, aby zakodować instancję
  
  - $log_2 b*(2+2n)$ - zakodowana binarne instancja problemu plecakowego
  
  - Czyli $b=2^{log_2b}$
  
  - Algorytm pseudo-wielomianowy - algorytm nie może zależeć od wartości danych, powinien zależeć od ilości. Algorytm pseudo-wielomianowy to złożoność zależy od rozmiaru problemu i wartości maksymalnej stałej. Jak damy duży plecak to już nie jest wielomianowy, ale w praktyce ten algorytm jest bardzo szybki.
  
  - Problem plecakowy jest NP-zupełny **w zwykłym sensie**, bo posiada algorytm pseudo-wielomianowy

### Heurystyki

Heurerum - przybliżenie. Dla tego problemu można zaproponować przybliżenia szybkie. 

- Brać elementy losowo

- Możemy posortować po rozmiarze rosnąco i zapchać plecak - $O(n\log n)$
  
  - Bierzemy element 3 do plecaka, git
  
  - Bierzemy element 2, git
  
  - Bierzemy element 5, git
  
  - Reszta sie nie mieści, łączna wartość to 7

- Możemy posortować według wartości malejąco = $O(n \log n)$

- Możemy sortować po $\frac{w_i}{s_i}$

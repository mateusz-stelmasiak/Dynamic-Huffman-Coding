# Dynamic-Huffman-Coding
Implementation of dynamic Huffman Coding in Python. Created together with [@Wojciech-Mazurowski](https://github.com/Wojciech-Mazurowski) as a final project for TKIK (Teoria Informacji i Kodowania).

## Opis algorytmu
Dynamiczne kodowanie Huffmana to technika kodowania oparta na kodowaniu Huffmana. Pozwala na budowanie kodu w miarę przesyłania symboli, bez wstępnej wiedzy o alfabecie czy statystyce, co umożliwia adaptację do zmieniających się warunków w danych. 
Przez to, że  kod źródłowy może być kodowany w czasie rzeczywistym, staje się on bardziej wrażliwy na błędy transmisji, ponieważ wystarczy utrata jednego komunikatu aby zniszczyć cały kod.

### Drzewo huffmana
Drzewo Huffmana jest drzewem binarnym, które przechowuje w liściach symbol oraz liczbę jego wystąpień, a w wierzchołkach sumę wystąpień znaków znajdujących się w danej gałęzi.\
![Przykład drzewa Huffmana](https://github.com/mateusz-stelmasiak/Dynamic-Huffman-Coding/assets/46268673/6213b383-59ef-455e-80ec-8adf3896bd72)\
Rysunek 1. Przykład drzewa Huffmana

Każdemu z przejść w lewą stronę drzewa przypisuje się etykietę  ‘0’ a w prawą ‘1’ (patrz Rys. 1). Kod znaku jest wtedy konkatenacją tych etykiet na ścieżce prowadzącej do niego od korzenia. Na powyższym przykładzie kod znaku ‘a’ byłby równy ‘01’, a kod znaku ‘c’ byłby równy ‘00’.

## Dynamiczna budowa drzewa
Poniżej opisano proces dynamicznej budowy drzewa Huffmana.
### Węzeł ZERO
Drzewo jest inicjalizowane przez węzeł ZERO (ang. 0-node). Aby dodać nową literę musimy przesłać jej kod ASCII poprzedzony ścieżką pod którą znajduję się węzeł zero. Wtedy  węzeł ZERO jest rozdzielany na parę - nowy węzeł ZERO (z lewej strony) oraz dodany symbol (z prawej).Poniżej  (patrz Rys 2.) przedstawiono zachowanie węzła zero przy kodowaniu tekstu “ba”.\
![Kodowanie znaków b i a](https://github.com/mateusz-stelmasiak/Dynamic-Huffman-Coding/assets/46268673/89f53f25-abbc-40e8-8bff-d4b461377692)\
Rysunek 2. Kodowanie znaków b i a

W powyższym przykładzie kodem byłoby “[b]0[a]” gdzie [b] i [a] są reprezentacjami ASCII przesyłanych liter  a zero pomiędzy nimi ścieżką wskazującą na węzeł zero.

### Przebudowa drzewa
Przebudowa drzewa, czyli zamiana miejscami niektórych z węzłów, jest konieczna aby zachować optymalność dynamicznego drzewa Huffmana w miarę napływu nowych symboli.
Przebudowę wykonuje się jeżeli po otrzymaniu nowego symbolu i próbie inkrementacji jego wartości drzewo nie zachowuje zasady sibling property tj. przy przejściu drzewa wszerz od prawej do lewej i odczycie liczników powiązanych z każdym węzłem uzyskuje się ciąg liczb nierosnących.  Różne implementacje algorytmu mogą zachować zasadę przez inne przebudowy drzewa. Ważne jest więc, aby koder i dekoder tworzyły drzewa w ten sam sposób. Dlatego też, zgubienie jednego symbolu w trakcie przesyłania w czasie rzeczywistym, sprawia, że wiadomośc nie może być poprawnie  zdekodowana.

## Proces kodowania
1. Zainicjalizowanie drzewa przez rozdzielenie węzła ZERO na parę - nowy węzeł zero oraz pierwszy przesłany symbol.
2. Przesyłanie dalszego kodu:
    1. Zostaje przesłany nowy symbol, poprzedzony kodem prowadzącym do  węzła zero.
    2. Zostaje przesłany kod prowadzący już do istniejącego symbolu.
3. W zależności od kodu:
    1. Węzeł zero rozdziela się na parę - nowy węzeł, wprowadzony symbol.
    2. Inkrementuje wystąpienie znaku o jeden.
4. Drzewo w razie naruszenia sibling property odpowiednio się przebudowywuje (patrz Przebudowa drzewa).
5. Powtarzamy punkty 2-4 dopóki nie skończy się przesyłanie tekstu.

## Proces dekodowania
1. Zainicjalizowanie drzewa przez rozdzielenie węzła ZERO na parę - nowy węzeł zero oraz pierwszy odebrany symbol.
2. Odbieranie dalszego kodu:
    1. Zostaje odebrany nowy symbol, poprzedzony kodem prowadzącym do  węzła zero.
    2. Zostaje odebrany kod prowadzący już do istniejącego symbolu.
3. W zależności od kodu:
    1. Węzeł zero rozdziela się na parę - nowy węzeł, wprowadzony symbol.
    2. Inkrementuje wystąpienie znaku o jeden.
4. Drzewo w razie naruszenia sibling property odpowiednio się przebudowywuje (patrz 2.2. Przebudowa drzewa).
5. Powtarzamy punkty 2-4 dopóki nie skończy się czytanie tekstu.



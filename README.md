### Oculi Mundi - prowizoryczna strzelanka napisana przy pomocy biblioteki PyGame
## Spis treści
* [Opis](#opis)
* [Technologie](#technologie)
* [Uruchomienie](#uruchomienie)
* [Demo](#demo)
* [Autor](#autor)
 
 ## Opis
Powyższej znajduje się kod źródłowy prostej strzelanki napisanej w języku Python w ramach kursu Grafika komputerowa i komunikacja człowiek-komputer. Projekt dzieli się na dwie części: pierwszą z nich stanowi surowa "logika" gry (jak przemieszczają się pociski, gracz i przeciwnik), natomiast druga obsługuje grafikę i jest oparta na silniku z książki "Developing Graphics Frameworks with Python and OpenGL" Lee Stemkoski i Michael Pascale.


 ## Technologie
Projekt został napisany w całości w języku Python 3 z następującymi bibliotekami
* pygame==2.5.2
* PyOpenGL==3.1.7
* PyOpenGL-accelerate==3.1.7

## Uruchomienie
Aby lokalnie uruchomić projekt, najpierw należy sklonować repozytorium

``` bash
git clone https://github.com/Barionetta/oculi-mundi.git
```

Następnie stworzyć wirtualne środowisko o nazwie `oculimundi-dev`

```bash
conda create --name oculimundi-dev python=3.11
```

Później należy aktywować środowisko

```bash
conda activate oculimundi-dev
```

Na końcu zainstalować wymagane paczki

```bash
pip install -e .
```

Kod można uruchomić w następujący sposób:

```bash
oculimundi
```

## Demo
<p>Demonstracja gry:</p>

![D1](/assets/demo1.png)
![D2](/assets/demo2.png)

## Autor
Autorem projektu jest Katarzyna Matuszek


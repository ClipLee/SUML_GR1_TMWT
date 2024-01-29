<!-- dokumentacja projektu -->

# SUML_GR1_TMWT

> Webowa aplikacja do przewidywania pogody, bazując na danych z poprzednich lat.

## Twórcy

- Dominika Balcerowska <s22647@pejot.edu.pl>
- Krzysztof Lipski @ClipLee <s20901@pjwstk.edu.pl>
- Filip Woźniak <s22703@pjwstk.edu.pl>

## Instalacja

Pobierz repozytorium i zainstaluj wymagane pakiety:

`pip install -r requirements.txt`

## Uruchomienie

W konsoli, w głównym katalogu projektu, uruchom: `python app/app.py`

## Struktura Projektu

`app/app.py`: Główny skrypt aplikacji.
`model.h5` i `app/model.h5`: Zapisane modele uczenia maszynowego.
`data/`: Katalog zawierający dane używane do trenowania modelu.
`data_prep.ipynb`: Notatnik Jupyter używany do przygotowania i czyszczenia danych.
`model.ipynb`: Notatnik Jupyter używany do trenowania modelu uczenia maszynowego.

## Dane

Zbiór danych "Rain in Australia" składających się z informacji o opadach deszczu w różnych regionach Australii.

Dataset: dane pogodowe z stacji meteoroligocznych w Australii na przestrzeni lat 2007-2017

Predykcja: Aplikacja będzie przewidywać pogodę w danym dniu/ tygodniu

Uzasadnienie funkcjonalności aplikacji: Aplikacja będzie wykorzystać dane pogodowe z ostatnich lat, aby przewidzieć jaka pogoda będzie w danym dniu lub tygodniu.

Funkcjonalność aplikacji mogłaby obejmować:

- Możliwość wprowadzenia danych pogodowych z danego regionu
- Generowanie prognozy pogody na podstawie wprowadzonych danych
- Wizualizację prognozy pogody w postaci wykresów lub map

Zastosowany model uczenia maszynowego: Regresja liniowa bądź logistyczna

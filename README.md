<!-- dokumentacja projektu -->

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

# SUML_GR1_TMWT

> Webowa aplikacja do opadów deszczu, bazując na danych z poprzednich lat.

## Procesy

Projekt tworzony jest na podstawie procesów zdefiniowanych w ramach przedmiotu "Środowiska Uruchomieniowe AutoML" na Polsko-Japońskiej Akademii Technik Komputerowych.

## Twórcy

- Dominika Balcerowska <s22647@pejot.edu.pl> — Model uczenia maszynowego
- Krzysztof Lipski @ClipLee <s20901@pjwstk.edu.pl> — Dokumentacja projektu, przygotowanie danych
- Filip Woźniak <s22703@pjwstk.edu.pl> — Aplikacja streamlit

## Znane problemy i ograniczenia

- Aplikacja nie uwzględnia danych pogodowych z innych regionów niż Australia
- Aplikacja nie uwzględnia danych pogodowych z innych lat niż 2007-2017
- Aplikacja nie uwzględnia danych pogodowych z innych stacji meteorologicznych niż te, które zostały uwzględnione w zbiorze danych
- Model uczenia maszynowego nie jest optymalizowany pod kątem wydajności

# Aplikacja lokalna

## Instalacja

Pobierz repozytorium i zainstaluj wymagane pakiety:

`pip install -r requirements.txt`

## Uruchomienie aplikacji z konsoli

W konsoli, w głównym katalogu projektu, uruchom: `streamlit run app/app.py`

## Struktura Projektu

`app/app.py`: Główny skrypt aplikacji.
`model.h5` i `app/model.h5`: Zapisane modele uczenia maszynowego.
`data/`: Katalog zawierający dane używane do trenowania modelu.
`data_prep.ipynb`: Notatnik Jupyter używany do przygotowania i czyszczenia danych.
`model.ipynb`: Notatnik Jupyter używany do trenowania modelu uczenia maszynowego.

## Dane

Zbiór danych "Rain in Australia" składających się z informacji o opadach deszczu w różnych regionach Australii.

Dataset: dane pogodowe z stacji meteoroligocznych w Australii na przestrzeni lat 2007-2017

Predykcja: Aplikacja będzie przewidywać opady deszczu w kolejnym dniu

Uzasadnienie funkcjonalności aplikacji: Aplikacja będzie wykorzystać dane pogodowe z ostatnich lat, aby przewidzieć opady deszczuw kolejnym dniu.

Funkcjonalność aplikacji w przyszłości mogłaby obejmować:

- Możliwość wprowadzenia danych pogodowych z danego regionu
- Generowanie prognozy pogody na podstawie wprowadzonych danych
- Wizualizację prognozy pogody w postaci wykresów lub map

Zastosowany model uczenia maszynowego: Regresja liniowa bądź logistyczna

## Konfiguracja

Aplikacja nie wymaga specjalnej konfiguracji. Wszystkie wymagane pakiety są wymienione w pliku `requirements.txt`.

## Testy

Projekt nie zawiera jeszcze testów jednostkowych. Planujemy dodać je w przyszłości.

## FAQ

**Q: Czy mogę używać tej aplikacji do przewidywania opadów deszczu w innych krajach?**
A: Nie, aplikacja jest obecnie zaprojektowana do przewidywania opadów deszczu tylko w Australii.

**Q: Czy mogę używać tej aplikacji do przewidywania opadów deszczu w innych latach?**
A: Nie, aplikacja jest obecnie zaprojektowana do przewidywania opadów deszczu tylko na podstawie danych z lat 2007-2017.

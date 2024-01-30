<!-- dokumentacja projektu -->

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

# SUML_GR1_TMWT

> Webowa aplikacja do predykcji opadów deszczu, bazując na danych z poprzednich lat.

## Aplikacja webowa

Aplikacja dostępna jest pod adresem: [https://rain-prediction.streamlit.app/](https://rain-prediction.streamlit.app/)

### Jak korzystać

Należy przejść na stronę aplikacji webowej i po uruchomieniu aplikacji wprowadzić dane pogodowe z danego regionu. Dane pogodowe można wprowadzić ręcznie lub za pomocą przycisków. Po wprowadzeniu danych należy kliknąć przycisk "Przewiduj". Aplikacja wyświetli prognozę pogody na kolejny dzień.

Aplikacja posiada następujące elementy możliwe do zmiany:

- MinTemp - jest to minimalna temperatura w danym dniu
- MaxTemp - jest to maksymalna temperatura w danym dniu
- Rainfall - jest to opad deszczu w danym dniu w milimetrach
- WindGustSpeed - prędkość (km/h) najmocniejszego porywu wiatru w ciągu 24 godzin do północy
- WindSpeed9am - jest to prędkość wiatru o 9 rano w danym dniu
- WindSpeed3pm - jest to prędkość wiatru o 15 po południu w danym dniu
- Humidity3pm - jest to wilgotność powietrza o 15 po południu w danym dniu
- Pressure9am - jest to ciśnienie atmosferyczne o 9 rano w danym dniu
- Pressure3pm - jest to ciśnienie atmosferyczne o 15 po południu w danym dniu
- Latitude - jest to szerokość geograficzna
- Longitude - jest to długość geograficzna
- Year - jest to rok w którym mamy przewidzieć opady deszczu
- Month - jest to miesiąc w którym mamy przewidzieć opady deszczu
- Day - jest to dzień w którym mamy przewidzieć opady deszczu
- Location - jest to lokalizacja w której mamy przewidzieć opady deszczu
- WindGustDir - jest to kierunek najmocniejszego porywu wiatru w ciągu 24 godzin do północy
- WindDir9am - jest to kierunek wiatru o 9 rano w danym dniu
- WindDir3pm - jest to kierunek wiatru o 15 po południu w danym dniu

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

### Docker

Dodatkowo należy zainstalować Docker'a. Następnie należy uruchomić kontener Docker:

`docker compose up`

### Docker-less

Ewentualnie można uruchomić aplikację bez kontenera Docker:

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

## Użyte technologie

Projekt korzysta z następujących technologii:

- [Flask](https://flask.palletsprojects.com/) i [Streamlit](https://streamlit.io/): Biblioteki Pythona do tworzenia aplikacji internetowych.
- [Numpy](https://numpy.org/) i [Pandas](https://pandas.pydata.org/): Biblioteki Pythona do manipulacji i analizy danych.
- [Cufflinks](https://github.com/santosjorge/cufflinks), [Matplotlib](https://matplotlib.org/) i [Seaborn](https://seaborn.pydata.org/): Biblioteki Pythona do wizualizacji danych.
- [Scikit-learn](https://scikit-learn.org/), [Tensorflow](https://www.tensorflow.org/) i [Category Encoders](https://contrib.scikit-learn.org/category_encoders/): Biblioteki Pythona do uczenia maszynowego.
- [Ipykernel](https://ipython.org/ipython-doc/3/development/kernels.html): Pakiet Pythona do uruchamiania interaktywnych notatników Jupyter.

## Dane

Zbiór danych "Rain in Australia" składających się z informacji o opadach deszczu w różnych regionach Australii. Pochodzi on ze strony Kaggle.com i jest dostępny pod adresem: [https://www.kaggle.com/jsphyg/weather-dataset-rattle-package](https://www.kaggle.com/jsphyg/weather-dataset-rattle-package). Zbiór danych zawiera 142193 rekordów i 24 kolumny. Dane pochodzą z lat 2007-2017. Ten zbiór danych zawiera około 10 lat codziennych obserwacji pogody z licznych australijskich stacji pogodowych.

RainTomorrow jest to zmienną docelową do przewidzenia. To znaczy: czy następnego dnia padał deszcz? Tak czy Nie?

## Predykcja

 Aplikacja będzie przewidywać opady deszczu w kolejnym dniu

Uzasadnienie funkcjonalności aplikacji: Aplikacja będzie wykorzystać dane pogodowe z ostatnich lat, aby przewidzieć opady deszczuw kolejnym dniu.

Funkcjonalność aplikacji:

- Możliwość wprowadzenia danych pogodowych z danego regionu
- Generowanie prognozy pogody na podstawie wprowadzonych danych

## Model uczenia maszynowego

Zastosowany model uczenia maszynowego: Model uczenia maszynowego użyty w tej aplikacji to regresja liniowa. Model został przeszkolony na zbiorze danych "Rain in Australia". Dokładność modelu: 0.8282

## Konfiguracja

Aplikacja nie wymaga specjalnej konfiguracji. Wszystkie wymagane pakiety są wymienione w pliku `requirements.txt`.

## Testy

Projekt nie zawiera jeszcze testów jednostkowych. Planujemy dodać je w przyszłości.

## FAQ

**Q: Czy mogę używać tej aplikacji do przewidywania opadów deszczu w innych krajach?**
A: Nie, aplikacja jest obecnie zaprojektowana do przewidywania opadów deszczu tylko w Australii.

**Q: Czy mogę używać tej aplikacji do przewidywania opadów deszczu w innych latach?**
A: Nie, aplikacja jest obecnie zaprojektowana do przewidywania opadów deszczu tylko na podstawie danych z lat 2007-2017.

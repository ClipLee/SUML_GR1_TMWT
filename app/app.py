import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import category_encoders as ce

# encoder 
def load_encoder():
    with open('encoder.pkl', 'rb') as file:
        encoder = pickle.load(file)
    return encoder
encoder = load_encoder()
# model
@st.cache
def load_model():
    with open('model.h5', 'rb') as file:
        model = pickle.load(file)
    return model

# funkcja do przetwarzania danych wejsciowych
def process_input(data, encoder):
    # kodowanie binarne dla rain today
    data = encoder.transform(data)

    # zmienne dummy
    data = pd.get_dummies(data, columns=['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'Coordinates'])

    # skalowanie
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data)

    return data

def main():
    st.set_page_config(page_title="Czy jutro będzie padać?")
    st.title("Czy jutro będzie padać?")

    # formularz
    with st.form(key='input_form'):
        min_temp = st.number_input('MinTemp', value=10.0)
        max_temp = st.number_input('MaxTemp', value=20.0)
        rainfall = st.number_input('Rainfall', value=0.0)
        wind_gust_speed = st.number_input('WindGustSpeed', value=40.0)
        wind_speed_9am = st.number_input('WindSpeed9am', value=20.0)
        wind_speed_3pm = st.number_input('WindSpeed3pm', value=20.0)
        humidity_3pm = st.number_input('Humidity3pm', value=50)
        pressure_9am = st.number_input('Pressure9am', value=1010.0)
        pressure_3pm = st.number_input('Pressure3pm', value=1010.0)
        year = st.number_input('Year', min_value=2000, max_value=2020, value=2010)
        month = st.number_input('Month', min_value=1, max_value=12, value=6)
        day = st.number_input('Day', min_value=1, max_value=31, value=15)
        rain_today = st.selectbox('RainToday', ['Yes', 'No'])
        location = st.selectbox('Location', ['Location1', 'Location2', 'Location3']) # to tylko dla testu
        wind_gust_dir = st.selectbox('WindGustDir', ['N', 'S', 'E', 'W'])
        wind_dir_9am = st.selectbox('WindDir9am', ['N', 'S', 'E', 'W'])  
        wind_dir_3pm = st.selectbox('WindDir3pm', ['N', 'S', 'E', 'W'])  
        coordinates = st.selectbox('Coordinates', ['Coord1', 'Coord2', 'Coord3'])  

        submit_button = st.form_submit_button(label='Predict')

    if submit_button:
        # przygtowanie danych wejsciowych
        input_data = pd.DataFrame([[min_temp, max_temp, rainfall, wind_gust_speed, wind_speed_9am, wind_speed_3pm,
                                    humidity_3pm, pressure_9am, pressure_3pm, year, month, day, rain_today,
                                    location, wind_gust_dir, wind_dir_9am, wind_dir_3pm, coordinates]],
                                  columns=['MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm',
                                           'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Year', 'Month', 'Day', 'RainToday',
                                           'Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'Coordinates'])
        
        encoder = load_encoder()
        # dane wejściowe
        processed_data = process_input(input_data, encoder)

        # model
        model = load_model()

        # predykcja
        prediction = model.predict(processed_data)
        st.write(f'Prediction: {"Rain" if prediction[0] == "Yes" else "No Rain"}')

if __name__ == "__main__":
    main()
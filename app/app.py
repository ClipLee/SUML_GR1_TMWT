"""
This module contains a Streamlit application for predicting whether it will rain tomorrow.
"""

from json import encoder
import pickle
from pyexpat import model
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import streamlit as st
import pickle

# pylint: disable=invalid-name, too-many-locals, too-many-statements, too-many-arguments


def load_encoder():
    """Load the encoder from a pickle file."""
    with open('encoder.pkl', 'rb') as file:
        encoder = pickle.load(file)
    return encoder


@st.cache
def load_model():
    """Load the model from a pickle file."""
    with open('model.h5', 'rb') as file:
        model = pickle.load(file)
    return model


def load_model_columns():
    """Load the model columns from a pickle file."""
    with open('model_columns.pkl', 'rb') as file:
        columns = pickle.load(file)
    return columns


def load_scaler():
    """Load the scaler from a pickle file."""
    with open('scaler.pkl', 'rb') as file:
        scaler = pickle.load(file)
    return scaler


def process_input(data, encoder, features, scaler):
    """Process the input data for the model."""
    data_binary_encoded = encoder.transform(data)

    categorical_columns = ['Location',
                           'WindGustDir', 'WindDir9am', 'WindDir3pm']
    data_one_hot_encoded = pd.get_dummies(
        data_binary_encoded[categorical_columns])

    data_combined = pd.concat([data.drop(
        ['RainToday'] + categorical_columns, axis=1), data_one_hot_encoded], axis=1)

    for col in features:
        if col not in data_combined.columns:
            data_combined[col] = 0.5
    data_prepared = data_combined.reindex(columns=features)

    data_scaled = scaler.transform(data_prepared)

    return data_scaled


def main():
    """The main function of the Streamlit application."""
    st.set_page_config(page_title="Czy jutro będzie padać?")
    st.title("Czy jutro będzie padać?")


def main():

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
        latitude = st.number_input('Latitude', value=-37.81)
        longtitude = st.number_input('Longtitude', value=144.97)
        year = st.number_input('Year', min_value=2000,
                               max_value=2020, value=2010)
        month = st.number_input('Month', min_value=1, max_value=12, value=6)
        day = st.number_input('Day', min_value=1, max_value=31, value=15)
        rain_today = st.selectbox('RainToday', ['Yes', 'No'])
        location = st.selectbox('Location',
                                ['Adelaide', 'Albany', 'Albury', 'AliceSprings', 'Ballarat', 'Bendigo', 'Brisbane', 'Cairns', 'Canberra',
                                 'Darwin', 'GoldCoast', 'Hobart', 'Launceston', 'Melbourne', 'MountGambier', 'MountGinini', 'Newcastle', 'Penrith',
                                 'Perth', 'Sydney', 'Townsville', 'Tuggeranong', 'Wollongong'
                                 ])

        wind_gust_dir = st.selectbox('WindGustDir', ['N', 'S', 'E', 'W'])
        wind_dir_9am = st.selectbox('WindDir9am', ['N', 'S', 'E', 'W'])
        wind_dir_3pm = st.selectbox('WindDir3pm', ['N', 'S', 'E', 'W'])

        submit_button = st.form_submit_button(label='Przewidź')

    if submit_button:
        # Prepare input data
        input_data = pd.DataFrame([[min_temp, max_temp, rainfall, wind_gust_speed, wind_speed_9am, wind_speed_3pm,
                                    humidity_3pm, pressure_9am, pressure_3pm, latitude, longtitude, year, month, day, rain_today,
                                    location, wind_gust_dir, wind_dir_9am, wind_dir_3pm]],
                                  columns=['MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm',
                                           'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Latitude', 'Longitude', 'Year', 'Month', 'Day', 'RainToday',
                                           'Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm'])
        # Model prediction
        model_columns = load_model_columns()
        scaler = load_scaler()  # Fix: Define the variable 'scaler' by calling the 'load_scaler()' function
        processed_data = process_input(
            input_data, encoder, model_columns, scaler)
        prediction = model.predict(processed_data)
        st.write(f'Predykcja: {"Rain" if prediction[0] == "Deszcz" else "Brak deszczu"}')


if __name__ == "__main__":
    main()
